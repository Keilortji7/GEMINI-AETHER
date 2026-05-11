import pyautogui
import time
import sys

def execute_ability(x, y, duration=0.5):
    try:
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown()
        time.sleep(duration)
        pyautogui.mouseUp()
        return {"status": "SUCCESS", "hold_duration": duration}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST INTERNO 050: CLIC SOSTENIDO ---")
    # Prueba un clic de 1 segundo en la posición actual
    curr_x, curr_y = pyautogui.position()
    print(execute_ability(curr_x, curr_y, 1.0))