# actions/main.py

import argparse
import time

import pyautogui

screen_x = 1500
screen_y = 50

active_spot_x = screen_x + 215
active_spot_y = screen_y + 500
bench1_spot_x = screen_x + 110
bench1_spot_y = screen_y + 670
bench2_spot_x = screen_x + 210
bench2_spot_y = screen_y + 670
bench3_spot_x = screen_x + 310
bench3_spot_y = screen_y + 670

ready_to_play_button_x = screen_x + 345
ready_to_play_button_y = screen_y + 430

energy_spot_x = screen_x + 370
energy_spot_y = screen_y + 770

def click_active_spot():
    start_x = screen_x + 300
    start_y = screen_y + 800
    total_cards = 5
    spacing = 100
    index = 0
    """
    手札内のカードの位置を計算する
    index: カードのインデックス（0から始まる）
    total_cards: 手札にあるカードの総数
    start_x, start_y: 手札の基準位置
    spacing: カード間の間隔
    """
    # 手札のカードが中央に並ぶように配置を調整
    offset_x = start_x - (spacing * (total_cards - 1)) // 2 + (spacing * index)
    return offset_x, start_y

def check_my_cards():
    drag_and_drop(screen_x + 300, screen_y + 800, screen_x + 100,  screen_y + 800)

def ready_to_play():
    click(ready_to_play_button_x, ready_to_play_button_y)

def finish_my_turn():
    click(ready_to_play_button_x, ready_to_play_button_y)

def take_pokemon_active_spot():
    start_x = screen_x + 300
    start_y = screen_y + 800
    end_x = active_spot_x
    end_y = active_spot_y
    drag_and_drop(start_x, start_y, end_x, end_y)

def take_pokemon_bench(spot=1):
    """
    ベンチの指定したスポットにポケモンを移動する
    spot: ベンチのスポット番号（1, 2, 3）
    """
    start_x = screen_x + 300
    start_y = screen_y + 800
    if spot == 1:
        end_x, end_y = bench1_spot_x
    elif spot == 2:
        end_x, end_y = bench2_spot_x
    elif spot == 3:
        end_x, end_y = bench3_spot_x
    drag_and_drop(start_x, start_y, end_x, end_y, waypoints=[(start_x, end_y)], )

def attach_energy(pokemon_spot):
    """
    エネルギーを指定したスポット（アクティブまたはベンチ）に移動する
    pokemon_spot: "active", "bench1", "bench2", "bench3" などの文字列で指定
    """
    start_x = energy_spot_x
    start_y = energy_spot_y

    # 移動先の座標を pokemon_spot に基づいて設定
    if pokemon_spot == "active":
        end_x, end_y = active_spot_x, active_spot_y
    elif pokemon_spot == "bench1":
        end_x, end_y = bench1_spot_x, bench1_spot_y
    elif pokemon_spot == "bench2":
        end_x, end_y = bench2_spot_x, bench2_spot_y
    elif pokemon_spot == "bench3":
        end_x, end_y = screen_x + 310, screen_y + 670
    else:
        print("Invalid pokemon spot specified")
        return

    # ドラッグアンドドロップでエネルギーを移動
    drag_and_drop(start_x, start_y, end_x, end_y)

def use_item():
    start_x = screen_x + 300
    start_y = screen_y + 800
    end_x = active_spot_x
    end_y = active_spot_y
    drag_and_drop(start_x, start_y, end_x, end_y)

def use_ability(pokemon_spot):
    """
    指定したスポットのポケモンの特性を使う（アクティブまたはベンチ）
    pokemon_spot: "active", "bench1", "bench2", "bench3" などの文字列で指定
    """
    if pokemon_spot == "active":
        x, y = active_spot_x, active_spot_y
    elif pokemon_spot == "bench1":
        x, y = bench1_spot_x, bench1_spot_y
    elif pokemon_spot == "bench2":
        x, y = bench2_spot_x, bench2_spot_y
    elif pokemon_spot == "bench3":
        x, y = bench3_spot_x, bench3_spot_y
    else:
        print("Invalid pokemon spot specified")
        return
    click(x, y)
    time.sleep(0.1)
    click(x, y + 100)
    

def use_supporter():
    start_x = screen_x + 300
    start_y = screen_y + 800
    end_x = active_spot_x
    end_y = active_spot_y
    drag_and_drop(start_x, start_y, end_x, end_y)

def use_attack(index=0, attacks=1):
    click(active_spot_x, active_spot_y)
    click(active_spot_x, active_spot_y + 190)

def retreat(to="bench1"):
    if(to == "bench1"):
        to_x, to_y = bench1_spot_x, bench1_spot_y
    elif(to == "bench2"):
        to_x, to_y = bench2_spot_x, bench2_spot_y
    elif(to == "bench3"):
        to_x, to_y = bench3_spot_x, bench3_spot_y
    click(active_spot_x, active_spot_y)
    time.sleep(0.1)
    click(active_spot_x, active_spot_y + 250)
    time.sleep(0.1)
    click(to_x, to_y)

def evolve_pokemon(spot="active"):
    """
    指定したスポットのポケモンを進化させる
    spot: "active", "bench1", "bench2", "bench3" などの文字列で指定
    """
    start_x = screen_x + 300
    start_y = screen_y + 800
    
    if spot == "active":
        end_x, end_y = active_spot_x
    elif spot == "bench1":
        end_x, end_y = bench1_spot_x
    elif spot == "bench2":
        end_x, end_y = bench2_spot_x
    elif spot == "bench3":
        end_x, end_y = bench3_spot_x
    drag_and_drop(start_x, start_y, end_x, end_y, waypoints=[(start_x, end_y)], )

