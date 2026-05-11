import os

def execute_ability(file_path):
    """
    HABILIDAD 041: file_size_check.py
    Objetivo: Obtener el tamaño de un archivo en MB.
    """
    try:
        size_bytes = os.path.getsize(file_path)
        size_mb = round(size_bytes / (1024 * 1024), 2)
        return {"status": "SUCCESS", "size_mb": size_mb}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}