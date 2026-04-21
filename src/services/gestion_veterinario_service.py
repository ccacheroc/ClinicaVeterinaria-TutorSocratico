from src.entities.veterinario import Veterinario


class GestionVeterinarioService:
    """Orquesta la creación y consulta de Veterinario.

    En esta sesión solo se crean objetos.
    Los métodos de negocio y el uso de Resultado se añadirán en la Sesión 3.

    Ejemplo:
        >>> servicio = GestionVeterinarioService()
        >>> vet = servicio.registrar("87654321B", "Dr. López", "lopez@clinica.com", "600333444")
        >>> vet is not None
        True
    """

    def __init__(self):
        self.__veterinarios = []

    def registrar(self, nif, nombre, email, tfno, esp_clinicas=None, tipos_animales=None):
        """Crea un Veterinario y lo guarda en memoria."""
        vet = Veterinario(nif, nombre, email, tfno, esp_clinicas, tipos_animales)
        self.__veterinarios.append(vet)
        return vet

    def listar(self):
        """Devuelve todos los veterinarios registrados."""
        return list(self.__veterinarios)

