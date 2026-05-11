import pyautogui
import time
import ctypes

# Esto corrige el problema del 125% de escala
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass # Por si no estás en Windows

def execute_ability(x1, y1, x2, y2, duration=1.2):
    """
    HABILIDAD 009: mouse_drag.py corregida para escalado del 125%.
    """
    try:
        # 1. Mover al objeto
        pyautogui.moveTo(x1, y1)
        time.sleep(0.3) # Tiempo de "asentamiento"
        
        # 2. Enganchar (Click y mantener)
        pyautogui.mouseDown(button='left')
        time.sleep(0.4) # Tiempo para que Windows reconozca el drag
        
        # 3. Desplazar
        pyautogui.moveTo(x2, y2, duration=duration)
        
        # 4. Soltar
        time.sleep(0.2)
        pyautogui.mouseUp(button='left')
        
        return {
            "status": "SUCCESS",
            "origin": (x1, y1),
            "destination": (x2, y2),
            "scaling_fix": "DPI_AWARE_ACTIVE"
        }
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST 009: ARRASTRE CON FIX DE ESCALA (125%) ---")
    print("Pon el mouse sobre un icono y espera 3 segundos...")
    time.sleep(3)
    curr_x, curr_y = pyautogui.position()
    # Intenta moverlo 150 píxeles a la derecha
    print(execute_ability(curr_x, curr_y, curr_x + 150, curr_y))