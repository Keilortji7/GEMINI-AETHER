import requests
import os

def execute_ability(url, filename):
    """
    HABILIDAD 024: net_download.py
    Objetivo: Descargar archivos directamente de la web al workspace.
    """
    try:
        save_path = os.path.join("workspace", filename)
        response = requests.get(url, stream=True)
        
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return {"status": "SUCCESS", "saved_at": save_path}
        else:
            return {"status": "FAILED", "http_code": response.status_code}
            
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}