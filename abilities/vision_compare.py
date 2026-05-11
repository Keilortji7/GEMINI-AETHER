from PIL import Image, ImageChops
import os

def execute_ability(img_path_a, img_path_b):
    """
    HABILIDAD 008: vision_compare.py
    Objetivo: Determinar si una acción causó un efecto visual en la pantalla.
    """
    try:
        if not os.path.exists(img_path_a) or not os.path.exists(img_path_b):
            return {"status": "FAILED", "error": "Uno de los archivos no existe."}

        img_a = Image.open(img_path_a).convert("RGB")
        img_b = Image.open(img_path_b).convert("RGB")

        # Calculamos la diferencia absoluta entre imágenes
        diff = ImageChops.difference(img_a, img_b)
        
        # Si no hay diferencia, bbox será None
        bbox = diff.getbbox()

        return {
            "status": "SUCCESS",
            "changed": bbox is not None,
            "diff_area": bbox if bbox else (0,0,0,0),
            "message": "Cambio detectado" if bbox else "Sin cambios visuales"
        }
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

# --- MINI-TEST ATÓMICO ---
if __name__ == "__main__":
    print("--- INICIANDO TEST: VISION_COMPARE ---")
    print("Este test requiere dos capturas previas en logs/vision_temp/...")
    # Este test es manual: debes pasarle rutas de archivos reales que existan
    # resultado = execute_ability("ruta/a/foto1.png", "ruta/a/foto2.png")
    print("Neurona lista para comparar. Esperando integración con el Kernel.")

    # ... (aquí va tu función execute_ability)

if __name__ == "__main__":
    from PIL import Image
    import os

    print("--- INICIANDO TEST ATÓMICO: VISION_COMPARE ---")
    
    # 1. Creamos dos imágenes de prueba rápidas
    img1_path = "logs/vision_temp/test_a.png"
    img2_path = "logs/vision_temp/test_b.png"
    
    if not os.path.exists("logs/vision_temp/"):
        os.makedirs("logs/vision_temp/")

    # Imagen A: Un cuadro rojo
    Image.new('RGB', (100, 100), color='red').save(img1_path)
    # Imagen B: Un cuadro azul
    Image.new('RGB', (100, 100), color='blue').save(img2_path)

    # 2. Ejecutamos la comparación
    resultado = execute_ability(img1_path, img2_path)
    
    if resultado["status"] == "SUCCESS" and resultado["changed"]:
        print("✅ TEST PASADO: La neurona detectó que las imágenes son diferentes.")
    else:
        print(f"❌ TEST FALLIDO: {resultado.get('error', 'No detectó cambios')}")