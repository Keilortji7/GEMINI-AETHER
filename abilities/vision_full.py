import pyautogui
import os
import time

def execute_ability():
    """
    HABILIDAD 007: vision_full.py
    Objetivo: Capturar la totalidad del escritorio para análisis de contexto global.
    """
    try:
        save_path = "logs/vision_temp/"
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        timestamp = int(time.time())
        filename = f"full_env_{timestamp}.png"
        full_path = os.path.join(save_path, filename)
        
        # Captura de pantalla completa
        screenshot = pyautogui.screenshot()
        screenshot.save(full_path)
        
        return {
            "status": "SUCCESS",
            "file_saved": full_path,
            "resolution": screenshot.size,
            "timestamp": timestamp
        }
    except Exception as e:
        return {
            "status": "FAILED",
            "error": str(e)
        }

# --- MINI-TEST ATÓMICO ---
if __name__ == "__main__":
    print("--- INICIANDO TEST: VISION_FULL ---")
    print("Capturando el escritorio completo en 2 segundos...")
    time.sleep(2)
    
    resultado = execute_ability()
    
    if resultado["status"] == "SUCCESS":
        print(f"TEST PASADO: Visión global activada.")
        print(f"Resolución detectada: {resultado['resolution']}")
        print(f"Archivo: {resultado['file_saved']}")
    else:
        print(f"TEST FALLIDO: {resultado['error']}")