import pygetwindow as gw

def execute_ability():
    """
    HABILIDAD 030: web_metadata.py
    Lee el título de la ventana activa (normalmente el navegador).
    """
    try:
        active_window = gw.getActiveWindow()
        return {
            "status": "SUCCESS",
            "page_title": active_window.title if active_window else "None"
        }
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}
