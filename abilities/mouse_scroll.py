import pyautogui
import time

def execute_ability(clicks):
    """
    HABILIDAD 006: mouse_scroll.py
    Objetivo: Navegación vertical (positivo para arriba, negativo para abajo).
    """
    try:
        # Registramos la acción
        pyautogui.scroll(clicks)
        
        return {
            "status": "SUCCESS",
            "scroll_amount": clicks,
            "direction": "UP" if clicks > 0 else "DOWN"
        }
    except Exception as e:
        return {
            "status": "FAILED",
            "error": str(e)
        }

# --- MINI-TEST ATÓMICO ---
if __name__ == "__main__":
    print("--- INICIANDO TEST: MOUSE_SCROLL ---")
    print("Pon el mouse sobre una ventana con scroll (como el navegador)...")
    time.sleep(3)
    
    # -500 suele ser un 'empujón' visible hacia abajo
    resultado = execute_ability(-500)
    
    if resultado["status"] == "SUCCESS":
        print(f"TEST PASADO: Scroll hacia {resultado['direction']} ejecutado.")
    else:
        print(f"TEST FALLIDO: {resultado['error']}")