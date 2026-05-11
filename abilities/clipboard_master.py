import pyperclip
import time

def execute_ability(text=None, mode="WRITE"):
    """
    HABILIDAD 018: clipboard_master.py
    Objetivo: Intercambio de datos rápido entre apps (Copiar/Pegar).
    """
    try:
        if mode == "WRITE" and text:
            pyperclip.copy(text)
            return {"status": "SUCCESS", "action": "TEXT_COPIED", "length": len(text)}
        
        elif mode == "READ":
            content = pyperclip.paste()
            return {"status": "SUCCESS", "action": "TEXT_READ", "content": content}
            
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

# --- MINI-TEST ATÓMICO ---
if __name__ == "__main__":
    print("--- TEST: CLIPBOARD_MASTER ---")
    # Probamos escribir
    execute_ability("AETHER_CORE_v1.0", mode="WRITE")
    print("1. Texto 'AETHER_CORE_v1.0' copiado al portapapeles.")
    
    # Probamos leer
    lectura = execute_ability(mode="READ")
    print(f"2. La IA leyó del portapapeles: {lectura['content']}")