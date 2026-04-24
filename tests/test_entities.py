"""Tests de construcción de las entidades — Sesión 02."""

from src.entities.aula import Aula
from src.entities.profesor import Profesor
from src.entities.reserva import Reserva


# ---------------------------------------------------------------------------
# Aula
# ---------------------------------------------------------------------------

def test_aula_se_crea_correctamente():
    # Given / When
    aula = Aula("A101", "Aula 101", "Aula de teoría", 30, "clase")

    # Then — el objeto existe y no lanza excepciones
    assert aula is not None


def test_aula_tiene_atributo_de_clase_tipos_validos():
    # Then — el atributo de clase existe independientemente de las instancias
    assert hasattr(Aula, "tipos_validos")
    assert len(Aula.tipos_validos) > 0


# ---------------------------------------------------------------------------
# Profesor
# ---------------------------------------------------------------------------

def test_profesor_se_crea_correctamente():
    # Given / When
    profesor = Profesor("12345678A", "Ana García", "Matemáticas", "ana@escuela.es")

    # Then — el objeto existe y no lanza excepciones
    assert profesor is not None


# ---------------------------------------------------------------------------
# Reserva
# ---------------------------------------------------------------------------

def test_reserva_se_crea_correctamente():
    # Given
    aula = Aula("A101", "Aula 101", "Aula de teoría", 30, "clase")
    profesor = Profesor("12345678A", "Ana García", "Matemáticas", "ana@escuela.es")

    # When
    reserva = Reserva("2026-04-22", "09:00", "11:00", "Clase de cálculo", profesor, aula)

    # Then — el objeto existe y no lanza excepciones
    assert reserva is not None

