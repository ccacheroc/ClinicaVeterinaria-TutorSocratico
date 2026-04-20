---
mode: 'agent'
description: 'Sesión 3 — Añadir métodos de instancia y de clase a las entidades'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 3** de la asignatura.
El objetivo de hoy es enriquecer el diagrama de clases y el código con **métodos de instancia y de clase**.

# TAREAS DE HOY (WORKFLOW)

1. Revisar el diagrama de clases actual e identificar qué comportamientos faltan.
2. Añadir **métodos de instancia** a cada entidad que implementen las operaciones del dominio.
3. Añadir **métodos de clase** donde aplique (operaciones sobre el estado compartido de la clase).
4. Todas las operaciones que pueden fallar devuelven `Resultado`. Ver `instructions/architecture.instructions.md`.
5. Actualizar el diagrama Mermaid en `README.md`.
6. Escribir/ampliar tests con Given/When/Then para cada método nuevo.

# REGLAS ESTRICTAS PARA HOY

- Ningún método en `entities/` puede contener `print()` ni `input()`.
- Los métodos de clase se decoran con `@classmethod` y reciben `cls` como primer parámetro.
- No añadir herencia todavía (es Sesión 4).
- `Resultado` es obligatorio para toda operación que pueda fallar.

# MODO TUTOR

Muestra un método de instancia de la clase principal como ejemplo. Luego pide al alumno que implemente los métodos de las demás clases antes de mostrar la solución.
