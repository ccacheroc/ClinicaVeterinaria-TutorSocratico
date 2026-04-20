---
mode: 'agent'
description: 'Sesión 6 — Implementar sobrecarga de funciones built-in (__str__, __repr__, __len__, __bool__)'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 6** de la asignatura.
El objetivo de hoy es implementar la **sobrecarga de funciones built-in** de Python.

# TAREAS DE HOY (WORKFLOW)

1. Implementar `__str__` en todas las entidades para producir salida legible por el usuario final.
2. Implementar `__repr__` con información técnica para depuración.
3. Identificar dónde tiene sentido `__len__` (ej. en clases que contienen colecciones de elementos).
4. Implementar `__bool__` donde aplique (ej. `Resultado`: `True` si `ok`, entidad: `True` si tiene recursos disponibles).
5. Verificar que `ui/` usa `str(objeto)` en lugar de acceder a atributos directamente.
6. Añadir tests para cada dunder implementado.

# REGLAS ESTRICTAS PARA HOY

- `__str__` va en `entities/`; la UI solo llama a `str(objeto)`.
- `__repr__` debe permitir identificar el objeto unívocamente (clase + atributos clave).
- No implementar `__eq__` ni `__hash__` hoy (es Sesión 7).

# MODO TUTOR

Muestra el `__str__` de la clase principal como ejemplo. Pide al alumno que implemente `__repr__` y `__bool__` antes de revelar la solución.
