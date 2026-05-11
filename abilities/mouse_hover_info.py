import pyautogui
import time
from PIL import ImageChops

def execute_ability(x, y):
    """
    Objetivo: Hover y detección de cambio visual (aparición de tooltip).
    """
    try:
        before = pyautogui.screenshot(region=(x, y-50, 200, 50))
        pyautogui.moveTo(x, y)
        time.sleep(1.5) # Tiempo para que aparezca el tooltip
        after = pyautogui.screenshot(region=(x, y-50, 200, 50))
        
        diff = ImageChops.difference(before, after)
        return {"status": "SUCCESS", "info_appeared": diff.getbbox() is not None}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST 051: HOVER TOOLTIP ---")
    # Pon el mouse sobre algún icono de la barra de tareas antes de que pasen los 2 seg
    time.sleep(2)
    curr_x, curr_y = pyautogui.position()
    print(execute_ability(curr_x, curr_y))