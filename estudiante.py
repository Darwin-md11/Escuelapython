class Estudiante:
    def __init__(self, nombre, apellido, id_estudiante, curso):
        self.nombre = nombre
        self.apellido = apellido
        self.id_estudiante = id_estudiante
        self.cursos = [curso]  # Inicialmente lista con un solo curso

    def mostrar_info(self):
        return f"Estudiante: {self.nombre} {self.apellido}\nID: {self.id_estudiante}\nCursos: {', '.join(self.cursos)}"

    def agregar_curso(self, curso):
        self.cursos.append(curso)
