---
mode: 'agent'
description: 'Sesión 9 — Añadir jerarquía de excepciones propias del dominio'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 9** de la asignatura.
El objetivo de hoy es añadir **manejo de excepciones** propio del dominio.

# TAREAS DE HOY (WORKFLOW)

1. Crear una jerarquía de excepciones propias en `entities/excepciones.py`:
   ```python
   class AppError(Exception): ...           # base de todas las excepciones del proyecto
   class IdentificadorInvalidoError(AppError): ...
   class RecursoInsuficienteError(AppError): ...
   class ElementoDuplicadoError(AppError): ...
   # Añadir las que el dominio del proyecto necesite
   ```
2. Lanzar estas excepciones en `__init__` para **invariantes de construcción** (datos de entrada inválidos).
3. **Mantener `Resultado`** para errores de flujo de negocio esperados (operación que falla por lógica, no por bug).
4. Capturar excepciones en `ui/` y mostrar mensaje amigable al usuario.
5. Añadir tests que verifiquen que las excepciones se lanzan en los casos correctos.

# CRITERIO: excepción vs Resultado

| Situación | Mecanismo |
|---|---|
| Identificador vacío al construir la entidad | `raise IdentificadorInvalidoError` |
| Operación que falla por falta de recursos | `return Resultado.error(...)` |
| Formato de dato inválido en construcción | `raise ValueError` o excepción propia |
| Elemento ya registrado en la colección | `return Resultado.error(...)` |

# REGLAS ESTRICTAS PARA HOY

- Las excepciones del dominio heredan de `AppError`, no directamente de `Exception`.
- `services/` no lanza excepciones propias; las deja propagar o las convierte en `Resultado`.
- `ui/` captura excepciones y las muestra como mensajes de error sin stack trace.

# MODO TUTOR

Muestra cómo crear `AppError` y la primera excepción específica. Pide al alumno que añada la validación en `__init__` de la entidad principal antes de mostrar la solución.
