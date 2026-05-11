import os

def execute_ability(log_path="logs/agent_memory/history.log"):
    """
    HABILIDAD 047: log_error_parser.py
    """
    try:
        if not os.path.exists(log_path):
            return {"status": "FAILED", "error": "No hay historial aún."}
        
        with open(log_path, 'r', encoding='utf-8') as f:
            content = f.read()
            errors = content.count("[FAILED]")
            success = content.count("[SUCCESS]")
            
        return {"status": "SUCCESS", "errors_found": errors, "success_found": success}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}