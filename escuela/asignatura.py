class Asignatura:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor

    def mostrar_info(self):
        return f"Asignatura: {self.nombre}\nProfesor: {self.profesor}"
