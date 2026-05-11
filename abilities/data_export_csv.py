import csv

def execute_ability(data_list, filename="report.csv"):
    """
    HABILIDAD 032: data_export_csv.py (VERSIÓN CORREGIDA PARA TILDES)
    """
    try:
        path = f"workspace/{filename}"
        # Cambiamos encoding a 'utf-8-sig' para compatibilidad total con Excel
        with open(path, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerows(data_list)
        return {"status": "SUCCESS", "file_saved": path}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}