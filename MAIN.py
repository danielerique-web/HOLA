import tkinter as tk
from tkinter import messagebox
import random

class FUNDILLO_E_FATHER:
    def __init__(self, ventana):
        self.activo = True
        self.contador = 0
        self.ventana = ventana
        
        # 1. Título y color
        self.ventana.title("SISTEMA COMPROMETIDO")
        self.ventana.configure(bg='black')
        
        # 2. Mantener siempre al frente
        self.ventana.attributes('-topmost', True)
        
        # 3. Definir dimensiones y centrar
        self.ancho = 450
        self.alto = 350
        x = (self.ventana.winfo_screenwidth() // 2) - (self.ancho // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (self.alto // 2)
        self.ventana.geometry(f"{self.ancho}x{self.alto}+{x}+{y}")

        # 4. Contenido visual
        self.label = tk.Label(
            self.ventana,
            text="FUNDILLO\nDESPIERTA",
            font=("Arial", 50, "bold"),
            fg="#00ff41",
            bg="black",
            justify="center"
        )
        self.label.pack(expand=True, fill="both")

        self.mensajes = [
            "SIGO VIVO 😈",
            "No puedes matarme",
            "¿Ya estás llorando?",
            "FUNDILLO ETERNO",
            "Cierra sesión, cobarde",
            "JAJAJA sigo aquí",
            "Mírame fijamente"
        ]

        # Iniciar ciclo
        self.actualizar()

    def actualizar(self):
        if not self.activo: return
        self.contador += 1
        mensaje = random.choice(self.mensajes)
        
        # Actualizar texto
        self.label.config(text=f"{self.contador}\n{mensaje}")
        
        # Movimiento errático cada 7 segundos
        if self.contador % 7 == 0:
            self.mover_ventana()
        
        # Forzar que la ventana salte al frente cada segundo
        self.ventana.lift()
        
        self.ventana.after(1000, self.actualizar)

    def mover_ventana(self):
        try:
            ancho_p = self.ventana.winfo_screenwidth()
            alto_p  = self.ventana.winfo_screenheight()
            nx = random.randint(0, max(0, ancho_p - self.ancho))
            ny = random.randint(0, max(0, alto_p - self.alto))
            self.ventana.geometry(f"+{nx}+{ny}")
        except:
            pass

def impedir_cierre():
    # Esta función se activa cuando intentan cerrar la ventana
    messagebox.showwarning("ERROR FATAL", "No puedes cerrar esta unidad.\nFUNDILLO VIVE.")

if __name__ == "__main__":
    root = tk.Tk()
    
    # Bloquear el botón de cierre (X)
    root.protocol("WM_DELETE_WINDOW", impedir_cierre)
    
    app = FUNDILLO_E_FATHER(root)
    root.mainloop()
