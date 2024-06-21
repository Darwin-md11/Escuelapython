class Horario:
    def __init__(self, dia, hora_inicio, hora_fin):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def mostrar_info(self):
        return f"Día: {self.dia}\nHora de inicio: {self.hora_inicio}\nHora de fin: {self.hora_fin}"
