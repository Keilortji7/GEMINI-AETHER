import webbrowser
import urllib.parse

def execute_ability(query):
    """
    HABILIDAD 022: web_search.py
    Objetivo: Realizar búsquedas en Google de forma automatizada.
    """
    try:
        # Codificamos el texto para que sea seguro en una URL
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"
        
        webbrowser.open(search_url)
        
        return {
            "status": "SUCCESS",
            "query": query,
            "search_url": search_url
        }
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print("--- TEST 022: WEB_SEARCH ---")
    print(execute_ability("HOla MUNDO"))