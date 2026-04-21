---
mode: 'agent'
description: 'Sesión 3 — Crear Resultado, añadir métodos de instancia y de clase a las entidades'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 3** de la asignatura.
El objetivo de hoy es dos cosas:
1. Crear `Resultado` — la clase de comunicación entre capas — y explicar su motivación.
2. Enriquecer las entidades con **métodos de instancia y de clase** que usen `Resultado`.

> 🔄 **Antes de empezar**: `git pull origin main` para tener el código actualizado.

---

# FASE 0 — CREAR `Resultado` (responsabilidad exclusiva del agente)

Antes de añadir ningún método, el agente explica al alumno por qué se necesita esta clase
y la crea íntegramente. El alumno **no la implementa** — solo la comprende.

## Paso 0.1 — El agente explica la motivación

> *"Fijaos en que nuestras entidades van a tener operaciones que pueden salir bien o mal.
> Por ejemplo, 'registrar un animal' puede fallar si el nombre está vacío; 'añadir una
> afección' puede fallar si ya existe.*
>
> *¿Cómo comunicamos ese fallo al servicio, y el servicio a la UI?*
>
> *Una opción sería lanzar una excepción. Pero las excepciones están pensadas para
> situaciones inesperadas — bugs, fallos de red, errores de programación. Que un nombre
> esté vacío no es un bug: es un caso de uso normal que hay que tratar con lógica ordinaria.*
>
> *Otra opción sería devolver `None` o un booleano. Pero entonces perdemos el mensaje
> de error: ¿cómo sabe la UI qué decirle al usuario?*
>
> *La solución es una clase auxiliar — no pertenece al dominio del negocio, sino a la
> infraestructura de comunicación entre capas — que envuelve el resultado de cualquier
> operación: si fue bien (`ok=True`) con el dato o mensaje de retorno, o si fue mal
> (`ok=False`) con el motivo del error y un código identificador.*
>
> *Esta clase se llama `Resultado`. No representa ningún concepto de vuestro dominio
> — es una convención técnica que usaréis en absolutamente todos los métodos de negocio
> del proyecto. La creo yo ahora para que podáis concentraros en implementar los métodos."*

Preguntar al alumno si ha entendido la motivación antes de continuar:

> *"¿Tiene sentido por qué usamos `Resultado` en lugar de lanzar excepciones o devolver None?
> ¿Tenéis alguna duda antes de ver el código?"*

## Paso 0.2 — El agente crea `src/entities/resultado.py`

```python
class Resultado:
    """Envuelve el resultado de cualquier operación que puede fallar.

    No es una clase de dominio: es una utilidad de comunicación entre capas.
    Toda operación de negocio que puede fallar debe devolver Resultado
    en lugar de lanzar una excepción o devolver None.

    Uso:
        return Resultado.exito("Operación completada")
        return Resultado.error("El nombre no puede estar vacío", "NOMBRE_VACIO")
    """

    def __init__(self, ok, mensaje, codigo=None, valor=None):
        self.ok = ok
        self.mensaje = mensaje
        self.codigo = codigo   # código corto para identificar el tipo de error
        self.valor = valor     # dato de retorno opcional en caso de éxito

    @classmethod
    def exito(cls, mensaje, valor=None):
        """Crea un Resultado de éxito con mensaje y dato de retorno opcional."""
        return cls(True, mensaje, valor=valor)

    @classmethod
    def error(cls, mensaje, codigo=None):
        """Crea un Resultado de error con mensaje y código identificador."""
        return cls(False, mensaje, codigo=codigo)
```

Tras crearla, mostrar al alumno un ejemplo de uso adaptado a su dominio concreto:

