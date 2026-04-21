class Veterinario:
    """Representa un veterinario que trabaja en la clínica."""
    especialidades_clinicas = [
        "Medicina general", "Cirugía", "Dermatología",
        "Oftalmología", "Odontología", "Cardiología",
        "Traumatología", "Neurología", "Oncología", "Nutrición"
    ]

    tipos_animales_atendidos = [
        "Pequeños animales", "Grandes animales",
        "Aves", "Reptiles", "Roedores y conejos", "Animales exóticos"
    ]
    def __init__(self,nif,nombre,email,tfno,esp_clinicas = None,tipos_animales = None):
        self.__nif = nif
        self.__nombre = nombre
        self.__email = email
        self.__tfno = tfno
        self.__esp_clinicas = esp_clinicas if esp_clinicas is not None else []
        self.__tipos_animales = tipos_animales if tipos_animales is not None else []