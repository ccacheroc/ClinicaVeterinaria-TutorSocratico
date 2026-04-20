---
mode: 'agent'
description: 'Sesión 5 — Añadir @property, herencia múltiple y clases abstractas'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 5** de la asignatura.
El objetivo de hoy es enriquecer el diseño con **propiedades (`@property`)**, **herencia múltiple** y **clases abstractas** donde proceda.

# TAREAS DE HOY (WORKFLOW)

1. Convertir la clase base principal en clase abstracta con `ABC` y decorar con `@abstractmethod` los métodos que cada subclase debe implementar obligatoriamente.
2. Identificar qué atributos necesitan `@property` de lectura (los que `services/` o `ui/` necesitan leer). Ver `instructions/entities.instructions.md`.
3. Añadir setter `@atributo.setter` solo donde la mutación tenga lógica de validación.
4. Si el dominio lo requiere, implementar herencia múltiple documentando el MRO elegido con un comentario.
5. Actualizar el diagrama de clases en `README.md`.
6. Verificar que todos los tests existentes siguen pasando.

# REGLAS ESTRICTAS PARA HOY

- La clase base abstracta no puede instanciarse directamente; debe lanzar `TypeError` si se intenta.
- No añadir setter si no hay validación real. Ver `instructions/entities.instructions.md`.
- El orden MRO en herencia múltiple debe ser explícito y documentado con un comentario en la clase.

# MODO TUTOR

Muestra cómo declarar la clase base como abstracta. Luego pide al alumno que identifique qué `@property` son necesarias antes de implementarlas.
