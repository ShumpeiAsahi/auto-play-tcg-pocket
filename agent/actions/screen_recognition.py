import pyautogui
import pytesseract
from PIL import Image, ImageFilter, ImageOps
import numpy as np
import cv2

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

        # 色フィルタを適用して白文字を抽出して背景を黒に
    region_np = np.array(region)
    lower_bound = np.array([200, 200, 200])  # 明るい色の下限 (R, G, B)
    upper_bound = np.array([255, 255, 255])  # 明るい色の上限 (R, G, B)
    mask = cv2.inRange(region_np, lower_bound, upper_bound)
    filtered_region_np = cv2.bitwise_and(region_np, region_np, mask=mask)
    filtered_region_np[mask == 0] = [0, 0, 0]  # 背景を黒色にする
    filtered_region = Image.fromarray(filtered_region_np)

    # 反転して白背景黒文字にする
    inverted_region = ImageOps.invert(filtered_region)

    # シャープネスを軽く強調
    sharpened_region = inverted_region.filter(ImageFilter.UnsharpMask(radius=2, percent=150))

    return sharpened_region

def recognize_text(image, save_path, psm=8):
    # 画像を保存（確認用）
    image.save(save_path)

    white_list = "先後攻"
    custom_config = f'-c tessedit_char_whitelist={white_list} --oem 3 --psm {psm}'
    text = pytesseract.image_to_string(image, lang="jpn", config=custom_config)
    return text.strip()

