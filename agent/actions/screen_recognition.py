import pyautogui
import pytesseract

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

    return region

def recognize_text(image, save_path, psm=8):
    # 画像を保存（確認用）
    image.save(save_path)

    white_list = "先攻後"
    custom_config = f'-c tessedit_char_whitelist={white_list} --oem 3 --psm {psm}'
    text = pytesseract.image_to_string(image, lang="jpn", config=custom_config)
    return text.strip()

