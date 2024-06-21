class Curso:
    def __init__(self, nombre, profesor, horario):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []  # Inicialmente lista vacía
        self.horario = horario

    def mostrar_info(self):
        return f"Curso: {self.nombre}\nProfesor: {self.profesor}\nHorario: {self.horario}"

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
