import os

def execute_ability(folder_path, extension):
    """
    HABILIDAD 045: file_filter.py
    """
    try:
        files = [f for f in os.listdir(folder_path) if f.endswith(extension)]
        return {"status": "SUCCESS", "files": files, "count": len(files)}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}