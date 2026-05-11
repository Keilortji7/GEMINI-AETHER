import pyautogui
import cv2
import numpy as np

def execute_ability():
    """
    Objetivo: Detectar contornos rectangulares (ventanas) en pantalla.
    """
    try:
        screenshot = pyautogui.screenshot()
        img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 50, 150)
        
        contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        rects = [cv2.boundingRect(c) for c in contours if cv2.contourArea(c) > 5000]
        
        return {"status": "SUCCESS", "windows_detected": len(rects), "main_rect": rects[0] if rects else None}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST 050: UI DETECTION ---")
    print(execute_ability())