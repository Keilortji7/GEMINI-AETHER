import time

def execute_ability(seconds):
    """
    HABILIDAD 026: system_wait.py
    Objetivo: Pausar la ejecución para sincronizarse con procesos externos.
    """
    try:
        time.sleep(seconds)
        return {"status": "SUCCESS", "waited": seconds}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}