```python
# En una entidad (ejemplo adaptado al dominio del alumno):
def anadir_afeccion(self, afeccion):
    if not afeccion:
        return Resultado.error("La afección no puede estar vacía", "AFECCION_VACIA")
    if afeccion in self.__afecciones:
        return Resultado.error("La afección ya existe", "AFECCION_DUPLICADA")
    self.__afecciones.append(afeccion)
    return Resultado.exito(f"Afección '{afeccion}' añadida")

# En la UI (adelanto de cómo se usará):
resultado = servicio.anadir_afeccion(animal, "diabetes")
if resultado.ok:
    print(f"✅ {resultado.mensaje}")
else:
    print(f"❌ {resultado.mensaje}")
```

Aplicar la plantilla de verificación:

```
🔍 Acabo de crear src/entities/resultado.py.
   Por favor, ábrelo y comprueba que:
   - Existen los métodos de clase Resultado.exito y Resultado.error.
   - Los atributos ok, mensaje, codigo y valor son públicos (sin guiones).
   ¿Tiene sentido la clase? ¿Alguna duda antes de usarla en los métodos?
```

---

# TAREAS DE HOY (WORKFLOW)

1. Revisar el diagrama de clases actual e identificar qué comportamientos faltan.
2. Añadir **métodos de instancia** a cada entidad que implementen las operaciones del dominio.
3. Añadir **métodos de clase** donde aplique (operaciones sobre el estado compartido de la clase).
4. Todas las operaciones que pueden fallar devuelven `Resultado`. Ver `instructions/architecture.instructions.md`.
5. Actualizar el diagrama Mermaid en `README.md`.
6. Escribir/ampliar tests con Given/When/Then para cada método nuevo.

# REGLAS ESTRICTAS PARA HOY

- Ningún método en `entities/` puede contener `print()` ni `input()`.
- Los métodos de clase se decoran con `@classmethod` y reciben `cls` como primer parámetro.
- No añadir herencia todavía (es Sesión 4).
- `Resultado` es obligatorio para toda operación que pueda fallar.

# MODO TUTOR

Muestra un método de instancia de la clase principal como ejemplo. Luego pide al alumno que implemente los métodos de las demás clases antes de mostrar la solución.

---

# ✅ DEFINITION OF DONE (DoD)

## Quality gates generales (aplican en todas las sesiones)
- [ ] `python -m pytest -q` → 0 fallos, 0 errores
- [ ] `python main.py` arranca sin errores
- [ ] No hay imports de `entities/` en `ui/`: `grep -r "from entities" ui/` → vacío
- [ ] Commits del día con patrón `sesion03: descripción corta`

## Quality gates específicos de esta sesión
- [ ] `src/entities/resultado.py` creado por el agente con `Resultado.exito` y `Resultado.error`, y el alumno ha confirmado que entiende su propósito
- [ ] Cada entidad tiene al menos un método de instancia que implementa una operación del dominio
- [ ] Toda operación que puede fallar devuelve `Resultado` (ninguna lanza excepción al exterior)
- [ ] Ningún método en `entities/` contiene `print()` ni `input()`: `grep -rn "print\|input" entities/`
- [ ] Métodos de clase decorados con `@classmethod` donde aplique
- [ ] Tests Given/When/Then escritos para cada método nuevo (happy path + error de dominio)
- [ ] Diagrama de clases actualizado en `README.md` con los métodos nuevos

---

# 📓 JOURNAL DE SESIÓN

Al terminar, crea o actualiza `journal/sesion03.md` y haz commit:

```markdown
# Journal — Sesión 03 — [fecha]

## Integrantes
-
-

## ¿Qué hemos hecho hoy?


## Métodos implementados por clase
<!-- Lista los métodos añadidos a cada clase y su propósito -->

## Decisiones de diseño tomadas (y por qué)
<!-- Ej: decidimos que X devuelve Resultado en lugar de lanzar excepción porque... -->

## Problemas encontrados y cómo los resolvimos


## ¿Qué queda pendiente para la próxima sesión?


## Tiempo invertido
- Horas de trabajo en equipo:
```

```bash
git add journal/sesion03.md
git commit -m "sesion03: journal de sesión"
git push origin main
```
