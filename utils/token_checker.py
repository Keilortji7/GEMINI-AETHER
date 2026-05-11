import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def check_usage():
    print("--- REPORTE DE RECURSOS AETHER ---")
    try:
        # Consultamos el estado del modelo específico que estás usando
        model_info = genai.get_model('models/gemini-2.5-flash')
        print(f"Modelo activo: {model_info.name}")
        print(f"Capacidad de entrada: {model_info.input_token_limit} tokens")
        print(f"Capacidad de salida: {model_info.output_token_limit} tokens")
        print("\n[NOTA]: Para ver el consumo exacto en dólares o cuota diaria,")
        print("debes ingresar a: https://aistudio.google.com/app/plan_usage")
    except Exception as e:
        print(f"Error al conectar con la API: {e}")

if __name__ == "__main__":
    check_usage()