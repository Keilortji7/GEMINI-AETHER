import re

def execute_ability(text, keyword):
    """
    HABILIDAD 033: text_finder.py
    """
    try:
        # Busca la oración que contiene la palabra clave
        sentences = re.findall(r'([^.]*?' + re.escape(keyword) + r'[^.]*\.)', text)
        return {"status": "SUCCESS", "matches": sentences, "count": len(sentences)}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}