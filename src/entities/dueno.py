class Dueno:
    """Representa al dueño de uno o varios animales registrados en la clínica."""

    def __init__(self, nif, nombre, email, tfno):
        self.__nif = nif
        self.__nombre = nombre
        self.__email = email
        self.__tfno = tfno
        self.__animales = []  # lista de animales asociados; se gestiona desde el servicio

