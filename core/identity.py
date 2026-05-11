# CONFIGURACIÓN DE IDENTIDAD - GEMINI-AETHER
SYSTEM_NAME = "GEMINI-AETHER"
VERSION = "0.1.0-ALPHA"
CORE_MODEL = "Gemini 1.5 Flash"
DEVELOPER = "Keilor Tellez"

def get_welcome_banner():
    return f"""
    ╔══════════════════════════════════════════╗
    ║        G E M I N I  -  A E T H E R       ║
    ╠══════════════════════════════════════════╣
    ║ > Núcleo: {CORE_MODEL}                   ║
    ║ > Usuario: {DEVELOPER}                   ║
    ║ > Estado: Local Host Active              ║
    ╚══════════════════════════════════════════╝
    """