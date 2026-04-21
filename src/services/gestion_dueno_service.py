from src.entities.dueno import Dueno


class GestionDuenoService:
    """Orquesta la creación y consulta de Dueno.

    En esta sesión solo se crean objetos.
    Los métodos de negocio y el uso de Resultado se añadirán en la Sesión 3.

    Ejemplo:
        >>> servicio = GestionDuenoService()
        >>> dueno = servicio.registrar("12345678A", "Ana García", "ana@email.com", "600111222")
        >>> dueno is not None
        True
    """

    def __init__(self):
        self.__duenos = []

    def registrar(self, nif, nombre, email, tfno):
        """Crea un Dueno y lo guarda en memoria."""
        dueno = Dueno(nif, nombre, email, tfno)
        self.__duenos.append(dueno)
        return dueno

    def listar(self):
        """Devuelve todos los dueños registrados."""
        return list(self.__duenos)

