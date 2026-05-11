import pyautogui
import time
from PIL import ImageChops

def execute_ability(timeout=10):
    """
    HABILIDAD 055: system_wait_stable.py
    Objetivo: Esperar a que la pantalla deje de cambiar antes de actuar.
    """
    start = time.time()
    try:
        while time.time() - start < timeout:
            s1 = pyautogui.screenshot()
            time.sleep(0.5)
            s2 = pyautogui.screenshot()
            
            # Si no hay diferencia entre capturas, la pantalla está estable
            if ImageChops.difference(s1, s2).getbbox() is None:
                return {
                    "status": "SUCCESS", 
                    "stable_after": round(time.time()-start, 2),
                    "msg": "Pantalla lista para interactuar"
                }
        return {"status": "TIMEOUT", "msg": "La pantalla sigue en movimiento"}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST INTERNO 055: SYSTEM STABLE CHECK ---")
    print("No movás nada por un momento...")
    print(execute_ability())