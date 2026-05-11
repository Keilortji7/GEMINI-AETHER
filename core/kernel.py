import importlib.util
import time
import json
import os
from core.sensors import AetherSensors
from core.aether_core import AetherCore

class AetherKernel:
    def __init__(self):
        self.sensors = AetherSensors()
        self.brain = AetherCore()
        
        # Iniciamos sin herramientas para limpieza total
        self.brain.setup_chat(tools=[])

        self.state = "IDLE"
        self.log_path = "logs/events.json"
        self._ensure_log_exists()
        self.data = self._load_session_data()
        self.daily_token_limit = 50000
        self.is_running = True
        
        print(f"\n[KERNEL] {time.strftime('%H:%M:%S')} | Monitor: ONLINE")
        print(f"[KERNEL] {time.strftime('%H:%M:%S')} | Estado Inicial: {self.state}\n")

    def _ensure_log_exists(self):
        if not os.path.exists('logs'):
            os.makedirs('logs')

    def _load_session_data(self):
        if os.path.exists(self.log_path):
            with open(self.log_path, 'r') as f:
                return json.load(f)
        return {"tokens_today": 0, "events": [], "last_session": time.strftime("%Y-%m-%d")}

    def _save_session_data(self):
        with open(self.log_path, 'w') as f:
            json.dump(self.data, f, indent=4)

    def update_state(self):
        """Monitorea el cambio de estado y lo imprime en terminal."""
        old_state = self.state
        event = self.sensors.get_system_event()
        
        if event == "EVENT_CRITICAL_LOAD" or self.data["tokens_today"] >= self.daily_token_limit:
            self.state = "OVERLOADED"
        elif self.state not in ["THINKING", "PROCESSING"]:
            self.state = "IDLE"
            
        if old_state != self.state:
            print(f"[KERNEL] {time.strftime('%H:%M:%S')} | CAMBIO DE ESTADO: {old_state} -> {self.state}")

    def query_brain(self, prompt):
        if self.state == "OVERLOADED":
            return "<STATUS> | SYSTEM_BLOCK | OVERLOADED"
        
        self.state = "THINKING"
        print(f"[KERNEL] {time.strftime('%H:%M:%S')} | Solicitando respuesta a AetherCore...")
        
        try:
            result = self.brain.get_response(prompt)
            self.data["tokens_today"] += result["tokens"]
            self._save_session_data()
            self.state = "IDLE"
            return f"{result['text']}\n\n[TKN: {result['tokens']} | TOTAL: {self.data['tokens_today']}]"
        except Exception as e:
            self.state = "ERROR"
            print(f"[KERNEL] {time.strftime('%H:%M:%S')} | ERROR EN QUERY: {str(e)}")
            return f"<STATUS> | ERROR | {str(e)}"

    def process_cycle(self):
        """Bucle infinito del hilo secundario."""
        while self.is_running:
            try:
                self.update_state()
            except Exception as e:
                print(f"[KERNEL] {time.strftime('%H:%M:%S')} | CRITICAL LOOP ERROR: {e}")
            time.sleep(2)
    
    def call_ability(self, ability_name, *args):
        """
        Carga y ejecuta una habilidad desde la carpeta /abilities[cite: 4].
        """
        file_path = f"abilities/{ability_name}.py"
        if not os.path.exists(file_path):
            return f"<STATUS> | ERROR | Habilidad {ability_name} no encontrada."

        try:
            # Protocolo de importación dinámica para scripts independientes[cite: 4]
            spec = importlib.util.spec_from_file_location(ability_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Ejecución de la lógica interna del script[cite: 4, 9]
            result = module.execute_ability(*args)
            
            # Registro en el log para que Gemini aprenda del éxito/fallo[cite: 3, 4]
            self.data["events"].append({
                "type": "ABILITY_EXECUTION",
                "name": ability_name,
                "result": result,
                "timestamp": time.strftime("%H:%M:%S")
            })
            self._save_session_data()
            
            return f"<STATUS> | SUCCESS | {ability_name} ejecutado: {result['status']}"
            
        except Exception as e:
            return f"<STATUS> | ERROR | Fallo en {ability_name}: {str(e)}"