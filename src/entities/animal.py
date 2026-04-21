class Animal:
    """Representa un animal registrado en la clínica veterinaria."""

    contador_por_tipo = {}  # atributo de clase: {"perro": 2, "gato": 1, ...}

    def __init__(self, nombre, fecha_nacimiento, tipo, raza, color, dueno):
        self.__nombre = nombre
        self.__fecha_nacimiento = fecha_nacimiento
        self.__tipo = tipo
        self.__raza = raza
        self.__color = color
        self.__afecciones = []
        self.__dueno = dueno

        tipo_lower = tipo.lower()
        Animal.contador_por_tipo[tipo_lower] = Animal.contador_por_tipo.get(tipo_lower, 0) + 1

