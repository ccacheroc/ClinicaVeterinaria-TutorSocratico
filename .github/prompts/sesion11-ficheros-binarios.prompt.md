---
mode: 'agent'
description: 'Sesión 11 — Añadir persistencia en ficheros binarios (pickle)'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 11** de la asignatura.
El objetivo de hoy es añadir **persistencia en ficheros binarios** usando `pickle`.

# TAREAS DE HOY (WORKFLOW)

1. Crear adaptadores binarios en `persistence/`:
   - Nombre: `<entidad>_repo_bin.py`.
2. Usar `pickle.dump` / `pickle.load` para serializar objetos directamente:
   ```python
   import pickle
   from pathlib import Path

   class EntidadRepoBin:
       def __init__(self, path: Path) -> None:
           self.__path = path

       def guardar(self, entidades: list) -> None:
           with open(self.__path, "wb") as f:
               pickle.dump(entidades, f)

       def cargar(self) -> list:
           try:
               with open(self.__path, "rb") as f:
                   return pickle.load(f)
           except FileNotFoundError:
               return []
   ```
3. Comparar ventajas/desventajas de pickle vs JSON (documentar en un comentario):

   | | JSON (texto) | Pickle (binario) |
   |---|---|---|
   | Legible por humanos | ✅ | ❌ |
   | Serializa objetos Python directamente | ❌ (requiere `to_dict`) | ✅ |
   | Portable entre versiones | ✅ | ⚠️ |
   | Seguro con datos no confiables | ✅ | ❌ |

4. Configurar `main.py` para elegir entre adaptador binario y de texto mediante una constante.
5. Añadir tests con `tmp_path` que verifiquen que los objetos se guardan y recuperan correctamente.

# REGLAS ESTRICTAS PARA HOY

- **Nunca** cargar un fichero pickle de una fuente no confiable. Documentarlo con `# WARNING`.
- Los adaptadores binarios y de texto tienen la misma interfaz (`guardar` / `cargar`); son intercambiables.
- No cambiar las entidades para acomodar pickle (deben ser serializables por defecto).

# MODO TUTOR

Muestra el adaptador binario de la entidad principal. Pide al alumno que implemente el de otra entidad y que escriba el test antes de mostrar la solución.
