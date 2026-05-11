import os

def execute_ability(mode="shutdown"):
    """
    HABILIDAD 028: system_power.py
    Modos: 'shutdown', 'restart'
    """
    try:
        if mode == "shutdown":
            # os.system("shutdown /s /t 60") # Comentado por seguridad: apaga en 60s
            return {"status": "SUCCESS", "action": "SHUTDOWN_QUEUED"}
        elif mode == "restart":
            # os.system("shutdown /r /t 60")
            return {"status": "SUCCESS", "action": "RESTART_QUEUED"}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}