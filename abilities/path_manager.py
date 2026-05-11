import os

def execute_ability(folder_name):
    """
    HABILIDAD 023: path_manager.py
    Objetivo: Crear y validar rutas de almacenamiento para el agente.
    """
    try:
        # Creamos una carpeta dentro de 'workspace'
        base_path = "workspace"
        target_path = os.path.join(base_path, folder_name)
        
        if not os.path.exists(target_path):
            os.makedirs(target_path)
            
        return {
            "status": "SUCCESS",
            "full_path": os.path.abspath(target_path),
            "created": True
        }
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST 023: PATH_MANAGER ---")
    print(execute_ability("reportes_mensuales"))