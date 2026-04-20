---
applyTo: 'persistence/**/*.py'
description: 'Reglas de la capa de persistencia (adaptadores de almacenamiento)'
---

# Reglas — Capa `persistence/`

## Responsabilidad

Esta capa implementa **adaptadores de almacenamiento**: serializa entidades a disco y las deserializa al arrancar.
Es la única capa que hace I/O de ficheros.

## Dependencias permitidas

- ✅ Importar desde `entities/` (solo para reconstruir objetos con `from_dict` / `pickle.load`).
- ❌ Importar desde `ui/` o `services/`.
- ❌ Lógica de negocio aquí — solo serialización / deserialización.

## Interfaz esperada de cada adaptador

Cada repositorio debe implementar al menos estos dos métodos:

```python
def guardar(self, datos: list) -> None:
    """Persiste la lista de objetos en el soporte elegido."""
    ...

def cargar(self) -> list:
    """Carga y devuelve la lista de objetos. Devuelve [] si no existe el fichero."""
    ...
```

## Adaptadores de texto (JSON)

```python
import json
from pathlib import Path

class EntidadRepoJson:
    def __init__(self, path: Path) -> None:
        self.__path = path

    def guardar(self, entidades: list) -> None:
        with open(self.__path, "w", encoding="utf-8") as f:
            json.dump([e.to_dict() for e in entidades], f, ensure_ascii=False, indent=2)

    def cargar(self) -> list:
        try:
            with open(self.__path, encoding="utf-8") as f:
                return [MiEntidad.from_dict(d) for d in json.load(f)]
        except FileNotFoundError:
            return []
```

> **Ejemplo en Coches2026**: `CochesRepoJson` usa `Coche.to_dict()` y `CocheCombustion.from_dict()`.

## Adaptadores binarios (Pickle)

```python
import pickle
from pathlib import Path

# WARNING: nunca cargar ficheros pickle de fuentes no confiables (riesgo de ejecución arbitraria).
class EntidadRepoBin:
    def __init__(self, path: Path) -> None:
        self.__path = path

    def guardar(self, entidades: list) -> None:
        with open(self.__path, "wb") as f:
            pickle.dump(entidades, f)

    def cargar(self) -> list:
        try:
            with open(self.__path, "rb") as f:
                return pickle.load(f)  # noqa: S301
        except FileNotFoundError:
            return []
```

## Paths

Usar siempre `pathlib.Path`. El path se **inyecta** en el constructor; nunca se hardcodea dentro del adaptador.

## Cuándo añadir un adaptador nuevo

1. Crear el fichero en `persistence/` con nombre `<entidad>_repo_<formato>.py`.
2. Inyectarlo en `services/` desde `main.py`.
3. Añadir test con `tmp_path` de pytest (sin tocar ficheros reales).
