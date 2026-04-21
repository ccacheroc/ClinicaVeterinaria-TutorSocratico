from src.entities.animal import Animal


class GestionAnimalService:
    """Orquesta la creación y consulta de Animal.

    En esta sesión solo se crean objetos.
    Los métodos de negocio y el uso de Resultado se añadirán en la Sesión 3.

    Ejemplo:
        >>> servicio = GestionAnimalService()
        >>> dueno = ...  # obtenido desde GestionDuenoService
        >>> animal = servicio.registrar("Rex", "2020-03-15", "perro", "labrador", "negro", dueno)
        >>> animal is not None
        True
    """

    def __init__(self):
        self.__animales = []

    def registrar(self, nombre, fecha_nacimiento, tipo, raza, color, dueno):
        """Crea un Animal y lo guarda en memoria."""
        animal = Animal(nombre, fecha_nacimiento, tipo, raza, color, dueno)
        self.__animales.append(animal)
        return animal

    def listar(self):
        """Devuelve todos los animales registrados."""
        return list(self.__animales)

