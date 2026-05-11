import webbrowser
import time

def execute_ability(url):
    """
    HABILIDAD 021: web_browser.py
    Objetivo: Apertura instantánea de sitios web específicos.
    """
    try:
        # Abrir en el navegador predeterminado
        webbrowser.open(url)
        
        return {
            "status": "SUCCESS",
            "url_opened": url,
            "timestamp": time.time()
        }
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST 021: WEB_BROWSER ---")
    # Probamos abriendo Google directamente
    print(execute_ability("https://www.google.com"))