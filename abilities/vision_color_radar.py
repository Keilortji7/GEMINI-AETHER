import pyautogui
import sys

def execute_ability(target_hex, tolerance=20, region=None):
    """
    HABILIDAD 053: vision_color_radar.py
    Busca un color con un margen de error (tolerancia) para evitar fallos por brillo o suavizado.
    """
    try:
        # Convertir HEX a RGB objetivo
        t_r, t_g, t_b = tuple(int(target_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        
        sc = pyautogui.screenshot(region=region)
        w, h = sc.size
        
        # Escaneo optimizado
        for x in range(0, w, 10):
            for y in range(0, h, 10):
                p_r, p_g, p_b = sc.getpixel((x, y))
                
                # Verificar si el píxel está dentro del rango de tolerancia
                if (abs(p_r - t_r) <= tolerance and 
                    abs(p_g - t_g) <= tolerance and 
                    abs(p_b - t_b) <= tolerance):
                    
                    final_x = x + (region[0] if region else 0)
                    final_y = y + (region[1] if region else 0)
                    return {
                        "status": "SUCCESS", 
                        "found_at": (final_x, final_y), 
                        "color_detected": '#%02x%02x%02x' % (p_r, p_g, p_b)
                    }
        
        return {"status": "NOT_FOUND", "searched_color": target_hex}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST INTERNO 053: RADAR COLOR (ROBUSTO) ---")
    
    # Capturamos el color actual bajo el mouse
    x, y = pyautogui.position()
    r, g, b = pyautogui.pixel(x, y)
    current_hex = '#%02x%02x%02x' % (r, g, b)
    
    print(f"Buscando color similar a {current_hex} (Tolerancia: 20)...")
    # Ejecutamos con tolerancia para asegurar el SUCCESS
    print(execute_ability(current_hex, tolerance=20))