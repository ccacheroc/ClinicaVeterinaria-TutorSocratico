# AGENTS.md

Guía operativa para agentes de IA (Codex, Claude, Gemini CLI, Cursor Agent…) que trabajen en este repositorio.

---

## Qué es este proyecto

Consulta el fichero `README.md` del repositorio para obtener la descripción del proyecto, su dominio de negocio y su propósito académico.

Arquitectura de cuatro capas con dependencias **estrictamente unidireccionales**:
```
ui  →  services  →  entities  →  (persistence)
```

---

## Versión de Python

**No asumas una versión fija.** Detéctala en tiempo de ejecución a partir del entorno virtual activo:

```bash
python --version
# o bien
python -c "import sys; print(sys.version)"
```

Usa la versión que reporte ese comando como referencia para las type hints, sintaxis y características del lenguaje disponibles.

---

## Flujo de trabajo Git

- Se trabaja **directamente sobre `main`** — no hay ramas de trabajo.
- Antes de empezar cada sesión: `git pull origin main`.
- Al terminar cada sesión: `git push origin main`.
- Mensaje de commit: `"sesionXX: descripción corta en español"`.

> Flujo completo, coordinación entre miembros y resolución de conflictos en
> `.github/instructions/gitflow.instructions.md`.

---

## Comandos esenciales

```bash
# Crear entorno e instalar dependencias
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt   # o: pip install pytest si no hay requirements.txt

# Ejecutar la aplicación
python -m src.main

# Ejecutar todos los tests
python -m pytest -q

# Ejecutar tests de una capa concreta
python -m pytest tests/test_entities.py -v
```

---

## Estructura del proyecto

```
src/
├── main.py            ← punto de entrada; construye dependencias y lanza la UI
├── entities/          ← dominio puro (sin I/O)
├── services/          ← casos de uso; orquesta entidades
├── ui/                ← interfaz de consola
└── persistence/       ← adaptadores de almacenamiento (reservado)
tests/                 ← tests por capa: test_entities, test_*_service, test_ui_menu
```

---

## Reglas críticas que nunca debes violar

1. `ui/` **no puede importar** nada de `entities/`. Solo importa de `services/`.
2. `entities/` no contiene `print()`, `input()` ni acceso a ficheros.
3. `services/` no contiene I/O de consola — solo orquesta entidades.
4. Toda operación que puede fallar devuelve `Resultado` (nunca lanza excepción al exterior).
5. Atributos de instancia en `entities/` son siempre privados (`self.__nombre`); expuestos solo con `@property` de lectura. Setter solo si hay validación de dominio.
6. Type hints en todas las firmas públicas (versión detectada desde el entorno virtual).
7. Tests con pytest; estructura `Given/When/Then`. Mocks solo en tests de servicios y UI, nunca en tests de entidades.

---

## Dónde encontrar las reglas detalladas

| Qué necesitas saber | Fichero |
|---|---|
| Flujo Git sobre main, coordinación, conflictos | `.github/instructions/gitflow.instructions.md` |
| Arquitectura de capas completa | `.github/instructions/architecture.instructions.md` |
| Reglas de dominio y visibilidad OO | `.github/instructions/entities.instructions.md` |
| Convenciones Python del proyecto | `.github/instructions/python-conventions.instructions.md` |
| Casos de uso, gestión de errores en servicios | `.github/instructions/services.instructions.md` |
| Reglas de UI | `.github/instructions/ui.instructions.md` |
| Adaptadores JSON/Pickle, interfaz de repositorio | `.github/instructions/persistence.instructions.md` |
| Cómo escribir tests | `.github/instructions/tests.instructions.md` |
| Cómo generar diagramas Mermaid | `.github/instructions/mermaid.instructions.md` |
| Contexto pedagógico y tareas por sesión | `.github/prompts/sesionXX-*.prompt.md` |

---

## Qué NO hacer

- ❌ No mover ficheros de capa sin actualizar los imports de todas las capas dependientes.
- ❌ No añadir lógica de negocio en `ui/` ni `services/` que pertenezca a `entities/`.
- ❌ No crear tests que instancien entidades en `test_ui_menu.py` (usar mocks de servicios).
- ❌ No subir `.venv/`, `__pycache__/`, `dist/` ni `build/`.
- ❌ No asumir una versión de Python fija: detéctala siempre desde el entorno virtual.
- ❌ No usar `python main.py` — el punto de entrada correcto es `python -m src.main`.
- ❌ No lanzar excepciones al exterior desde entidades o servicios — usar `Resultado`.
