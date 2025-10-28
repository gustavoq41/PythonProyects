import tkinter as tk
from tkinter import messagebox
from src.model.model import cuestionario  # ajusta el import a tu estructura real
from src.view.view import App_View


class Cuestionario_Controller:
    def __init__(self, vista: App_View, modelo: cuestionario):
        self.vista = vista
        self.modelo = modelo

        # Conexión recíproca
        self.vista.controller = self

        # Crear botones de acciones (controla los eventos del usuario)
        self.crear_botones()

    def crear_botones(self):
        """Agrega botones al formulario para realizar acciones usando el modelo."""
        frame_botones = tk.Frame(self.vista.fmr, bg=self.vista.form_bg)
        frame_botones.grid(row=9, column=0, columnspan=2, pady=10)

        tk.Button(frame_botones, text="Mayúsculas", command=self.convertir_mayus).pack(side=tk.LEFT, padx=6)
        tk.Button(frame_botones, text="Minúsculas", command=self.convertir_minus).pack(side=tk.LEFT, padx=6)
        tk.Button(frame_botones, text="Título", command=self.convertir_titulo).pack(side=tk.LEFT, padx=6)
        tk.Button(frame_botones, text="Validar", command=self.vista.validar_campos).pack(side=tk.LEFT, padx=6)
        tk.Button(frame_botones, text="Limpiar", command=self.vista.limpiar_form).pack(side=tk.LEFT, padx=6)

    # ------------------- Métodos de acción (llaman al modelo) -------------------

    def obtener_nombre(self):
        """Obtiene el texto del campo nombre."""
        nombre = self.vista.entry_nombre.get().strip()
        if not nombre:
            messagebox.showerror("Error", "Por favor ingresa un nombre.")
            return None
        return nombre

    def convertir_mayus(self):
        """Convierte el nombre a mayúsculas usando el modelo."""
        nombre = self.obtener_nombre()
        if nombre:
            resultado = nombre.upper()
            self.vista.entry_nombre.delete(0, tk.END)
            self.vista.entry_nombre.insert(0, resultado)
            self.modelo.Convertirmayus(nombre)

    def convertir_minus(self):
        """Convierte el nombre a minúsculas usando el modelo."""
        nombre = self.obtener_nombre()
        if nombre:
            resultado = nombre.lower()
            self.vista.entry_nombre.delete(0, tk.END)
            self.vista.entry_nombre.insert(0, resultado)
            self.modelo.Converitrminus(nombre)

    def convertir_titulo(self):
        """Convierte el nombre a formato título usando el modelo."""
        nombre = self.obtener_nombre()
        if nombre:
            resultado = nombre.title()
            self.vista.entry_nombre.delete(0, tk.END)
            self.vista.entry_nombre.insert(0, resultado)
            self.modelo.Convertirtitulo(nombre)
