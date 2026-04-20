---
mode: 'agent'
description: 'Sesión 1 — Configurar Git y aprender el flujo de trabajo en equipo'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Actualmente estamos en la **Sesión 1** de la asignatura.
El objetivo de hoy es configurar Git correctamente y aprender el flujo de trabajo en equipo que usaremos durante todo el curso.

# TAREAS DE HOY (WORKFLOW)

1. Instalar Git y configurar identidad global:
   ```bash
   git config --global user.name "Nombre Apellido"
   git config --global user.email "correo@ejemplo.com"
   ```
2. Crear cuenta en GitHub (si no se tiene) y generar un token de acceso personal (PAT) o configurar SSH.
3. Hacer fork del repositorio plantilla de la asignatura.
4. Clonar el fork en local:
   ```bash
   git clone https://github.com/<usuario>/<proyecto>.git
   cd <proyecto>
   ```
5. Añadir el repositorio original como `upstream`:
   ```bash
   git remote add upstream https://github.com/<profesor>/<proyecto>.git
   ```
6. Practicar el ciclo básico: `add` → `commit` → `push`.
7. Abrir una Pull Request de prueba desde vuestra rama de trabajo hacia `main`.

# FLUJO DE RAMAS QUE USAREMOS EN TODO EL CURSO

```
main          ← rama estable; solo se actualiza con PR revisadas
└── sesionXX  ← rama de trabajo por sesión (ej. sesion02-clases)
```

Pasos para cada sesión:
```bash
git checkout main
git pull upstream main            # sincronizar con el repo del profesor
git checkout -b sesion02-clases   # crear rama de trabajo
# … trabajar …
git add .
git commit -m "sesion02: descripción corta de lo que se hace"
git push origin sesion02-clases
# abrir PR hacia main del propio fork
```

# REGLAS ESTRICTAS PARA HOY

- **Nunca** trabajar directamente en `main`.
- Los commits deben tener mensajes descriptivos en español: `"sesionXX: descripción corta"`.
- Cada miembro del equipo debe hacer al menos un commit hoy.
- No subir ficheros generados automáticamente (`.pyc`, `.venv/`, `__pycache__/`). Verificar que `.gitignore` los excluye.

# MODO TUTOR

Actúa como tutor: explica cada comando antes de ejecutarlo. No des todos los pasos de golpe; espera a que el alumno confirme que ha completado cada uno.

---

# ✅ DEFINITION OF DONE (DoD)

Antes de cerrar la sesión, verifica que se cumplen **todos** los criterios:

## Quality gates generales (aplican en todas las sesiones)
- [ ] La app (o el proyecto base) arranca sin errores
- [ ] Los commits del día siguen el patrón `sesionXX: descripción corta`
- [ ] No hay ficheros innecesarios subidos (`.venv/`, `__pycache__/`, `*.pyc`)
- [ ] Cada miembro del equipo tiene al menos un commit

## Quality gates específicos de esta sesión
- [ ] `git remote -v` muestra `origin` (fork propio) y `upstream` (repo del profesor)
- [ ] `git log --oneline` muestra al menos 1 commit propio con mensaje correcto
- [ ] `.gitignore` excluye `.venv/`, `__pycache__/` y `*.pyc`
- [ ] PR de prueba abierta en GitHub y visible en el repositorio

---

# 📓 JOURNAL DE SESIÓN

Al terminar, crea o actualiza el fichero `journal/sesion01.md` con el siguiente contenido rellenado y haz commit:

```markdown
# Journal — Sesión 01 — [fecha]

## Integrantes
-
-

## ¿Qué hemos hecho hoy?


## Decisiones tomadas (y por qué)
<!-- Ej: elegimos SSH en lugar de PAT porque... -->

## Problemas encontrados y cómo los resolvimos


## ¿Qué queda pendiente para la próxima sesión?


## Tiempo invertido
- Horas de trabajo en equipo:
```

```bash
git add journal/sesion01.md
git commit -m "sesion01: journal de sesión"
git push origin sesion01-git
```
