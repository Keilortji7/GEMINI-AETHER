import psutil

class AetherSensors:
    def __init__(self):
        # Umbrales técnicos de estabilidad
        self.cpu_limit = 85.0
        self.ram_limit = 90.0
        # Lista de procesos que activan el estado de CARGA ALTA inmediatamente
        self.heavy_processes = ["Valorant.exe", "GenshinImpact.exe", "vlc.exe"]

    def get_hardware_status(self):
        """Devuelve un diccionario con la carga actual del sistema."""
        cpu_usage = psutil.cpu_percent(interval=0.1)
        ram_usage = psutil.virtual_memory().percent
        
        return {
            "cpu_percent": cpu_usage,
            "ram_percent": ram_usage,
            "is_overloaded": cpu_usage > self.cpu_limit or ram_usage > self.ram_limit
        }

    def check_heavy_software(self):
        """Busca si hay juegos o software pesado activo."""
        for proc in psutil.process_iter(['name']):
            try:
                if proc.info['name'] in self.heavy_processes:
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return False

    def get_system_event(self):
        """Consolida los datos en un evento legible para el Kernel."""
        hw = self.get_hardware_status()
        is_heavy = self.check_heavy_software()
        
        if hw["is_overloaded"] or is_heavy:
            return "EVENT_CRITICAL_LOAD"
        return "EVENT_NONE"