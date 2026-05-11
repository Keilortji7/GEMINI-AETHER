import pyautogui
import time
import ctypes

# Mantenemos la consistencia con el escalado y permisos
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

def execute_ability(*args):
    """
    HABILIDAD 011: keyboard_hotkey.py
    Objetivo: Ejecutar combinaciones de teclas simultáneas.
    Uso: execute_ability('ctrl', 'c')
    """
    try:
        pyautogui.hotkey(*args)
        
        return {
            "status": "SUCCESS",
            "keys_used": args,
            "timestamp": time.time()
        }
    except Exception as e:
        return {
            "status": "FAILED",
            "error": str(e)
        }

# --- MINI-TEST ATÓMICO ---
if __name__ == "__main__":
    print("--- INICIANDO TEST: KEYBOARD_HOTKEY ---")
    print("En 3 segundos se minimizarán todas las ventanas (Win+D)...")
    time.sleep(3)
    
    # Probamos el combo para mostrar el escritorio
    resultado = execute_ability('win', 'd')
    
    if resultado["status"] == "SUCCESS":
        print(f"TEST PASADO: Combo {resultado['keys_used']} ejecutado.")
    else:
        print(f"TEST FALLIDO: {resultado['error']}")