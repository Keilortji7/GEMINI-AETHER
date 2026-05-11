import pyautogui
import time

def execute_ability(text, interval=0.1):
    """
    HABILIDAD 005: keyboard_write.py
    Objetivo: Aprender a ingresar secuencias de caracteres con ritmo humano.
    """
    try:
        # El intervalo simula la velocidad de escritura para evitar bloqueos de seguridad
        pyautogui.write(text, interval=interval)
        
        return {
            "status": "SUCCESS",
            "chars_written": len(text),
            "text_sample": text[:10] + "..." if len(text) > 10 else text
        }
    except Exception as e:
        return {
            "status": "FAILED",
            "error": str(e)
        }

# --- MINI-TEST ATÓMICO ---
if __name__ == "__main__":
    print("--- INICIANDO TEST: KEYBOARD_WRITE ---")
    print("En 3 segundos, la IA escribirá 'AETHER ONLINE'...")
    time.sleep(3)
    
    # Si tienes el Bloc de notas abierto o el chat, verás la magia
    resultado = execute_ability("AETHER ONLINE", interval=0.2) # Más lento
    
    if resultado["status"] == "SUCCESS":
        print(f"TEST PASADO: Se escribieron {resultado['chars_written']} caracteres.")
    else:
        print(f"TEST FALLIDO: {resultado['error']}")