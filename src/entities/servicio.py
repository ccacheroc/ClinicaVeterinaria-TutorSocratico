class Servicio:
    """Representa un servicio ofrecido por la clínica veterinaria."""
    def __init__(self, codigo, nombre, descripcion, precio, duracion_estimada):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__duracion_estimada = duracion_estimada
