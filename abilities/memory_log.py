import datetime
import os

def execute_ability(message, category="INFO"):
    """
    HABILIDAD 019: memory_log.py
    Objetivo: Registro de eventos para auditoría y persistencia.
    """
    try:
        log_dir = "logs/agent_memory"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{category}] {message}\n"
        
        with open(f"{log_dir}/history.log", "a", encoding="utf-8") as f:
            f.write(log_entry)
            
        return {"status": "SUCCESS", "logged": True}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST: MEMORY_LOG ---")
    print(execute_ability("Habilidad 019 activada exitosamente.", category="SYSTEM"))