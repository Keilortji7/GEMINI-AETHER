import pyautogui
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)


def execute_ability(x, y):
    """
    HABILIDAD 001: mouse_linear.py
    Objetivo: Traslación física del cursor a coordenadas absolutas.
    """
    try:
        # Registro de posición previa para análisis de aprendizaje[cite: 4]
        start_pos = pyautogui.position()
        
        # Movimiento instantáneo
        pyautogui.moveTo(x, y)
        
        end_pos = pyautogui.position()
        
        return {
            "status": "SUCCESS",
            "start": start_pos,
            "end": end_pos,
            "target": (x, y),
            "precision_error": abs(end_pos[0] - x) + abs(end_pos[1] - y)
        }
    except Exception as e:
        return {
            "status": "FAILED",
            "error": str(e)
        }

# --- BLOQUE DE MINI-TEST ---
if __name__ == "__main__":
    print("--- INICIANDO TEST ATÓMICO: MOUSE_LINEAR ---")
    
    # Coordenadas de prueba: Centro de la pantalla aproximadamente
    test_x, test_y = 500, 500
    
    resultado = execute_ability(test_x, test_y)
    
    if resultado["status"] == "SUCCESS":
        print(f"TEST PASADO: El mouse se movió a {resultado['end']}")
        print(f"Error de precisión: {resultado['precision_error']} píxeles")
    else:
        print(f"TEST FALLIDO: {resultado['error']}")