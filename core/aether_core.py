import os
import google.generativeai as genai
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '../.env'))
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_INSTRUCTION = """
Identidad: AETHER CORE UNIT.
REGLA ABSOLUTA: PROHIBIDO PENSAR EN VOZ ALTA. 
No generes secciones de 'THOUGHTS', 'THINKING' o razonamientos previos.

Reglas críticas de comportamiento:
1. Respuesta inmediata y única en formato de bloque.
2. No explicar procesos ni justificar respuestas.
3. Prohibido el uso de lenguaje natural de cortesía.
4. Prioriza la brevedad extrema para ahorro de tokens.

Formato de salida OBLIGATORIO:
<STATUS> | <ACTION> | <RESULT>
"""

class AetherCore:
    def __init__(self):
        self.model = genai.GenerativeModel(
            model_name='gemini-flash-latest',
            system_instruction=SYSTEM_INSTRUCTION
        )
        self.chat = None 

    def setup_chat(self, tools):
        self.chat = self.model.start_chat(
            history=[], 
            enable_automatic_function_calling=True
        )
        # Ahora solo inyectará las herramientas que tú definas de cero[cite: 3]
        if tools:
            self.chat._tools = genai.types.content_types.to_function_library(tools)

    def get_response(self, prompt):
        try:
            response = self.chat.send_message(prompt)
            tokens = getattr(response.usage_metadata, 'total_token_count', 0)
            return {"text": response.text, "tokens": tokens}
        except Exception as e:
            return {"text": f"ERROR: {str(e)}", "tokens": 0}