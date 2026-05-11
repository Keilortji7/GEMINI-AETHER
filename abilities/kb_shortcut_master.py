import pyautogui

def execute_ability(action_name):
    """
    Objetivo: Ejecutar navegación de sistema por teclado.
    """
    shortcuts = {
        "switch_app": ("alt", "tab"),
        "show_desktop": ("win", "d"),
        "close_window": ("alt", "f4"),
        "search": ("win", "s")
    }
    try:
        keys = shortcuts.get(action_name)
        if keys:
            pyautogui.hotkey(*keys)
            return {"status": "SUCCESS", "executed": action_name}
        return {"status": "NOT_FOUND"}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST 053: SHORTCUT MASTER ---")
    print(execute_ability("switch_app"))