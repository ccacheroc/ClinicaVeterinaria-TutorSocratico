---
applyTo: '**/*.py'
description: 'Reglas de arquitectura por capas del proyecto'
---

# Arquitectura por capas

## Capas y responsabilidades

| Capa | Carpeta | Responsabilidad |
|---|---|---|
| Dominio | `entities/` | Entidades, invariantes, reglas de negocio, `Resultado` |
| Servicios | `services/` | Orquestación de casos de uso; no hay I/O de consola |
| Interfaz | `ui/` | Entrada/salida de consola, menús, traducción de `Resultado` a mensajes |
| Persistencia | `persistence/` | Adaptadores de almacenamiento (JSON, Pickle, BD…) |

## Regla de dependencias (unidireccional)

```
ui  →  services  →  entities
                ↘  persistence
```

- `ui` **solo** importa de `services`. Prohibido `from entities import ...` en `ui/`.
- `services` importa de `entities` y de `persistence`.
- `entities` no importa de ninguna otra capa del proyecto.

## Contrato de errores: `Resultado`

Todas las operaciones que pueden fallar **deben** devolver `Resultado` en lugar de lanzar excepciones al exterior.

```python
# ✅ Correcto — devolver Resultado
def realizar_operacion(self, valor: float) -> Resultado:
    if valor <= 0:
        return Resultado.error("El valor debe ser positivo", "VALOR_INVALIDO")
    ...
    return Resultado.exito("Operación completada")

# ❌ Incorrecto — lanzar excepción desde dominio hacia servicios/ui
def realizar_operacion(self, valor: float) -> None:
    raise ValueError("valor inválido")
```

> **Ejemplo en Coches2026**: `Coche.avanzar(km)` devuelve `Resultado.error("SIN_COMBUSTIBLE")` en lugar de lanzar una excepción cuando no hay energía.

## Seed de datos

`services/seed_data_service.py` inserta datos de ejemplo al arrancar.
Se invoca desde `main.py` **antes** de lanzar el menú.
Las entidades desconocen que son "datos de seed".

## Añadir nueva funcionalidad — checklist

1. Invariante o regla → `entities/` (sin I/O).
2. Caso de uso → `services/` (método en el servicio adecuado).
3. Pantalla/menú → `ui/` (llama al servicio, muestra `Resultado.mensaje`).
4. Test → `tests/test_<capa>.py` con Given/When/Then.
