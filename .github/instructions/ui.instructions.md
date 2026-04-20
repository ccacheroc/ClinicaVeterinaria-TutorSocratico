---
applyTo: 'ui/**/*.py'
description: 'Reglas de la capa de interfaz de usuario (UI/CLI)'
---

# Reglas — Capa `ui/`

## Responsabilidad

Esta capa es la **única** que interactúa con el usuario: recibe entradas por consola y muestra resultados.
Traduce las acciones del usuario en llamadas a `services/` y convierte `Resultado` en mensajes legibles.

## Dependencias permitidas

- ✅ Importar desde `services/`.
- ❌ **Prohibido importar desde `entities/`** — ni clases, ni tipos, ni constantes.
- ❌ No instanciar entidades directamente.

## Patrón de llamada a servicios

```python
# ✅ Correcto: la UI llama al servicio y muestra el mensaje de Resultado
resultado = self.__servicio.registrar(identificador, datos)
if resultado.ok:
    print(f"✅ {resultado.mensaje}")
else:
    print(f"❌ {resultado.mensaje}")

# ❌ Incorrecto: la UI instancia entidades directamente
from entities.mi_entidad import MiEntidad   # PROHIBIDO
obj = MiEntidad(identificador)
```

> **Ejemplo en Coches2026**: `ui/menu.py` llama a `GestionConcesionarioService.registrar_coche()`
> y nunca importa `CocheCombustion` ni `Persona` directamente.

## Estructura del menú

- Clase de menú (`MenuCLI` o similar) con inyección de dependencias de servicios en `__init__`.
- Método `iniciar()` como punto de entrada del bucle principal.
- Cada opción de menú tiene su propio método privado (`__alta_entidad`, `__listar`, etc.).
- Usar `try/except` solo para capturar excepciones de construcción que los servicios no hayan podido interceptar.

```python
class MenuCLI:
    def __init__(self, servicio_a: ServicioA, servicio_b: ServicioB) -> None:
        self.__sa = servicio_a
        self.__sb = servicio_b

    def iniciar(self) -> None:
        """Arranca el bucle principal del menú."""
        ...
```

## Entrada de datos

- Validar formato básico en la UI (campo vacío, tipo de dato).
- Validar **lógica de negocio** en `entities/` o `services/`, nunca en `ui/`.
- Usar `input().strip()` siempre para evitar espacios accidentales.

## Mostrar objetos

Llamar siempre a `str(objeto)` o `resultado.mensaje`.
No acceder a propiedades internas de las entidades directamente desde `ui/`.
