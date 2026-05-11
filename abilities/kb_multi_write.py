import pyautogui

def execute_ability(lines):
    try:
        for line in lines:
            pyautogui.write(line)
            pyautogui.press('enter')
        return {"status": "SUCCESS", "lines_written": len(lines)}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST INTERNO 055: MULTI WRITE ---")
    test_lines = ["Línea 1: Setup", "Línea 2: Procesando...", "Línea 3: Fin."]
    print(execute_ability(test_lines))