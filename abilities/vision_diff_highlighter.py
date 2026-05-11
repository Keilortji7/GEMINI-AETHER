from PIL import Image, ImageChops, ImageDraw
import os
import time

def execute_ability(img_path_a, img_path_b):
    """
    HABILIDAD 020: vision_diff_highlighter.py
    Objetivo: Generar un mapa visual de cambios para depuración de errores.
    """
    try:
        if not os.path.exists(img_path_a) or not os.path.exists(img_path_b):
            return {"status": "FAILED", "error": "Faltan imágenes de origen."}

        img_a = Image.open(img_path_a).convert("RGB")
        img_b = Image.open(img_path_b).convert("RGB")

        # 1. Encontrar la diferencia
        diff = ImageChops.difference(img_a, img_b)
        
        # 2. Crear una máscara de los cambios
        # Si el píxel cambió más de un umbral (threshold), lo marcamos
        bbox = diff.getbbox()
        
        if bbox:
            # 3. Generar imagen de resaltado (Highlight)
            # Dibujamos un rectángulo rojo sobre la imagen original donde hubo cambio
            highlight = img_b.copy()
            draw = ImageDraw.Draw(highlight)
            draw.rectangle(bbox, outline="red", width=5)
            
            save_path = f"logs/vision_temp/diff_report_{int(time.time())}.png"
            highlight.save(save_path)
            
            return {
                "status": "SUCCESS",
                "changed": True,
                "report_file": save_path,
                "area": bbox
            }
        else:
            return {"status": "SUCCESS", "changed": False, "message": "Imágenes idénticas"}

    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST 020: VISUAL AUDIT ---")
    print("Neurona de auditoría visual cargada. Lista para el Kernel.")