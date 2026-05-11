import subprocess
import socket
import time

def execute_ability():
    """
    HABILIDAD 015: net_status.py
    Objetivo: Verificar conexión a internet y obtener identidad de red local.
    """
    try:
        # 1. Obtener IP Local
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        
        # 2. Probar Ping a Google (DNS universal)
        # -n 1 es para enviar solo un paquete en Windows
        ping_check = subprocess.run(
            ["ping", "-n", "1", "8.8.8.8"], 
            capture_output=True, 
            text=True
        )
        
        has_internet = ping_check.returncode == 0
        
        return {
            "status": "SUCCESS",
            "online": has_internet,
            "local_ip": local_ip,
            "hostname": hostname,
            "timestamp": time.time()
        }
    except Exception as e:
        return {
            "status": "FAILED",
            "error": str(e)
        }

# --- MINI-TEST ATÓMICO ---
if __name__ == "__main__":
    print("--- INICIANDO TEST: NET_STATUS ---")
    print("Verificando identidad y conexión...")
    
    resultado = execute_ability()
    
    if resultado["status"] == "SUCCESS":
        estado = "CONECTADO ✅" if resultado["online"] else "OFFLINE ❌"
        print(f"Estado: {estado}")
        print(f"IP Local: {resultado['local_ip']}")
    else:
        print(f"Error de diagnóstico: {resultado['error']}")