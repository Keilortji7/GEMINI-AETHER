import os

def execute_ability():
    """
    HABILIDAD 048: project_summary.py
    """
    try:
        files = os.listdir("workspace")
        summary = f"RESUMEN DE WORKSPACE\nTotal archivos: {len(files)}\n"
        summary += "-"*20 + "\n"
        for f in files:
            summary += f"- {f}\n"
            
        with open("workspace/summary.txt", "w", encoding='utf-8') as s:
            s.write(summary)
        return {"status": "SUCCESS", "summary_created": True}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}