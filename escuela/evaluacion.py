class Evaluacion:
    def __init__(self, curso, estudiante, nota):
        self.curso = curso
        self.estudiante = estudiante
        self.nota = nota

    def mostrar_info(self):
        return f"Curso: {self.curso}\nEstudiante: {self.estudiante}\nNota: {self.nota}"
