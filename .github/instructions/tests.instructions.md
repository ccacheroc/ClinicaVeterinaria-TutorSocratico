---
applyTo: 'tests/**/*.py'
description: 'Reglas de la capa de tests'
---

# Reglas — Capa `tests/`

## Responsabilidad

Los tests validan el comportamiento del sistema capa por capa.
Cada fichero de test corresponde a un módulo concreto del proyecto.

## Estructura de ficheros

| Fichero | Qué prueba |
|---|---|
| `tests/test_entities.py` | Entidades y reglas de negocio (sin mocks) |
| `tests/test_<nombre>_service.py` | Cada servicio de la capa `services/` |
| `tests/test_seed_data_service.py` | Servicio de seed de datos |
| `tests/test_ui_menu.py` | Capa UI (con servicios mockeados) |

> **Ejemplo en Coches2026**: `test_gestion_concesionario_service.py`, `test_gestion_personas_service.py`.

## Estructura obligatoria de cada test

```python
def test_nombre_descriptivo_del_escenario():
    # Given — estado inicial / contexto
    entidad = MiEntidad("id-001", "dato")
    entidad.preparar(10.0)

    # When — acción bajo prueba
    resultado = entidad.ejecutar(5)

    # Then — verificaciones
    assert resultado.ok is True
    assert entidad.estado == 5.0
```

## Reglas por tipo de test

### Tests de entidades (`test_entities.py`)
- **Sin mocks**. Instanciar directamente la clase y verificar comportamiento.
- Cubrir: happy path + error de dominio + edge case (valor límite 0, negativo, etc.).

### Tests de servicios
- Mockear dependencias externas si las hubiera (repositorios de persistencia).
- No mockear entidades — usar instancias reales.

### Tests de UI (`test_ui_menu.py`)
- Mockear los servicios con `unittest.mock.MagicMock`.
- **Prohibido** importar o instanciar entidades aquí.
- Usar `patch("builtins.input", side_effect=[...])` para simular entradas del usuario.

```python
from unittest.mock import MagicMock, patch
from entities.resultado import Resultado
from ui.menu import MenuCLI

def test_menu_registrar_entidad_exitoso():
    # Given
    servicio_mock = MagicMock()
    servicio_mock.registrar.return_value = Resultado.exito("Entidad registrada")
    menu = MenuCLI(servicio_mock)

    # When / Then
    with patch("builtins.input", side_effect=["1", "id-001", "dato", "0"]):
        with patch("builtins.print") as mock_print:
            menu.iniciar()
            salidas = " ".join(str(c) for c in mock_print.call_args_list)
            assert "Entidad registrada" in salidas
```

> **Ejemplo en Coches2026**: `test_menu_alta_cliente_exitosa()` en `test_ui_menu.py`.

## Ejecución

```bash
python -m pytest -q                       # todos los tests
python -m pytest tests/test_entities.py -v  # solo entidades
python -m pytest -k "registrar" -v         # filtrar por nombre
```

## Nombrado de tests

Patrón: `test_<clase_o_función>_<escenario_en_snake_case>`

```
# Genérico
test_entidad_ejecutar_sin_recursos_devuelve_error
test_servicio_registrar_identificador_duplicado_devuelve_error
test_menu_listar_llama_al_servicio

# Ejemplo en Coches2026
test_coche_combustion_avanzar_sin_gasolina_devuelve_error
test_concesionario_anadir_cliente_dni_duplicado_devuelve_error
```
