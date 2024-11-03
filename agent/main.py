import time
from actions.screen_recognition import capture_screen, extract_and_process_region_for_text, recognize_text  # 画像認識系をscreen_recognitionに移動
from domains.battle import Battle
from domains.field import BattleField
from domains.player import Opponent, Player

# バトルとプレイヤーの初期化
battle = Battle(first_player="player")
player = Player(name="自分")
oppnent = Opponent(name="相手")
battle_field = BattleField()

def waiting():
    """対戦相手を探している状態の処理"""
    print("Waiting for opponent...")
    # 必要ならばこの状態での処理を追加

def init_battle(is_player_first):
    """対戦開始の初期化処理"""
    global battle, player, opponent, battle_field
    battle = Battle(first_player="player" if is_player_first else "opponent")  # バトルの再初期化
    player = Player(name="自分")  # プレイヤーの再初期化
    opponent = Opponent(name="相手")  # 相手の再初期化
    battle_field = BattleField()  # バトルフィールドの再初期化
    print(f"Battle initialized. Player goes first: {is_player_first}")


def my_turn():
    """自分のターンの処理"""
    print("Executing my turn...")
    # 戦場の情報を更新し、アクションを実行するための手順をここで記述します
    # 例：エネルギーのアタッチ、サポート・アイテムの使用、特性やわざの使用など
    # player.attach_energy() や player.use_support() などのメソッドを使う

def main():
    screenshot = capture_screen()
    state = detect_state(screenshot)
    if state == "waiting":
        waiting()
    elif state == "init_battle_player_first":
        init_battle(is_player_first=True)
    elif state == "init_battle_opponent_first":
        init_battle(is_player_first=False)
    elif state == "my_turn":
        my_turn()
    else:
        print("Unknown state detected")
    # """メインの処理ループ"""
    # while True:
    #     screenshot = capture_screen()
    #     state = detect_state(screenshot)

    #     if state == "waiting":
    #         waiting()
    #     elif state == "init_battle_player_first":
    #         init_battle(is_player_first=True)
    #     elif state == "init_battle_opponent_first":
    #         init_battle(is_player_first=False)
    #     elif state == "my_turn":
    #         my_turn()
    #     else:
    #         print("Unknown state detected")

    #     # 4. 一定時間待機して次のスクリーンショット取得まで待つ
    #     time.sleep(1)  # 1秒ごとにチェック（必要に応じて調整）

def detect_state(screenshot, battle_started=False, setting_up=False):
    """現在のゲームの状態を検出する

    Args:
        screenshot: スクリーンショット画像
        battle_started (bool): バトルがすでに始まっているかどうかのフラグ
    """
    # バトルがまだ始まっていない場合のみ、初期テキストを確認
    if not battle_started:
        init_text_screenshot = extract_and_process_region_for_text(screenshot, 170, 270, 240, 305)
        init_text = recognize_text(init_text_screenshot, 'init_text.png')

        # 「先攻」または「後攻」の文字を確認して、バトル開始の状態を検出
        if "先攻" in init_text:
            return "init_battle_player_first"
        elif "後攻" in init_text:
            return "init_battle_opponent_first"
        else:
            return "waiting"
    
    # バトルが始まっている場合、たねポケモンをバトル場に出してくださいと表示されるまで待つ
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
