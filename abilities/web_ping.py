import requests

def execute_ability(url):
    """
    HABILIDAD 039: web_ping.py
    """
    try:
        response = requests.get(url, timeout=5)
        return {"status": "SUCCESS", "code": response.status_code, "ok": response.ok}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}