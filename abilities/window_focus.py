import pygetwindow as gw
import time
import ctypes

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

def execute_ability(window_title):
    """
    HABILIDAD 012: window_focus.py
    Objetivo: Localizar y traer al frente una ventana específica por su título.
    """
    try:
        # Buscamos ventanas que contengan el texto (case-insensitive)
        windows = gw.getWindowsWithTitle(window_title)
        
        if not windows:
            return {"status": "FAILED", "error": f"No se encontró: {window_title}"}
        
        target = windows[0]
        
        # Si está minimizada, la restauramos
        if target.isMinimized:
            target.restore()
        
        # La traemos al frente
        target.activate()
        
        return {
            "status": "SUCCESS",
            "window_found": target.title,
            "size": (target.width, target.height),
            "position": (target.left, target.top)
        }
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

# --- MINI-TEST ATÓMICO ---
if __name__ == "__main__":
    print("--- INICIANDO TEST: WINDOW_FOCUS ---")
    print("Asegúrate de tener el Bloc de notas o Chrome abierto...")
    nombre = input("¿Qué ventana quieres buscar? (ej: Notepad): ")
    
    resultado = execute_ability(nombre)
    
    if resultado["status"] == "SUCCESS":
        print(f"✅ ¡ENCONTRADA! La ventana '{resultado['window_found']}' está ahora al frente.")
    else:
        print(f"❌ ERROR: {resultado['error']}")