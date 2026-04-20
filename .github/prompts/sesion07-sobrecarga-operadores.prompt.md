---
mode: 'agent'
description: 'Sesión 7 — Sobrecarga de operadores matemáticos, comparación y acceso por índice'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 7** de la asignatura.
El objetivo de hoy es implementar la **sobrecarga de operadores**.

# TAREAS DE HOY (WORKFLOW)

1. Implementar `__eq__` y `__hash__` en las entidades que tienen identidad (igualdad por identificador único).
2. Implementar operadores de colección en la clase contenedora principal del dominio:
   - `__add__` / `__iadd__` (`+`, `+=`): añadir un elemento → nuevo objeto o mutación.
   - `__sub__` / `__isub__` (`-`, `-=`): eliminar un elemento por identificador.
3. Implementar `__getitem__` para acceder a elementos por índice o identificador.
4. Implementar `__contains__` (`in`) para comprobar si un identificador está en la colección.
5. Añadir tests para cada operador.

# REGLAS ESTRICTAS PARA HOY

- `__eq__` debe ir acompañado siempre de `__hash__` (si el objeto puede estar en sets o dicts).
- Los operadores que mutan el estado (`+=`, `-=`) devuelven `self`.
- Los operadores que crean copias (`+`, `-`) devuelven una **nueva instancia**.
- No romper tests existentes.

# MODO TUTOR

Muestra `__eq__` y `__hash__` de la entidad principal. Luego pide al alumno que implemente `__add__` de la clase contenedora antes de mostrar la solución.
