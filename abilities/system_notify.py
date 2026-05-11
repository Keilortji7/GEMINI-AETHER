from plyer import notification
import time

def execute_ability(title, message):
    """
    HABILIDAD 025: system_notify.py (Versión Plyer)
    """
    try:
        notification.notify(
            title=title,
            message=message,
            app_name='AETHER',
            timeout=5
        )
        return {"status": "SUCCESS", "sent": True}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    print(execute_ability("AETHER", "¡Test de notificación exitoso!"))