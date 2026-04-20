---
applyTo: '**/*'
description: 'Flujo de trabajo Git para equipos de dos personas trabajando sobre main'
---

# Flujo de trabajo Git — Equipos de dos personas sobre `main`

## Por qué trabajamos sobre `main` directamente

En esta asignatura **no se usan ramas de trabajo**. El motivo es pedagógico: el objetivo es aprender a coordinarse en tiempo real, gestionar conflictos cuando ocurren y mantener `main` siempre en un estado funcional. Este es también el flujo habitual en equipos pequeños con ciclos de entrega muy cortos.

---

## Ritual de inicio de sesión (obligatorio)

Antes de tocar cualquier fichero, **siempre**:

```bash
git pull origin main
```

Esto evita la mayoría de los conflictos. Si no se hace y el compañero ha subido cambios, el `push` fallará.

---

## Ciclo básico de trabajo

```
pull → editar → add → commit → pull → push
```

El `pull` antes del `push` es clave: integra los cambios del compañero antes de subir los propios.

```bash
# 1. Sincronizar antes de empezar
git pull origin main

# 2. Trabajar en el código...

# 3. Preparar los cambios
git add <ficheros>          # añadir ficheros concretos (preferible a git add .)
git status                  # revisar qué se va a commitear

# 4. Commitear con mensaje descriptivo
git commit -m "sesionXX: descripción corta en español"

# 5. Sincronizar de nuevo antes de subir (por si el compañero ha pusheado)
git pull origin main

# 6. Subir
git push origin main
```

---

## Mensajes de commit

Patrón obligatorio: `sesionXX: descripción corta en español`

```bash
# ✅ Correcto
git commit -m "sesion03: añadir método avanzar a Coche con Resultado"
git commit -m "sesion05: convertir Coche en clase abstracta con ABC"

# ❌ Incorrecto
git commit -m "cambios"
git commit -m "fix"
git commit -m "WIP"
```

**Criterios de un buen commit:**
- Atómico: un commit = un cambio coherente (no mezclar refactor + nueva feature).
- El proyecto debe funcionar (`python main.py` y `pytest`) después de cada commit.
- El mensaje explica el *qué*, no el *cómo*.

---

## Coordinación entre los dos miembros del equipo

### Regla de oro: no editéis el mismo fichero a la vez

La forma más sencilla de evitar conflictos es **dividir el trabajo por ficheros o clases**:

```
# Sesión de ejemplo — división del trabajo
Miembro A → entities/coche.py + entities/coche_combustion.py
Miembro B → entities/coche_electrico.py + tests/test_entities.py
```

### Comunicación antes de empezar cada bloque de trabajo

Antes de ponerse a escribir código, acordad en voz alta (o por mensaje) qué va a tocar cada uno. Treinta segundos de coordinación evitan diez minutos de resolución de conflictos.

---

## Gestión de conflictos

Los conflictos ocurren cuando los dos miembros modifican las **mismas líneas** del mismo fichero. Git los marca así:

```
<<<<<<< HEAD
    def avanzar(self, km):       # tu versión local
=======
    def avanzar(self, km: float):  # versión del compañero
>>>>>>> origin/main
```

### Cómo resolverlos

1. Abrir el fichero en conflicto (PyCharm lo resalta en rojo).
2. Elegir qué versión conservar — o combinar ambas manualmente.
3. Eliminar las marcas `<<<<<<<`, `=======`, `>>>>>>>`.
4. Verificar que el código funciona: `python main.py` + `pytest`.
5. Hacer commit de la resolución:

```bash
git add <fichero-resuelto>
git commit -m "sesionXX: resolver conflicto en <fichero>"
git push origin main
```

### En PyCharm

`Git → Resolve Conflicts` abre una vista de tres paneles (local / base / remoto) que facilita la resolución visual sin editar las marcas a mano.

---

## Comprobación del estado del repositorio

```bash
git status          # ficheros modificados, staged, sin seguimiento
git log --oneline   # historial compacto de commits
git diff            # cambios no staged
git diff --staged   # cambios staged (listos para commit)
```

---

## Qué NO hacer nunca

| ❌ Acción prohibida | ✅ Alternativa |
|---|---|
| `git push --force` | Hablar con el compañero y resolver el conflicto |
| `git add .` sin revisar `git status` antes | `git status` → `git add <ficheros concretos>` |
| Commitear con `python main.py` o `pytest` fallando | Arreglar antes de commitear |
| Subir `.venv/`, `.idea/`, `__pycache__/` | Verificar `.gitignore` y usar `git status` |
| Commits con mensaje vacío o críptico (`fix`, `wip`, `asdf`) | Mensajes descriptivos con patrón `sesionXX:` |

---

## Ritual de fin de sesión (obligatorio)

Antes de cerrar el ordenador, **siempre**:

```bash
python -m pytest -q          # todos los tests pasan
git status                   # working tree clean
git push origin main         # código subido
```

Si hay cambios sin commitear al acabar la sesión, el compañero empezará la siguiente sin ellos.

---

## Flujo completo de una sesión — resumen visual

```
┌─────────────────────────────────────────────────────┐
│                  INICIO DE SESIÓN                   │
│              git pull origin main                   │
└───────────────────────┬─────────────────────────────┘
                        │
          ┌─────────────┴──────────────┐
          │  Miembro A                 │  Miembro B
          │  edita fichero_a.py        │  edita fichero_b.py
          │  git add fichero_a.py      │  git add fichero_b.py
          │  git commit -m "sesionXX"  │  git commit -m "sesionXX"
          │  git pull origin main      │  git pull origin main
          │  git push origin main      │  git push origin main
          └─────────────┬──────────────┘
                        │
┌───────────────────────┴─────────────────────────────┐
│                  FIN DE SESIÓN                      │
│   pytest -q  →  git status  →  git push origin main │
└─────────────────────────────────────────────────────┘
```

