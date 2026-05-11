from datetime import datetime

def execute_ability():
    """
    HABILIDAD 027: time_stats.py
    """
    now = datetime.now()
    return {
        "status": "SUCCESS",
        "time": now.strftime("%H:%M:%S"),
        "date": now.strftime("%Y-%m-%d"),
        "weekday": now.strftime("%A"),
        "timestamp": now.timestamp()
    }