import os

def execute_ability(filename, start_path="."):
    """
    HABILIDAD 038: file_hunter.py
    """
    matches = []
    for root, dirs, files in os.walk(start_path):
        if filename in files:
            matches.append(os.path.join(root, filename))
    
    return {
        "status": "SUCCESS" if matches else "NOT_FOUND",
        "matches": matches
    }