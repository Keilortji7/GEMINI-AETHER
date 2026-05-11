import psutil
import time

def execute_ability():
    """
    HABILIDAD 017: system_stats.py
    Objetivo: Conciencia del estado del hardware (CPU, RAM, Batería).
    """
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        battery = psutil.sensors_battery()
        
        return {
            "status": "SUCCESS",
            "cpu_percent": cpu_usage,
            "ram_percent": ram.percent,
            "battery_percent": battery.percent if battery else "N/A",
            "power_plugged": battery.power_plugged if battery else "N/A"
        }
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST: SYSTEM_STATS ---")
    print("Analizando salud del sistema...")
    print(execute_ability())