import os
import time

def execute_ability(folder_path, days=1):
    """
    HABILIDAD 044: folder_cleaner.py
    """
    try:
        now = time.time()
        count = 0
        for f in os.listdir(folder_path):
            file_path = os.path.join(folder_path, f)
            if os.stat(file_path).st_mtime < now - (days * 86400):
                os.remove(file_path)
                count += 1
        return {"status": "SUCCESS", "deleted_count": count}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}