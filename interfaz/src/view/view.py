import tkinter as tk#libreria principal de la interfaz grafica
from tkinter import messagebox#creacion de ventanas y mensajes
import tkinter.colorchooser as colorchooser#selector de colores
from tkcalendar import DateEntry#selector de fechas
import datetime#tiempo y fecha
import re#expresiones regulares
#___________________________librerias  e importaciones_____________________________

class App_View(tk.Tk):
    def __init__(self)-> None:
        super().__init__()
        #____________________________configuracion de la ventana_____________________________
        self.geometry("800x520")#tamaño inicial
        self.overrideredirect(True)#oculta la barra de titulo predeterminada
        self.resizable(True, True)#permite mover y redimencionar la ventana
        self.minsize(700, 480)#tamaño minimo de la ventana

        # ___________________________paleta de colores de la venta y fuentes de las letras___________________________
        self.primary = "#2D6CDF"       
        self.surface = "#F4F7FB"       
        self.form_bg = "#FFFFFF"       
        self.muted = "#6B7280"         
        self.font_normal = ("Segoe UI", 10)
        self.font_label = ("Segoe UI", 10, "bold")

        self.controller = None
        self.barra_color = self.primary  # Color por defecto

        # Configuración ventana
        self.configure(bg=self.surface)

        # __________________________barra superior personalizada___________________________
        self.barra_superior = tk.Frame(self, bg=self.barra_color, height=36)
        self.barra_superior.pack(fill=tk.X)

        # _________________________titulo y botones de la barra superios__________________________
        self.title_label = tk.Label(self.barra_superior, text="Cuestionario", 
                                  bg=self.barra_color, fg="white", font=("Segoe UI", 11, "bold"))
        self.title_label.pack(side=tk.LEFT, padx=12)#titulo de la barra

        # Botones de la barra superior
        btn_opts = dict(bg=self.barra_color, fg="white", activebackground=self.barra_color,
                        activeforeground="white", borderwidth=0, font=("Segoe UI", 11, "bold"))
        
        #boton para cerra la app
        self.btn_cerrar = tk.Button(self.barra_superior, text="✕", command=self.quit, **btn_opts)
        self.btn_cerrar.pack(side=tk.RIGHT, padx=8, pady=2)
        
        #boton para maximizarla ventana
        self.btn_maximizar = tk.Button(self.barra_superior, text="▢", command=self.maximizar, **btn_opts)
        
        self.btn_maximizar.pack(side=tk.RIGHT, padx=4, pady=2)
        #boton para abrir la conficuracion 
        self.btn_config = tk.Button(self.barra_superior, text="⚙", command=self.abrir_configuracion, **btn_opts)
        self.btn_config.pack(side=tk.RIGHT, padx=8, pady=2)

        # Frame principal contenedor con padding
        self.fmr = tk.Frame(self, bg=self.form_bg, padx=20, pady=20, relief="flat")
        self.fmr.pack(fill=tk.BOTH, expand=True, padx=18, pady=(12,18))

        # Grid configuración para formulario
        self.fmr.columnconfigure(0, weight=0, minsize=160)
        self.fmr.columnconfigure(1, weight=1)

        # ____________________campos de formularios__________________________________________________________
        lbl_opts = dict(bg=self.form_bg, fg="black", anchor="w", font=self.font_label)
        ent_opts = dict(relief="groove", borderwidth=1, font=self.font_normal, bg="#ffffff", width=32)
        #___________________________nombre______________________________
        tk.Label(self.fmr, text="Nombre:", **lbl_opts).grid(row=0, column=0, sticky="w", pady=8, padx=(0,10))
        self.entry_nombre = tk.Entry(self.fmr, **ent_opts)
        self.entry_nombre.grid(row=0, column=1, sticky="ew", pady=8)
        #___________________________apellido______________________________
        tk.Label(self.fmr, text="Apellido:", **lbl_opts).grid(row=1, column=0, sticky="w", pady=8, padx=(0,10))
        self.entry_apellido = tk.Entry(self.fmr, **ent_opts)
        self.entry_apellido.grid(row=1, column=1, sticky="ew", pady=8)
        #___________________________fecha de nacimiento______________________________
        tk.Label(self.fmr, text="Fecha de nacimiento:", **lbl_opts).grid(row=2, column=0, sticky="w", pady=8, padx=(0,10))
        self.entry_edad = DateEntry(
            self.fmr,
            width=30,
            background='white',
            foreground='black',
            borderwidth=1,
            locale='es_ES',
            date_pattern='dd/mm/yyyy',
            year=2000,
            mindate=datetime.date(1900, 1, 1),
            maxdate=datetime.date.today(),
            showweeknumbers=False
        )
        self.entry_edad.grid(row=2, column=1, sticky="w", pady=8)
        #___________________________documento______________________________
        tk.Label(self.fmr, text="Documento:", **lbl_opts).grid(row=3, column=0, sticky="w", pady=8, padx=(0,10))
        self.entry_documento = tk.Entry(self.fmr, **ent_opts)
        self.entry_documento.grid(row=3, column=1, sticky="ew", pady=8)
        #___________________________correo electronico______________________________
        tk.Label(self.fmr, text="Correo electrónico:", **lbl_opts).grid(row=4, column=0, sticky="w", pady=8, padx=(0,10))
        self.entry_email = tk.Entry(self.fmr, **ent_opts)
        self.entry_email.grid(row=4, column=1, sticky="ew", pady=8)
        #___________________________telefono______________________________
        tk.Label(self.fmr, text="Teléfono:", **lbl_opts).grid(row=5, column=0, sticky="w", pady=8, padx=(0,10))
        self.entry_numero = tk.Entry(self.fmr, **ent_opts)
        self.entry_numero.grid(row=5, column=1, sticky="ew", pady=8)
        #___________________________cargo______________________________
        tk.Label(self.fmr, text="Cargo:", **lbl_opts).grid(row=6, column=0, sticky="w", pady=8, padx=(0,10))
        self.entry_cargo = tk.Entry(self.fmr, **ent_opts)
        self.entry_cargo.grid(row=6, column=1, sticky="ew", pady=8)
        #___________________________numero de hijos______________________________
        tk.Label(self.fmr, text="Número de hijos:", **lbl_opts).grid(row=7, column=0, sticky="w", pady=8, padx=(0,10))
        self.entry_hijos = tk.Entry(self.fmr, **ent_opts)
        self.entry_hijos.grid(row=7, column=1, sticky="ew", pady=8)

        # Separador visual
        sep = tk.Frame(self.fmr, height=1, bg="#E6E9EF")
        sep.grid(row=8, column=0, columnspan=2, sticky="ew", pady=(12,14))
        
        # ____________________Contenedor lateral para búsqueda_______________________________
        self.contenedor_principal = tk.Frame(self, bg=self.surface)
        self.contenedor_principal.place(relx=0.74, rely=0.08, relheight=0.82, relwidth=0.24)

        # ____________________________panel de busqueda____________________________________
        self.panel_busqueda = tk.LabelFrame(self.contenedor_principal, text=" Búsqueda ", padx=10, pady=10, bg=self.form_bg, font=self.font_label, fg="black")
        self.panel_busqueda.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        # ________________________________Campo de búsqueda con estilo____________________________
        tk.Label(self.panel_busqueda, text="Documento:", bg=self.form_bg, font=self.font_label).pack(anchor="w", pady=(4,6))
        self.entry_buscar = tk.Entry(self.panel_busqueda, width=18, relief="groove", borderwidth=1, font=self.font_normal)
        self.entry_buscar.pack(pady=(0,8))

        # ___________________________eventos para mover la ventana___________________________
        self.barra_superior.bind("<B1-Motion>", self.mover_ventana)
        self.barra_superior.bind("<Button-1>", self.guardar_posicion)
    #____________________________________funciones para la ventana _____________________________________
    
    #funciones del boton de configuracion, abre otra ventana aparte 
    def abrir_configuracion(self):
        config_win = tk.Toplevel(self)
        config_win.title("Configuración de colores")
        config_win.geometry("320x160")
        config_win.configure(bg="white")
        #permite cambiar el color de la barra superior, abre una paleta de colores  
        def cambiar_color_barra():
            color = colorchooser.askcolor(title="Color de la barra")[1]
            if color:
                self.barra_color = color
                self.barra_superior.configure(bg=color)
                self.title_label.configure(bg=color)
                self.btn_config.configure(bg=color, activebackground=color)
                self.btn_cerrar.configure(bg=color, activebackground=color)
                self.btn_maximizar.configure(bg=color, activebackground=color)
        #permite cambiar el color del fondo del formulario, abre una paleta de colores
        def cambiar_color_fondo():
            color = colorchooser.askcolor(title="Color del fondo")[1]
            if color:
                self.fmr.configure(bg=color)
                config_win.configure(bg=color)
                for widget in self.fmr.winfo_children():
                    if isinstance(widget, tk.Label):
                        widget.configure(bg=color)
        #botones para abrir las paletas de colores 
        btn_barra = tk.Button(config_win, text="Cambiar color de barra", command=cambiar_color_barra)
        btn_barra.pack(pady=10)
        btn_fondo = tk.Button(config_win, text="Cambiar color de fondo", command=cambiar_color_fondo)
        btn_fondo.pack(pady=6)
    #maximiza y restaura el tamaño de la ventana
    def maximizar(self):
        if self.state() == 'zoomed':
            self.state('normal')
        else:
            self.state('zoomed')
    
    def guardar_posicion(self, event):
            self.x = event.x
            self.y = event.y
    #funcion que permite mover la ventana en la pantalla 
    def mover_ventana(self, event):
            deltax = event.x - self.x
            deltay = event.y - self.y
            x = self.winfo_x() + deltax
            y = self.winfo_y() + deltay
            self.geometry(f"+{x}+{y}")

    def limpiar_form(self):
        # Limpia los campos del formulario
        for widget in [self.entry_nombre, self.entry_apellido, self.entry_documento,
                       self.entry_email, self.entry_numero, self.entry_cargo,
                       self.entry_hijos, self.entry_buscar]:
            try:
                widget.delete(0, tk.END)
            except Exception:
                pass
    #crea ventanas emergentes en caso de error o exito en la validacion de los datos 
    def validar_campos(self):
        letras_re = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$")
        numeros_re = re.compile(r"^\d+$")

        nombre = self.entry_nombre.get().strip()
        apellido = self.entry_apellido.get().strip()
        documento = self.entry_documento.get().strip()
        telefono = self.entry_numero.get().strip()
        hijos = self.entry_hijos.get().strip()
        cargo = self.entry_cargo.get().strip()
        correo = self.entry_email.get().strip()

        if not nombre or not letras_re.match(nombre):
            messagebox.showerror("Error de validación", "El campo 'nombre' debe contener solo letras.")
            self.entry_nombre.focus_set()
            return False

        if not apellido or not letras_re.match(apellido):
            messagebox.showerror("Error de validación", "El campo 'apellido' debe contener solo letras.")
            self.entry_apellido.focus_set()
            return False

        if not documento or not numeros_re.match(documento):
            messagebox.showerror("Error de validación", "El campo 'documento' debe contener solo números.")
            self.entry_documento.focus_set()
            return False

        email_re = re.compile(r"^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$", re.IGNORECASE)
        if not correo or not email_re.match(correo):
            messagebox.showerror("Error de validación", "El campo 'correo electronico' debe ser una dirección válida.")
            self.entry_email.focus_set()
            return False

        if telefono and not numeros_re.match(telefono):
            messagebox.showerror("Error de validación", "El campo 'telefono' debe contener solo números.")
            self.entry_numero.focus_set()
            return False

        if hijos and not numeros_re.match(hijos):
            messagebox.showerror("Error de validación", "El campo 'numero de hijos' debe contener solo números.")
            self.entry_hijos.focus_set()
            return False

        if not cargo or not letras_re.match(cargo):
            messagebox.showerror("Error de validación", "El campo 'cargo' debe contener solo letras.")
            self.entry_cargo.focus_set()
            return False

        messagebox.showinfo("Éxito", "Datos válidos.")
        return True

#el ejecutable temporal de la ventana de la vista 
if __name__ == "__main__":
    app = App_View()
    app.mainloop()