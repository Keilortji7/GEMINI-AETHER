import pyautogui
import pytesseract
import sys

# --- ESTA LÍNEA ES LA CLAVE ---
# Cambiá la ruta por la carpeta donde instalaste Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def execute_ability():
    """
    HABILIDAD 054: vision_text_block_detect.py
    Objetivo: Devolver coordenadas de áreas densas en texto.
    """
    try:
        screenshot = pyautogui.screenshot()
        # image_to_data nos da las cajas (coordenadas) de cada palabra
        data = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)
        
        blocks = []
        for i in range(len(data['text'])):
            # Solo guardamos lo que tenga texto real y confianza > 70%
            if data['text'][i].strip() and int(data['conf'][i]) > 70:
                blocks.append({
                    'x': data['left'][i], 
                    'y': data['top'][i], 
                    'w': data['width'][i], 
                    'h': data['height'][i],
                    'text': data['text'][i]
                })
        
        return {"status": "SUCCESS", "found_blocks": len(blocks), "sample": blocks[:2]}
    except Exception as e:
        # Aquí es donde te salió el error de "not in PATH"
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST INTERNO 054: TEXT BLOCK LOCATOR ---")
    print(execute_ability())