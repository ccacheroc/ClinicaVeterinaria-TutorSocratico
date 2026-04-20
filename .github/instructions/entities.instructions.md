---
applyTo: 'entities/**/*.py'
description: 'Reglas de la capa de dominio: arquitectura, visibilidad, properties y setters'
---

# Reglas — Capa `entities/`

## Responsabilidad

Esta capa contiene el **modelo de dominio puro**: entidades, invariantes y reglas de negocio.
No tiene dependencias con ninguna otra capa del proyecto.

## Prohibiciones absolutas

- ❌ `print()`, `input()` o cualquier I/O de consola.
- ❌ Acceso a ficheros, red o base de datos.
- ❌ Importar desde `services/`, `ui/` o `persistence/`.
- ❌ Atributos de instancia públicos sin pasar por `@property`.

---

## Diseño OO — Visibilidad, Properties y Setters

### Principio fundamental

> **Ocultar la implementación, exponer el comportamiento.**
> (Principio de encapsulación — Parnas, 1972; reforzado en "Clean Code" y "SOLID".)

Un atributo nunca debe ser público por comodidad. Debe ser público solo si forma parte intencional de la interfaz de la clase.

### `__doble_guion` → Privado (name-mangling)

Usar cuando:
- El atributo es un **detalle de implementación** que no debe ser accedido ni sobrescrito por subclases.
- Su modificación directa rompería invariantes del objeto.
- Es la opción **por defecto** en `entities/`.

```python
# Ejemplo genérico
class Entidad:
    def __init__(self, identificador: str) -> None:
        if not identificador:
            raise ValueError("El identificador no puede estar vacío")
        self.__identificador: str = identificador   # ← privado
        self.__estado: float = 0.0                  # ← privado

# Ejemplo en Coches2026
class Coche(ABC):
    def __init__(self, matricula: str, marca: str) -> None:
        self.__matricula: str = matricula
        self.__kilometros_recorridos: float = 0.0
```

### `_un_guion` → Protegido (convención)

Usar **solo** cuando una subclase necesita leerlo o modificarlo directamente y añadir una `@property` sería artificialmente verboso.
Documentar siempre el motivo.

```python
# Ejemplo en Coches2026: _gasolina es accesible por CocheHibrido
class CocheCombustion(Coche):
    def __init__(self, ...) -> None:
        self._gasolina: float = 0.0  # accesible por subclase CocheHibrido
```

### Sin guion → Público

Usar únicamente para:
- Constantes de clase que son parte de la API pública.
- Atributos de objetos de datos simples (ej. `Resultado`) donde la transparencia es deliberada.

### Cuándo añadir `@property` (lectura)

Añadir `@property` cuando:
1. El atributo forma parte de la **interfaz observable** de la entidad.
2. Otra capa (`services`, `ui`) necesita leerlo para mostrar información.
3. Podría requerir lógica en el futuro (cálculo derivado, logging, lazy init).

```python
# Ejemplo genérico
@property
def identificador(self) -> str:
    """Identificador único de la entidad (solo lectura)."""
    return self.__identificador

# Ejemplo en Coches2026
@property
def matricula(self) -> str:
    return self.__matricula
```

**No añadir `@property`** si el atributo es un detalle interno que nunca sale de la clase.

### Cuándo añadir setter (`@xxx.setter`)

Añadir setter **solo** si se cumplen **las dos** condiciones:
1. La mutación es parte explícita del **dominio**.
2. Hay **lógica de validación** que debe ejecutarse al asignar.

```python
# Ejemplo genérico
@recurso.setter
def recurso(self, nuevo: "Recurso | None") -> None:
    """Asigna un recurso; None indica ausencia de recurso."""
    self.__recurso = nuevo

# Ejemplo en Coches2026
@coche.setter
def coche(self, nuevo_coche: "Coche | None") -> None:
    self.__coche = nuevo_coche
```

**No añadir setter** si:
- El valor se establece solo en `__init__` y no cambia.
- La mutación se hace a través de un método de dominio con nombre explícito.

### Resumen rápido de visibilidad

| Situación | Solución |
|---|---|
| Atributo interno, no sale de la clase | `self.__atributo` (privado, sin property) |
| Atributo que services/ui necesita leer | `self.__atributo` + `@property` de lectura |
| Atributo mutable con validación de dominio | `self.__atributo` + `@property` + `@xxx.setter` |
| Subclase necesita acceso directo | `self._atributo` (protegido, documentar motivo) |
| API pública deliberada / constante | sin guion |

---

## Contrato de errores

Toda operación que puede fallar por **lógica de negocio** devuelve `Resultado`:

```python
# Ejemplo genérico
def ejecutar(self, cantidad: float) -> Resultado:
    if cantidad <= 0:
        return Resultado.error("La cantidad debe ser positiva", "CANTIDAD_INVALIDA")
    ...
    return Resultado.exito("Ejecutado correctamente")

# Ejemplo en Coches2026
def avanzar(self, km: float) -> Resultado:
    if km <= 0:
        return Resultado.error("Los km deben ser positivos", "KM_INVALIDOS")
    ...
    return Resultado.exito(f"Avanzado {km} km")
```

Las excepciones (`ValueError`, clases propias de `excepciones.py`) se reservan para **invariantes de construcción** (datos inválidos que son un bug del llamador, no un flujo de negocio esperado).

---

## Atributos de clase

Usar `ClassVar` y documentar su propósito:

```python
from typing import ClassVar

class Entidad:
    _contador_global: ClassVar[int] = 0  # compartido por todas las instancias

# Ejemplo en Coches2026
class Coche(ABC):
    __km_por_marca: ClassVar[dict[str, float]] = {}
```

## Type hints

Obligatorios en todas las firmas públicas. Usar `X | None` (nunca `Optional[X]`).

## Clases abstractas

Usar `ABC` y `@abstractmethod` para los métodos que cada subclase debe implementar obligatoriamente.

```python
from abc import ABC, abstractmethod

class EntidadBase(ABC):
    @abstractmethod
    def ejecutar(self, cantidad: float) -> Resultado: ...

# Ejemplo en Coches2026: Coche es abstracta, avanzar() es abstractmethod
```

## Herencia múltiple

Si el proyecto requiere herencia múltiple, documentar el MRO elegido con un comentario:

```python
# Ejemplo en Coches2026
# MRO: CocheHibrido → CocheElectrico → CocheCombustion → Coche
class CocheHibrido(CocheElectrico, CocheCombustion):
    ...
```
