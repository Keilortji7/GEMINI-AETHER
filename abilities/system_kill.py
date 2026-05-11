import psutil
import time

def execute_ability(process_name):
    """
    HABILIDAD 016: system_kill.py
    Objetivo: Cerrar aplicaciones por nombre de proceso de forma limpia.
    """
    try:
        count = 0
        for proc in psutil.process_iter(['name']):
            # Buscamos coincidencias (ej: 'Calculator.exe' o 'calc.exe')
            if process_name.lower() in proc.info['name'].lower():
                proc.kill()
                count += 1
        
        if count > 0:
            return {
                "status": "SUCCESS",
                "process_terminated": process_name,
                "instances_closed": count
            }
        else:
            return {"status": "FAILED", "error": f"No se encontró el proceso: {process_name}"}
            
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

# --- MINI-TEST ATÓMICO ---
if __name__ == "__main__":
    print("--- INICIANDO TEST: SYSTEM_KILL ---")
    print("Abre la calculadora manualmente...")
    time.sleep(3)
    
    # En Windows 10/11 la calculadora suele llamarse 'CalculatorApp.exe' o 'Calculator.exe'
    # Con poner 'calc' suele bastar para encontrarlo
    resultado = execute_ability("calc")
    print(resultado)