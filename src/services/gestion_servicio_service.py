from src.entities.servicio import Servicio


class GestionServicioService:
    """Orquesta la creación y consulta del catálogo de Servicio.

    En esta sesión solo se crean objetos.
    Los métodos de negocio y el uso de Resultado se añadirán en la Sesión 3.

    Ejemplo:
        >>> servicio = GestionServicioService()
        >>> s = servicio.registrar("S001", "Consulta general", "Revisión rutinaria", 30.0, "30 min")
        >>> s is not None
        True
    """

    def __init__(self):
        self.__servicios = []

    def registrar(self, codigo, nombre, descripcion, precio, duracion_estimada):
        """Crea un Servicio y lo guarda en el catálogo."""
        servicio = Servicio(codigo, nombre, descripcion, precio, duracion_estimada)
        self.__servicios.append(servicio)
        return servicio

    def listar(self):
        """Devuelve todos los servicios del catálogo."""
        return list(self.__servicios)

