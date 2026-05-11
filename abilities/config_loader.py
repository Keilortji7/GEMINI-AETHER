import json
import os

def execute_ability(file_path="config.json"):
    """
    HABILIDAD 031: config_loader.py
    Objetivo: Leer parámetros externos sin modificar el código fuente.
    """
    try:
        if not os.path.exists(file_path):
            # Creamos uno por defecto si no existe
            default = {"version": "1.0", "user": "AetherUser", "theme": "dark"}
            with open(file_path, 'w') as f:
                json.dump(default, f, indent=4)
            return {"status": "CREATED_DEFAULT", "data": default}
            
        with open(file_path, 'r') as f:
            data = json.load(f)
        return {"status": "SUCCESS", "data": data}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}