def calculate_card_position(index, total_cards, start_x, start_y, spacing=100):
    """
    手札内のカードの位置を計算する
    index: カードのインデックス（0から始まる）
    total_cards: 手札にあるカードの総数
    start_x, start_y: 手札の基準位置
    spacing: カード間の間隔
    """
    # 手札のカードが中央に並ぶように配置を調整
    offset_x = start_x - (spacing * (total_cards - 1)) // 2 + (spacing * index)
    return offset_x, start_y

def main():
    # argparseの設定
    parser = argparse.ArgumentParser(description="Game Actions CLI")
    
    # サブコマンドを定義
    subparsers = parser.add_subparsers(dest="action", help="Available actions")
    
    # 各アクションに対応するサブコマンドを追加
    subparsers.add_parser("click_active_spot", help="Click active spot")
    subparsers.add_parser("check_my_cards", help="Check my cards")
    subparsers.add_parser("ready_to_play", help="Ready to play")
    subparsers.add_parser("finish_my_turn", help="Finish my turn")
    subparsers.add_parser("take_pokemon_active_spot", help="Take Pokemon active spot")
    take_pokemon_bench_parser = subparsers.add_parser("take_pokemon_bench", help="Take Pokemon bench spot")
    take_pokemon_bench_parser.add_argument("spot", type=int, choices=[1, 2, 3], help="Specify the bench spot to take Pokemon (1, 2, 3)")
    attach_energy_parser = subparsers.add_parser("attach_energy", help="Attach energy to specified spot")
    attach_energy_parser.add_argument("pokemon_spot", choices=["active", "bench1", "bench2","bench3"], help="Specify the spot to attach energy (active, bench1, bench2, bench3, ...)")
    subparsers.add_parser("use_item", help="Use an item")
    use_ability_parser = subparsers.add_parser("use_ability", help="Use an ability")
    use_ability_parser.add_argument("pokemon_spot", choices=["active", "bench1", "bench2", "bench3"], help="Specify the spot to use ability (active, bench1, bench2, bench3, ...)")
    subparsers.add_parser("use_supporter", help="Use a supporter")
    subparsers.add_parser("use_attack", help="Use an attack")
    use_attack_parser = subparsers.add_parser("use_attack", help="Use an attack")
    use_attack_parser.add_argument("index", type=int, default=0, help="Specify the index of the attack to use")
    use_attack_parser.add_argument("attacks", type=int, default=1, help="Specify the number of attacks to use")
    subparsers.add_parser("retreat", help="Retreat active Pokemon")
    # subparsers.add_parser("evolve_pokemon", help="Evolve active Pokemon")
    evolve_pokemon_parser = subparsers.add_parser("evolve_pokemon", help="Evolve Pokemon")
    evolve_pokemon_parser.add_argument("spot", choices=["active", "bench1", "bench2","bench3"], help="Specify the bench spot to evolve Pokemon (1, 2, 3)")


    # 引数を解析
    args = parser.parse_args()
    
    # コマンドに応じて関数を呼び出す
    if args.action == "click_active_spot":
        click_active_spot()
    elif args.action == "check_my_cards":
        check_my_cards()
    elif args.action == "ready_to_play":
        ready_to_play()
    elif args.action == "finish_my_turn":
        finish_my_turn()
    elif args.action == "take_pokemon_active_spot":
        take_pokemon_active_spot()
    elif args.action == "take_pokemon_bench":
        take_pokemon_bench(args.spot)
    elif args.action == "attach_energy":
        attach_energy(args.pokemon_spot)
    elif args.action == "use_item":
        use_item()
    elif args.action == "use_ability":
        use_ability(args.pokemon_spot)
    elif args.action == "use_supporter":
        use_supporter()
    elif args.action == "use_attack":
        use_attack(args.index, args.attacks)
    elif args.action == "retreat":
        retreat()
    elif args.action == "evolve_pokemon":
        evolve_pokemon(args.spot)
    else:
        print("Invalid action. Use -h for help.")

def long_press(x, y, duration=2):
    """
    指定した座標 (x, y) で長押し操作を行う
    x, y: 長押しする座標
    duration: 長押しする時間（秒）
    """
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()  # 押し続ける
    time.sleep(duration)   # 指定した時間だけ押し続ける
    pyautogui.mouseUp()    # 指を離す

def drag_and_drop(start_x, start_y, end_x, end_y, waypoints=None, duration=0.5):
    """
    指定した開始座標 (start_x, start_y) から終了座標 (end_x, end_y) へドラッグアンドドロップ操作を行う
    waypoints: 中間地点のリスト [(x1, y1), (x2, y2), ...] で指定
    duration: ドラッグにかける時間（秒）
    """
    if waypoints is None:
        waypoints = []

    # 開始位置に移動してドラッグを開始
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()  # ドラッグを開始

    # 中間地点を順番に移動
    for waypoint in waypoints:
        pyautogui.moveTo(waypoint[0], waypoint[1], duration=duration / (len(waypoints) + 1))

    # 終了位置に移動
    pyautogui.moveTo(end_x, end_y, duration=duration / (len(waypoints) + 1))
    pyautogui.mouseUp()  # ドラッグを終了


def click(x, y, clicks=1, interval=0.0):
    """
    指定した座標 (x, y) でクリック操作を行う
    x, y: クリックする座標
    clicks: クリック回数（デフォルトは1）
    interval: クリック間の間隔（秒）
    """
    pyautogui.click(x=x, y=y, clicks=clicks, interval=interval)

if __name__ == "__main__":
    main()
