import pyautogui
import random
import numpy as np
from scipy import interpolate

def execute_ability(target_x, target_y):
    try:
        start_x, start_y = pyautogui.position()
        cp_x = [start_x, random.randint(min(start_x, target_x), max(start_x, target_x)), target_x]
        cp_y = [start_y, random.randint(min(start_y, target_y), max(start_y, target_y)), target_y]
        t = np.linspace(0, 1, 15)
        tck, u = interpolate.splprep([cp_x, cp_y], k=2, s=0)
        out = interpolate.splev(t, tck)
        for x, y in zip(out[0], out[1]):
            pyautogui.moveTo(x, y)
        return {"status": "SUCCESS"}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST INTERNO 051: CURVA HUMANA ---")
    print(execute_ability(800, 600))