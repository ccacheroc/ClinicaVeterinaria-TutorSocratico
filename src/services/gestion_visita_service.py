from src.entities.visita import Visita


class GestionVisitaService:
    """Orquesta la creación y consulta de Visita.

    En esta sesión solo se crean objetos.
    Los métodos de negocio y el uso de Resultado se añadirán en la Sesión 3.

    Ejemplo:
        >>> servicio = GestionVisitaService()
        >>> visita = servicio.registrar("2026-04-21", servicio_obj, animal_obj, vet_obj)
        >>> visita is not None
        True
    """

    def __init__(self):
        self.__visitas = []

    def registrar(self, fecha, servicio, animal, veterinario, pagada=False):
        """Crea una Visita y la guarda en memoria."""
        visita = Visita(fecha, servicio, animal, veterinario, pagada)
        self.__visitas.append(visita)
        return visita

    def listar(self):
        """Devuelve todas las visitas registradas."""
        return list(self.__visitas)

