import os

def execute_ability(old_name, new_name):
    """
    HABILIDAD 029: file_rename.py
    """
    try:
        os.rename(old_name, new_name)
        return {"status": "SUCCESS", "from": old_name, "to": new_name}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}