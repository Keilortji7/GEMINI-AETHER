import zipfile
import os

def execute_ability(source_folder, output_name):
    """
    HABILIDAD 034: file_zip.py
    """
    try:
        zip_path = f"workspace/{output_name}.zip"
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for root, dirs, files in os.walk(source_folder):
                for file in files:
                    zipf.write(os.path.join(root, file), file)
        return {"status": "SUCCESS", "zip_created": zip_path}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}