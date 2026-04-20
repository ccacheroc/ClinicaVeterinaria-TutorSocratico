---
mode: 'agent'
description: 'Sesión 12 — Crear un ejecutable distribuible con PyInstaller'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 12** de la asignatura.
El objetivo de hoy es crear un **ejecutable distribuible** de la aplicación.

# TAREAS DE HOY (WORKFLOW)

1. Instalar `PyInstaller`:
   ```bash
   pip install pyinstaller
   ```
2. Generar el ejecutable en modo `--onefile`:
   ```bash
   pyinstaller --onefile main.py --name nombre-del-proyecto
   ```
3. Verificar que el ejecutable funciona correctamente:
   ```bash
   ./dist/nombre-del-proyecto      # macOS/Linux
   dist\nombre-del-proyecto.exe    # Windows
   ```
4. Añadir al `.gitignore` los artefactos generados:
   ```gitignore
   dist/
   build/
   *.spec
   ```
5. Documentar en `README.md` cómo generar y ejecutar el binario.
6. (Opcional) Configurar el fichero `.spec` para incluir recursos adicionales.

# CONSIDERACIONES

Si la app usa ficheros de datos (pickle/JSON), los paths deben ser relativos al directorio de ejecución, no al directorio del script. Usar `pathlib.Path`:

```python
from pathlib import Path
BASE_DIR = Path(__file__).parent
DATOS_PATH = BASE_DIR / "datos" / "entidades.json"
```

En ejecutables `--onefile`, `__file__` apunta a un directorio temporal. Usar `sys._MEIPASS` si es necesario acceder a recursos empaquetados.

# REGLAS ESTRICTAS PARA HOY

- No subir `dist/` ni `build/` al repositorio.
- El ejecutable debe funcionar sin tener Python instalado en la máquina destino.
- Todos los tests deben pasar antes de generar el ejecutable.

# MODO TUTOR

Guía al alumno paso a paso. Muestra el comando de PyInstaller y pide que lo ejecuten, luego comprueben juntos que el binario arranca correctamente.
