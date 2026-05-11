import pyautogui
from PIL import Image, ImageChops # <--- Aquí faltaba el 'Image'

def execute_ability(template_path, region):
    """
    Objetivo: Saber si un icono cambió de estado (ON/OFF) comparando píxeles.
    """
    try:
        # Captura el área actual
        current = pyautogui.screenshot(region=region)
        # Carga la imagen de referencia
        template = Image.open(template_path)
        
        # Calcula la diferencia
        diff = ImageChops.difference(current, template)
        
        # Si no hay diferencia (bbox es None), es un match perfecto
        return {"status": "SUCCESS", "match": diff.getbbox() is None}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST 052: BIT COMPARE ---")
    # Para probarlo ocupás un screenshot previo guardado como 'template.png'
    # print(execute_ability("template.png", (0, 0, 100, 100)))