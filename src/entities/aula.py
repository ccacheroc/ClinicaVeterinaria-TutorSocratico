"""Entidad Aula — representa un espacio físico reservable de la escuela."""


class Aula:
    """Aula de la escuela que puede ser reservada por un profesor.

    Ejemplo:
        >>> aula = Aula("A101", "Aula 101", "Aula de teoría", 30, "clase")
        >>> aula is not None
        True
    """

    tipos_validos = ["laboratorio", "informática", "conferencias", "reuniones", "clase"]

    def __init__(self, identificador, nombre, descripcion, capacidad, tipo):
        self.__identificador = identificador
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__capacidad = capacidad
        self.__tipo = tipo
        self.__reservas = []

