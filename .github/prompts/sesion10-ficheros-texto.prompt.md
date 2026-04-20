---
mode: 'agent'
description: 'Sesión 10 — Añadir persistencia en ficheros de texto plano (JSON/CSV)'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 10** de la asignatura.
El objetivo de hoy es añadir **persistencia en ficheros de texto plano**.

# TAREAS DE HOY (WORKFLOW)

1. Decidir el formato de serialización (recomendado: JSON por legibilidad). Documentar la decisión.
2. Crear adaptadores en `persistence/`:
   - Un adaptador por cada entidad principal del dominio.
   - Nombre: `<entidad>_repo_json.py`.
3. Añadir a las entidades los métodos de transformación:
   - `to_dict() -> dict`: serializa la entidad a diccionario.
   - `from_dict(data: dict) -> MiEntidad` (método de clase): reconstruye desde diccionario.
4. Llamar a `guardar` desde `services/` al final de cada operación que modifica datos.
5. Llamar a `cargar` al arrancar la app (en `main.py`) en lugar del seed de datos.
6. Añadir tests con ficheros temporales (`tmp_path` de pytest).

# REGLAS ESTRICTAS PARA HOY

- **Ningún I/O de ficheros en `entities/`**. `to_dict()` y `from_dict()` son aceptables (son transformaciones puras).
- El path del fichero se inyecta como parámetro en el constructor del adaptador, no se hardcodea.
- Usar siempre `pathlib.Path` para los paths.
- Manejar `FileNotFoundError` al cargar: si no existe el fichero, devolver lista vacía.
- No romper los tests existentes; el seed puede coexistir como fallback.

# MODO TUTOR

Muestra `to_dict()` de la entidad principal y cómo guardarlo con `json.dump`. Pide al alumno que implemente `from_dict()` y el adaptador de otra entidad.
