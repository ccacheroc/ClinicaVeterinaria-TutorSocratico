from src.entities.animal import Animal
from src.entities.dueno import Dueno
from src.entities.veterinario import Veterinario
from src.entities.visita import Visita
from src.entities.servicio import Servicio


def test_dueno_se_crea_correctamente():
    # Given / When
    dueno = Dueno("12345678A", "Ana García", "ana@email.com", "600111222")

    # Then
    assert dueno is not None


def test_veterinario_se_crea_correctamente():
    # Given / When
    vet = Veterinario("87654321B", "Dr. López", "lopez@clinica.com", "600333444")

    # Then
    assert vet is not None


def test_veterinario_tiene_atributos_de_clase():
    # Then — los atributos de clase existen independientemente de las instancias
    assert hasattr(Veterinario, "especialidades_clinicas")
    assert hasattr(Veterinario, "tipos_animales_atendidos")
    assert len(Veterinario.especialidades_clinicas) > 0
    assert len(Veterinario.tipos_animales_atendidos) > 0


def test_servicio_se_crea_correctamente():
    # Given / When
    servicio = Servicio("S001", "Consulta general", "Revisión rutinaria del animal", 30.0, "30 min")

    # Then
    assert servicio is not None


def test_animal_se_crea_correctamente():
    # Given
    dueno = Dueno("12345678A", "Ana García", "ana@email.com", "600111222")

    # When
    animal = Animal("Rex", "2020-03-15", "perro", "labrador", "negro", dueno)

    # Then
    assert animal is not None


def test_animal_actualiza_contador_por_tipo():
    # Given — resetear el contador para aislar el test
    Animal.contador_por_tipo = {}

    # When
    dueno = Dueno("12345678A", "Ana García", "ana@email.com", "600111222")
    Animal("Rex", "2020-03-15", "perro", "labrador", "negro", dueno)
    Animal("Luna", "2021-06-01", "gato", "siamés", "blanco", dueno)
    Animal("Rocky", "2019-11-20", "perro", "bulldog", "marrón", dueno)

    # Then
    assert Animal.contador_por_tipo["perro"] == 2
    assert Animal.contador_por_tipo["gato"] == 1


def test_visita_se_crea_correctamente():
    # Given
    dueno = Dueno("12345678A", "Ana García", "ana@email.com", "600111222")
    animal = Animal("Rex", "2020-03-15", "perro", "labrador", "negro", dueno)
    vet = Veterinario("87654321B", "Dr. López", "lopez@clinica.com", "600333444")
    servicio = Servicio("S001", "Consulta general", "Revisión rutinaria", 30.0, "30 min")

    # When
    visita = Visita("2026-04-21", servicio, animal, vet)

    # Then
    assert visita is not None


def test_visita_no_pagada_por_defecto():
    # Given
    dueno = Dueno("12345678A", "Ana García", "ana@email.com", "600111222")
    animal = Animal("Rex", "2020-03-15", "perro", "labrador", "negro", dueno)
    vet = Veterinario("87654321B", "Dr. López", "lopez@clinica.com", "600333444")
    servicio = Servicio("S001", "Consulta general", "Revisión rutinaria", 30.0, "30 min")

    # When
    visita = Visita("2026-04-21", servicio, animal, vet)

    # Then — por defecto una visita recién creada no está pagada
    assert visita._Visita__pagada == False

