import pyautogui
import time
import ctypes

# Aseguramos el fix del 125% también aquí
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

def execute_ability():
    """
    HABILIDAD 010: mouse_right_click.py
    Objetivo: Acceder a menús contextuales y opciones de gestión.
    """
    try:
        # Registramos posición para el log de aprendizaje
        pos = pyautogui.position()
        
        # Ejecución del clic derecho
        pyautogui.rightClick()
        
        return {
            "status": "SUCCESS",
            "action": "RIGHT_CLICK",
            "coords": pos,
            "timestamp": time.time()
        }
    except Exception as e:
        return {
            "status": "FAILED",
            "error": str(e)
        }

# --- MINI-TEST ATÓMICO ---
if __name__ == "__main__":
    print("--- INICIANDO TEST: MOUSE_RIGHT_CLICK ---")
    print("Pon el mouse sobre el escritorio o un archivo...")
    print("El clic derecho se ejecutará en 3 segundos...")
    time.sleep(3)
    
    resultado = execute_ability()
    print(resultado)