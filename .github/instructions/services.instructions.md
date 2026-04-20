---
applyTo: 'services/**/*.py'
description: 'Reglas de la capa de servicios (casos de uso)'
---

# Reglas — Capa `services/`

## Responsabilidad

Esta capa orquesta los **casos de uso**: coordina entidades para llevar a cabo una operación completa.
Es el único lugar donde se combinan varias entidades para resolver una tarea.

## Dependencias permitidas

- ✅ Importar desde `entities/`.
- ✅ Importar desde `persistence/` (cuando esté implementada).
- ❌ Importar desde `ui/`.
- ❌ Usar `print()`, `input()` o cualquier I/O de consola.

## Firma de métodos

Cada método de servicio representa un caso de uso completo y **devuelve `Resultado`**:

```python
from entities.resultado import Resultado

class GestionEntidadService:
    """Orquesta operaciones sobre <nombre de la entidad principal>."""

    def __init__(self, repositorio: object) -> None:
        self.__repositorio = repositorio

    def registrar(self, identificador: str, datos: str) -> Resultado:
        """Crea y registra una nueva entidad.

        Returns:
            Resultado con ok=True si el registro fue correcto.
        """
        ...
```

> **Ejemplo en Coches2026**: `GestionConcesionarioService.registrar_coche(matricula, marca, tipo)`.

## Gestión de excepciones

Los servicios **no propagan** excepciones de dominio hacia `ui/`.
Si una entidad lanza una excepción de construcción, el servicio la captura y la convierte en `Resultado.error`:

```python
try:
    entidad = MiEntidad(identificador, datos)
except ValueError as e:
    return Resultado.error(str(e), "DATOS_INVALIDOS")
```

## Seed de datos

`seed_data_service.py` es un servicio especial de inicialización.
Se invoca **solo desde `main.py`** al arrancar la app.
Usa los mismos métodos públicos de servicio que usaría cualquier caso de uso real.

## Type hints

Obligatorios en todas las firmas. El tipo de retorno es siempre `Resultado` o un tipo concreto cuando no puede fallar.
