from PIL import ImageChops
import pyautogui
import time

def execute_ability():
    try:
        s1 = pyautogui.screenshot()
        time.sleep(1)
        s2 = pyautogui.screenshot()
        diff = ImageChops.difference(s1, s2)
        return {"status": "SUCCESS", "frozen": diff.getbbox() is None}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST INTERNO 054: FREEZE CHECK ---")
    print("No movás nada por 1 segundo...")
    print(execute_ability())