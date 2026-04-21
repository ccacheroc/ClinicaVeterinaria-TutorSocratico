class Visita:
    """Representa una visita de un animal a la clínica veterinaria."""

    def __init__(self, fecha, servicio, animal, veterinario, pagada=False):
        self.__fecha = fecha
        self.__servicio = servicio
        self.__animal = animal
        self.__veterinario = veterinario
        self.__pagada = pagada

