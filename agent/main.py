import time
import pyautogui
import pytesseract
from PIL import Image, ImageFilter
import numpy as np
import cv2

from agent.domains.battle import Battle


def main():
    # スクリーンショットを撮影
    screenshot = capture_screen().convert("RGB")
    init_text_screenshot = extract_and_process_region_for_text(screenshot, 0, 235, 430, 265)
    init_text = recognize_text(init_text_screenshot, 'init_text.png')
    print(f"Recognized text: {init_text}")

    # 対戦相手が見つかった場合、Battleインスタンスを作成
    if "対戦相手が見つかりました" in init_text:
        print("Battle found! Initializing battle...")
        battle = Battle()
        print(battle)  # Battleインスタンスの初期状態を確認
    else:
        print("Waiting for opponent...")

def capture_screen(region=(1500, 50, 430, 1000)):
    """
    指定した領域のスクリーンショットを取得
    region: (x, y, width, height) - スクリーンショットを取得する領域の指定
    """
    # 画面の一部をスクリーンショットとして取得
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save("app_screenshot.png")
    return screenshot

def extract_and_process_region_for_text(screenshot, left, top, right, bottom):
    # 指定された領域を切り出す
    region = screenshot.crop((left, top, right, bottom))

    # 色フィルタを適用して黒文字以外を白色に
    region_np = np.array(region)
    lower_bound = np.array([0, 0, 0])  # 黒色の下限 (R, G, B)
    upper_bound = np.array([200, 200, 200])  # 黒色の上限 (R, G, B)
    mask = cv2.inRange(region_np, lower_bound, upper_bound)
    filtered_region_np = cv2.bitwise_and(region_np, region_np, mask=mask)
    filtered_region_np[mask == 0] = [255, 255, 255]  # 黒文字以外を白色にする
    filtered_region = Image.fromarray(filtered_region_np)

    # シャープネスを軽く強調
    sharpened_region = filtered_region.filter(ImageFilter.UnsharpMask(radius=2, percent=150))

    return sharpened_region

def recognize_text(image, save_path, psm=8):
    # 画像を保存（確認用）
    image.save(save_path)

    white_list = "対戦相手を探していますが見つかりた！"
    custom_config = f'-c tessedit_char_whitelist={white_list} --oem 3 --psm {psm}'
    text = pytesseract.image_to_string(image, lang="jpn", config=custom_config)
    return text.strip()

if __name__ == "__main__":
    main()
