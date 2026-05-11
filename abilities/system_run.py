import subprocess
import time

def execute_ability(command):
    """
    HABILIDAD 014: system_run.py
    Objetivo: Ejecutar aplicaciones o comandos de sistema directamente.
    """
    try:
        # shell=True permite usar comandos como 'start' o 'dir'
        # subprocess.Popen no bloquea el código mientras la app está abierta
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        return {
            "status": "SUCCESS",
            "command_sent": command,
            "message": "Comando enviado al sistema."
        }
    except Exception as e:
        return {
            "status": "FAILED",
            "error": str(e)
        }

# --- MINI-TEST ATÓMICO ---
if __name__ == "__main__":
    print("--- INICIANDO TEST: SYSTEM_RUN ---")
    print("Intentando abrir el Calculadora en 2 segundos...")
    time.sleep(2)
    
    # 'calc' es el comando universal en Windows para la calculadora
    resultado = execute_ability("calc")
    print(resultado)