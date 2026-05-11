import pyautogui
import pyperclip
import time

def execute_ability(text):
    try:
        pyperclip.copy(text)
        time.sleep(0.2)
        pyautogui.hotkey('ctrl', 'v')
        return {"status": "SUCCESS", "chars": len(text)}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST INTERNO 052: SMART PASTE ---")
    print(execute_ability("Test de inyección AETHER con tildes: Árbol, Ñandú."))