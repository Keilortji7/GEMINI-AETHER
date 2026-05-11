import os
import time

def execute_ability(path="."):
    """
    HABILIDAD 013: file_list.py
    Objetivo: Listar archivos para que la IA sepa qué puede manipular en una carpeta.
    """
    try:
        files = os.listdir(path)
        
        # Filtramos para no saturar a la IA con carpetas ocultas
        visible_files = [f for f in files if not f.startswith('.')]
        
        return {
            "status": "SUCCESS",
            "path": os.path.abspath(path),
            "count": len(visible_files),
            "files": visible_files[:20] # Solo los primeros 20 para no explotar el log
        }
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST: FILE_LIST ---")
    # Listamos la carpeta de habilidades para ver si estamos todos
    print(execute_ability("./abilities"))