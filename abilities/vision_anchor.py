import pyautogui
import os
import time

def execute_ability(region_size=100):
    """
    HABILIDAD 003: vision_anchor.py
    Objetivo: Capturar el área inmediata alrededor del cursor para verificar cambios visuales.
    """
    try:
        # Creamos carpeta de capturas si no existe
        save_path = "logs/vision_temp/"
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # Obtenemos la posición actual para centrar la "foto"
        x, y = pyautogui.position()
        
        # Calculamos el cuadrado de visión (el ancla)
        left = x - (region_size // 2)
        top = y - (region_size // 2)
        
        timestamp = int(time.time())
        filename = f"anchor_{timestamp}.png"
        full_path = os.path.join(save_path, filename)
        
        # Captura de pantalla de la región específica
        screenshot = pyautogui.screenshot(region=(left, top, region_size, region_size))
        screenshot.save(full_path)
        
        return {
            "status": "SUCCESS",
            "file_saved": full_path,
            "coordinates": (x, y),
            "region_size": region_size
        }
    except Exception as e:
        return {
            "status": "FAILED",
            "error": str(e)
        }

# --- MINI-TEST ATÓMICO ---
if __name__ == "__main__":
    print("--- INICIANDO TEST: VISION_ANCHOR ---")
    print("Capturando lo que hay bajo tu mouse en 2 segundos...")
    time.sleep(2)
    
    resultado = execute_ability()
    
    if resultado["status"] == "SUCCESS":
        print(f"TEST PASADO: 'Ojo' activado. Captura guardada en: {resultado['file_saved']}")
        print(f"La IA ahora 've' el punto {resultado['coordinates']}")
    else:
        print(f"TEST FALLIDO: {resultado['error']}")