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

---

# ✅ DEFINITION OF DONE (DoD)

## Quality gates generales (aplican en todas las sesiones)
- [ ] `python -m pytest -q` → 0 fallos, 0 errores
- [ ] `python main.py` arranca sin errores
- [ ] No hay imports de `entities/` en `ui/`: `grep -r "from entities" ui/` → vacío
- [ ] Commits del día con patrón `sesion07: descripción corta`

## Quality gates específicos de esta sesión
- [ ] `__eq__` siempre acompañado de `__hash__` — la entidad puede usarse en `set` o como clave de `dict`
- [ ] `entidad1 == entidad2` compara por identidad de dominio (id único), no por referencia de memoria
- [ ] Operadores `+`/`-` devuelven nueva instancia; `+=`/`-=` devuelven `self`
- [ ] `elemento in coleccion` funciona correctamente (`__contains__`)
- [ ] `coleccion[clave]` funciona por índice y por identificador (`__getitem__`)
- [ ] Tests para cada operador: creación, igualdad, colecciones, acceso por índice

---

# 📓 JOURNAL DE SESIÓN

Al terminar, crea o actualiza `journal/sesion07.md` y haz commit:

```markdown
# Journal — Sesión 07 — [fecha]

## Integrantes
-
-

## ¿Qué hemos hecho hoy?


## Operadores implementados por clase
<!-- Lista: clase → __eq__, __add__, __getitem__, etc. -->

## Decisiones de diseño tomadas (y por qué)
<!-- Ej: __add__ crea nueva instancia porque la clase contenedora es inmutable en ese contexto -->

## Problemas encontrados y cómo los resolvimos


## ¿Qué queda pendiente para la próxima sesión?


## Tiempo invertido
- Horas de trabajo en equipo:
```

```bash
git add journal/sesion07.md
git commit -m "sesion07: journal de sesión"
git push origin sesion07-sobrecarga-operadores
```
