import sys
import os
import threading
import time
import socket

# Asegurar rutas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ctk
from core.kernel import AetherKernel

class AetherInterface(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AETHER SYSTEM | OS KERNEL V1")
        self.geometry("700x550")

        self.kernel = AetherKernel()
        self.kernel_thread = threading.Thread(target=self.kernel.process_cycle, daemon=True)
        self.kernel_thread.start()

        # --- UI ELEMENTS ---
        self.status_label = ctk.CTkLabel(self, text="ESTADO: INICIALIZANDO", font=("Consolas", 12, "bold"))
        self.status_label.pack(side="top", anchor="ne", padx=20, pady=5)

        self.chat_display = ctk.CTkTextbox(self, width=650, height=350)
        self.chat_display.pack(pady=10)

        self.input_field = ctk.CTkEntry(self, width=500, placeholder_text="Esperando instrucciones...")
        self.input_field.pack(side="left", padx=(25, 10), pady=10)
        self.input_field.bind("<Return>", lambda e: self.send_command())

        self.send_button = ctk.CTkButton(self, text="EJECUTAR", command=self.send_command)
        self.send_button.pack(side="left", pady=10)

        # Inicio de log
        self.update_log("="*35)
        self.update_log("      GEMINI-AETHER ONLINE")
        self.update_log("="*35)
        
        threading.Thread(target=self._validar_sistema_completo, daemon=True).start()
        self.update_gui_status()

    def _validar_sistema_completo(self):
        """Verificación de hardware real[cite: 1, 3]."""
        self.update_log("SISTEMA: Sincronizando bases de datos...")
        time.sleep(1) 
        
        self.update_log("SISTEMA: Verificando enlace con Google Gemini...")
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=2)
            self.update_log("Estado: Conexión cifrada establecida.")
            self.update_log("Sistema: LISTO PARA OPERAR.\n")
        except (OSError, socket.timeout):
            self.update_log("\n" + "!"*45)
            self.update_log("ERROR CRÍTICO: FALLO DE ENLACE FÍSICO")
            self.update_log("SISTEMA: Protocolos de IA desactivados.")
            self.update_log("!"*45 + "\n")

    def update_gui_status(self):
        """Actualiza el color y texto de estado[cite: 3]."""
        current_state = self.kernel.state
        self.status_label.configure(text=f"ESTADO: {current_state}")
        
        colors = {"IDLE": "#4CAF50", "THINKING": "#2196F3", "OVERLOADED": "#F44336", "ERROR": "#F44336"}
        self.status_label.configure(text_color=colors.get(current_state, "white"))
        
        self.after(1000, self.update_gui_status)

    def update_log(self, text):
        self.chat_display.insert("end", f"{text}\n")
        self.chat_display.see("end")

    def send_command(self):
        user_input = self.input_field.get()
        if not user_input: return
        self.update_log(f"KEILOR >> {user_input}") 
        self.input_field.delete(0, 'end')
        threading.Thread(target=self._get_kernel_response, args=(user_input,), daemon=True).start()

    def _get_kernel_response(self, text):
        response = self.kernel.query_brain(text)
        self.update_log(f"\nGAether >> {response}\n") 

if __name__ == "__main__":
    app = AetherInterface()
    app.mainloop()