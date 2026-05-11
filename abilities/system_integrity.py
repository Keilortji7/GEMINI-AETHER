import os

def execute_ability():
    """
    HABILIDAD 050: system_integrity.py
    Objetivo: Asegurar que el entorno de AETHER esté sano.
    """
    folders = ["abilities", "logs", "workspace", "logs/vision_temp", "logs/agent_memory"]
    created = []
    
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            created.append(folder)
            
    return {
        "status": "SUCCESS", 
        "integrity_ok": True, 
        "folders_created": created,
        "message": "Sistema listo para operar."
    }