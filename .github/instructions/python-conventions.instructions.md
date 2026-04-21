---
applyTo: '**/*.py'
description: 'Convenciones Python del proyecto'
---

# Convenciones Python

## Versión y herramientas

- **Python 3.12+** obligatorio.
- Formateo: `black` (líneas ≤ 88 caracteres).
- Linting: `ruff`.
- Tests: `pytest`.

## Type hints

Todas las firmas públicas llevan type hints. Sin excepciones.

```python
# ✅ Correcto
def realizar_operacion(self, cantidad: float) -> Resultado:
    ...

# ❌ Incorrecto
def realizar_operacion(self, cantidad):
    ...
```

Usar `|` en lugar de `Optional` para tipos nullables (Python 3.10+):

```python
def __init__(self, recurso: Recurso | None = None) -> None:
```

## Nomenclatura

| Elemento | Convención | Ejemplo |
|---|---|---|
| Clases | `PascalCase` | `GestionInventario` |
| Métodos / funciones | `snake_case` | `calcular_total` |
| Atributos privados | `__doble_guion` | `self.__identificador` |
| Atributos protegidos | `_un_guion` (solo si herencia lo requiere) | `self._estado` |
| Constantes de módulo | `UPPER_SNAKE` | `MAX_INTENTOS` |

## Docstrings

Docstring corto en todas las clases y métodos públicos. Formato:

```python
def procesar(self, cantidad: float) -> Resultado:
    """Procesa la operación con la cantidad indicada.

    Args:
        cantidad: Valor a procesar (debe ser > 0).

    Returns:
        Resultado con ok=True si la operación fue exitosa.

    Example:
        >>> obj = MiClase("id-001")
        >>> obj.procesar(10).ok
        True
    """
```

> **Ejemplo en ClinicaVeterinaria**: `Coche.avanzar(km)`, `CocheCombustion.repostar(litros)`.

## Errores y excepciones

- En `entities/` y `services/`: **nunca** lanzar excepciones al llamador; devolver `Resultado.error(...)`.
- Solo lanzar excepciones internas (`ValueError`, `TypeError`) para programación defensiva dentro del método, si la situación es un bug (no un flujo de negocio esperado).

## `__str__` y `__repr__`

- `__str__`: legible para el usuario final (usado en `ui/`).
- `__repr__`: información técnica útil para depuración.

```python
# Ejemplo genérico
def __str__(self) -> str:
    return f"{self.__nombre} [{self.__identificador}]"

def __repr__(self) -> str:
    return f"{self.__class__.__name__}(id={self.__identificador!r})"

# Ejemplo en ClinicaVeterinaria
def __str__(self) -> str:
    return f"{self.__marca} ({self.__matricula}) — {self.__kilometros_recorridos:.1f} km"
```

## Imports

Orden: stdlib → third-party → proyecto (separados por línea en blanco).
No usar imports relativos (`from . import`) salvo en `__init__.py`.
