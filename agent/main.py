import time
from actions.screen_recognition import capture_screen, extract_and_process_region_for_text, recognize_text
from domains.battle import Battle
from domains.field import BattleField
from domains.player import Opponent, Player

# バトルとプレイヤーの初期化
battle = Battle(first_player="player")
player = Player(name="自分")
opponent = Opponent(name="相手")
battle_field = BattleField()

def waiting():
    print("Waiting ...")

def init_battle(is_player_first):
    """対戦開始の初期化処理"""
    global battle, player, opponent, battle_field
    battle = Battle(first_player="player" if is_player_first else "opponent")  # バトルの再初期化
    player = Player(name="自分")  # プレイヤーの再初期化
    opponent = Opponent(name="相手")  # 相手の再初期化
    battle_field = BattleField()  # バトルフィールドの再初期化
    print(f"Battle initialized. Player goes first: {is_player_first}")

def setup_battlefield():
    """バトル場の設定"""
    print("Setting up battlefield...")
    # 手札の確認し、Playerのhandsを更新する
    # 手札のたねポケモンをバトル場に出す
    # 手札にたねポケモンがある場合、ベンチに出す

def my_turn():
    """自分のターンの処理"""
    print("Executing my turn...")

def main():
    battle_started = False  # バトルが開始されたかどうか
    setting_up = False      # バトル場の設定中かどうか

    while True:
        screenshot = capture_screen()
        state = detect_state(screenshot, battle_started=battle_started, setting_up=setting_up)

        if state == "waiting":
            waiting()
        elif state == "init_battle_player_first":
            init_battle(is_player_first=True)
            battle_started = True
            setting_up = True
        elif state == "init_battle_opponent_first":
            init_battle(is_player_first=False)
            battle_started = True
            setting_up = True
        elif state == "setting_up":
            print("Setting up battlefield...")
            setting_up = False
        elif state == "my_turn":
            my_turn()
        else:
            print("Unknown state detected")

        time.sleep(1)  # 1秒ごとにチェック（必要に応じて調整）

def detect_state(screenshot, battle_started=False, setting_up=False):
    """現在のゲームの状態を検出する

    Args:
        screenshot: スクリーンショット画像
        battle_started (bool): バトルがすでに始まっているかどうかのフラグ
        setting_up (bool): バトル場の設定中かどうかのフラグ
    """
    # バトルがまだ始まっていない場合のみ、初期テキストを確認
    if not battle_started:
        init_text_screenshot = extract_and_process_region_for_text(screenshot, 208, 187, 240, 209)
        init_text = recognize_text(init_text_screenshot, 'init_text.png')
        print(init_text)
        # 「先攻」または「後攻」の文字を確認して、バトル開始の状態を検出
        if "先攻" in init_text:
            return "init_battle_player_first"
        elif "後攻" in init_text:
            return "init_battle_opponent_first"
        else:
            return "waiting"
    
    # バトルが始まっていて、設定中の状態を確認
    if battle_started and setting_up:
        setup_text_screenshot = extract_and_process_region_for_text(screenshot, 100, 200, 500, 250)
        setup_text = recognize_text(setup_text_screenshot, 'setup_text.png')

        if "たねポケモンをバトル場に出してください" in setup_text:
            return "setting_up"
        else:
            return "waiting"

    # バトルが始まっている場合、スクリーンショットから現在のターンを検出
    my_turn_text_screenshot = extract_and_process_region_for_text(screenshot, 100, 200, 500, 250)
    my_turn_text = recognize_text(my_turn_text_screenshot, 'my_turn_text.png')

    if "あなたのターンです" in my_turn_text:
        return "my_turn"

    # 状態が判定できなかった場合
    return "unknown"

if __name__ == "__main__":
    main()
