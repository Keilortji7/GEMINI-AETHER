import pyautogui
import time

def execute_ability(key):
    """
    HABILIDAD 004: keyboard_press.py
    Objetivo: Aprender el impacto de una sola tecla en el sistema.
    """
    try:
        # Registro del estado previo (importante para que la IA aprenda)
        pyautogui.press(key)
        
        return {
            "status": "SUCCESS",
            "key_pressed": key,
            "timestamp": time.time()
        }
    except Exception as e:
        return {
            "status": "FAILED",
            "error": str(e)
        }

# --- MINI-TEST ATÓMICO ---
if __name__ == "__main__":
    print("--- INICIANDO TEST: KEYBOARD_PRESS ---")
    print("En 3 segundos se presionará la tecla 'Win' para abrir el menú inicio...")
    time.sleep(3)
    
    # Probamos con la tecla 'win' que es visual y fácil de confirmar
    resultado = execute_ability('win')
    
    if resultado["status"] == "SUCCESS":
        print(f"TEST PASADO: Tecla '{resultado['key_pressed']}' enviada.")
    else:
        print(f"TEST FALLIDO: {resultado['error']}")