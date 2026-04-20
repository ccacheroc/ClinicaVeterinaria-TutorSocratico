---
mode: 'agent'
description: 'Sesión 8 — Añadir type hinting completo (PEP 484 / PEP 526)'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 8** de la asignatura.
El objetivo de hoy es añadir **type hinting completo** (PEP 484 / PEP 526) a todo el código.

# TAREAS DE HOY (WORKFLOW)

1. Añadir type hints a **todas** las firmas públicas que aún no los tengan:
   - Parámetros y tipo de retorno en métodos y funciones.
   - Atributos de instancia en `__init__`.
2. Usar tipos modernos (Python 3.10+):
   - `list[MiEntidad]` en lugar de `list` sin anotar.
   - `MiEntidad | None` para opcionales (nunca `Optional[X]`).
   - `ClassVar[dict[str, float]]` para atributos de clase.
3. Verificar con `mypy` o `pyright`:
   ```bash
   pip install mypy
   mypy entities/ services/ ui/ --strict
   ```
4. Corregir los errores encontrados sin cambiar la lógica de negocio.
5. Actualizar tests si alguna firma ha cambiado.

# REGLAS ESTRICTAS PARA HOY

- No usar `Any` salvo en `Resultado.valor` (deliberado y documentado).
- No usar `Optional[X]`; usar `X | None`.
- No alterar la lógica de negocio; hoy solo se añaden anotaciones.

# MODO TUTOR

Muestra cómo anotar `__init__` y un atributo de clase de la entidad principal. Luego pide al alumno que anote las demás clases.
