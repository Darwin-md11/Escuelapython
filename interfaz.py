import tkinter as tk
from tkinter import ttk



from profesor import Profesor
from estudiante import Estudiante
from asignatura import Asignatura
from evaluacion import Evaluacion
from horario import Horario
from curso import Curso

class RegistroAcademico(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registro Académico")

        # Obtener las dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Definir el tamaño de la ventana
        window_width = 800  # Aumentado el ancho de la ventana para ajustar mejor los widgets
        window_height = 600  # Aumentado el alto de la ventana para ajustar mejor los widgets

        # Calcular las coordenadas para centrar la ventana
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Configurar la geometría de la ventana
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Definir colores suaves
        self.bg_color = "#f0f8ff"  # Color de fondo suave
        self.tab_bg_color = "#e6f7ff"  # Color de fondo de las pestañas

        # Configurar estilos
        self.style = ttk.Style()
        self.style.configure('TNotebook.Tab', font=('Helvetica', '12', 'bold'))
        self.style.configure('TLabel', font=('Helvetica', '10'))
        self.style.configure('TButton', font=('Helvetica', '10', 'bold'))
        self.style.configure('Custom.TFrame', background=self.tab_bg_color)

        # Configurar fondo de la ventana principal
        self.configure(bg=self.bg_color)

        # Listas para almacenar objetos
        self.cursos = []
        self.profesores = []
        self.estudiantes = []
        self.asignaturas = []
        self.evaluaciones = []
        self.horarios = []

        # Inicializar el control de pestañas
        self.tab_control = ttk.Notebook(self)
        self.tabs = {}
        tab_names = ['Cursos', 'Profesores', 'Estudiantes', 'Asignaturas', 'Evaluaciones', 'Horarios']

        for tab_name in tab_names:
            tab = ttk.Frame(self.tab_control, style='Custom.TFrame')
            self.tab_control.add(tab, text=tab_name)
            self.tabs[tab_name] = tab

        self.tab_control.pack(expand=1, fill="both", padx=10, pady=10)

        # Inicializar las pestañas
        self.init_tabs()

    def init_tabs(self):
        for tab_name in self.tabs:
            init_method = getattr(self, f'init_tab_{tab_name.lower()}', None)
            if init_method:
                init_method(self.tabs[tab_name])

    def create_entry_frame(self, parent, fields, button_text, command):
        frame = ttk.Frame(parent, style='Custom.TFrame')
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        entries = {}
        for field in fields:
            ttk.Label(frame, text=field, background=self.tab_bg_color).grid(row=fields.index(field), column=0, padx=5, pady=5, sticky="w")
            entry = ttk.Entry(frame)
            entry.grid(row=fields.index(field), column=1, padx=5, pady=5, sticky="ew")
            entries[field] = entry

        ttk.Button(frame, text=button_text, command=lambda: command(entries)).grid(row=len(fields), column=0, columnspan=2, padx=5, pady=10)

    def create_listbox(self, parent):
        listbox = tk.Listbox(parent, height=10, borderwidth=2, relief="ridge")
        listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        return listbox

    def init_tab_cursos(self, tab):
        fields = ["Nombre", "Profesor", "Horario"]
        self.create_entry_frame(tab, fields, "Registrar Curso", self.registrar_curso)
        self.lista_cursos = self.create_listbox(tab)

    def init_tab_profesores(self, tab):
        fields = ["Nombre", "Apellido"]
        self.create_entry_frame(tab, fields, "Registrar Profesor", self.registrar_profesor)
        self.lista_profesores = self.create_listbox(tab)

    def init_tab_estudiantes(self, tab):
        fields = ["Nombre", "Apellido", "ID Estudiante", "Curso"]
        self.create_entry_frame(tab, fields, "Registrar Estudiante", self.registrar_estudiante)
        self.lista_estudiantes = self.create_listbox(tab)

    def init_tab_asignaturas(self, tab):
        fields = ["Nombre", "Profesor"]
        self.create_entry_frame(tab, fields, "Registrar Asignatura", self.registrar_asignatura)
        self.lista_asignaturas = self.create_listbox(tab)

    def init_tab_evaluaciones(self, tab):
        fields = ["Curso", "Estudiante", "Nota"]
        self.create_entry_frame(tab, fields, "Registrar Evaluación", self.registrar_evaluacion)
        self.lista_evaluaciones = self.create_listbox(tab)

    def init_tab_horarios(self, tab):
        fields = ["Día"]
        self.create_entry_frame(tab, fields, "Registrar Horario", self.registrar_horario)
        self.lista_horarios = self.create_listbox(tab)

    def registrar_curso(self, entries):
        nombre = entries["Nombre"].get()
        profesor = entries["Profesor"].get()
        horario = entries["Horario"].get()
        if nombre and profesor and horario:
            curso = Curso(nombre, profesor, horario)
            self.cursos.append(curso)
            self.lista_cursos.insert(tk.END, nombre)
            self.clear_entries(entries)

    def registrar_profesor(self, entries):
        nombre = entries["Nombre"].get()
        apellido = entries["Apellido"].get()
        if nombre and apellido:
            profesor = Profesor(nombre, apellido)
            self.profesores.append(profesor)
            self.lista_profesores.insert(tk.END, f"{nombre} {apellido}")
            self.clear_entries(entries)

    def registrar_estudiante(self, entries):
        nombre = entries["Nombre"].get()
        apellido = entries["Apellido"].get()
        id_estudiante = entries["ID Estudiante"].get()
        curso = entries["Curso"].get()
        if nombre and apellido and id_estudiante and curso:
            estudiante = Estudiante(nombre, apellido, id_estudiante, curso)
            self.estudiantes.append(estudiante)
            self.lista_estudiantes.insert(tk.END, f"{nombre} {apellido}")
            self.clear_entries(entries)

    def registrar_asignatura(self, entries):
        nombre = entries["Nombre"].get()
        profesor = entries["Profesor"].get()
        if nombre and profesor:
            asignatura = Asignatura(nombre, profesor)
            self.asignaturas.append(asignatura)
            self.lista_asignaturas.insert(tk.END, nombre)
            self.clear_entries(entries)

    def registrar_evaluacion(self, entries):
        curso = entries["Curso"].get()
        estudiante = entries["Estudiante"].get()
        nota = entries["Nota"].get()
        if curso and estudiante and nota:
            evaluacion = Evaluacion(curso, estudiante, nota)
            self.evaluaciones.append(evaluacion)
            self.lista_evaluaciones.insert(tk.END, f"{curso} - {estudiante} - {nota}")
            self.clear_entries(entries)

    def registrar_horario(self, entries):
        dia = entries["Día"].get()
        if dia:
            horario = Horario(dia, "", "")  # Puedes agregar hora_inicio y hora_fin si es necesario
            self.horarios.append(horario)
            self.lista_horarios.insert(tk.END, dia)
            self.clear_entries(entries)

    def clear_entries(self, entries):
        for entry in entries.values():
            entry.delete(0, tk.END)

if __name__ == "__main__":
    app = RegistroAcademico()
    app.mainloop()
