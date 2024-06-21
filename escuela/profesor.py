class Profesor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.asignaturas = []  # Inicialmente lista vacía

    def mostrar_info(self):
        return f"Profesor: {self.nombre} {self.apellido}"

    def agregar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)
