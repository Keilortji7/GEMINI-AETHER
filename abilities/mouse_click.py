import pyautogui
import ctypes
import time

ctypes.windll.shcore.SetProcessDpiAwareness(1)

def execute_ability(button='left'):
    """
    HABILIDAD 002: mouse_click.py
    Objetivo: Ejecutar presión y liberación de un botón del mouse sin traslación[cite: 7].
    """
    try:
        # Registramos posición antes del clic para asegurar que no hubo "drift" (deslizamiento)
        pos_before = pyautogui.position()
        
        # Ejecución del clic[cite: 7]
        pyautogui.click(button=button)
        
        pos_after = pyautogui.position()
        
        return {
            "status": "SUCCESS",
            "button_used": button,
            "position": pos_before,
            "drift_detected": pos_before != pos_after
        }
    except Exception as e:
        return {
            "status": "FAILED",
            "error": str(e)
        }

# --- MINI-TEST ATÓMICO ---
if __name__ == "__main__":
    print("--- INICIANDO TEST: MOUSE_CLICK ---")
    print("Tienes 3 segundos para poner el mouse sobre algo 'cliqueable' (como el botón de inicio)...")
    time.sleep(3)
    
    resultado = execute_ability()
    
    if resultado["status"] == "SUCCESS":
        print(f"TEST PASADO: Clic {resultado['button_used']} ejecutado en {resultado['position']}")
        if resultado["drift_detected"]:
            print("AVISO: Se detectó movimiento durante el clic.")
    else:
        print(f"TEST FALLIDO: {resultado['error']}")