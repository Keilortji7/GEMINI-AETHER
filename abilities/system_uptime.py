import psutil
import datetime

def execute_ability():
    """
    HABILIDAD 040: system_uptime.py
    """
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.datetime.fromtimestamp(boot_time_timestamp)
    uptime = datetime.datetime.now() - bt
    
    return {
        "status": "SUCCESS",
        "boot_time": bt.strftime("%Y-%m-%d %H:%M:%S"),
        "uptime_hours": round(uptime.total_seconds() / 3600, 2)
    }