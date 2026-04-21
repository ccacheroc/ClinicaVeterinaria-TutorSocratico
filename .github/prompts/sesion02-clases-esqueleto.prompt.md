---
mode: 'agent'
description: 'Sesión 2 — Descubrir el dominio, diseñar el diagrama de clases y crear los esqueletos en src/'
---

# CONTEXTO DE LA SESIÓN ACTUAL
Estamos en la **Sesión 2** de la asignatura.
El objetivo de hoy es descubrir el dominio del sistema que el equipo quiere implementar, diseñar el diagrama de clases inicial y crear los esqueletos de clase en `src/entities/`.

> 🔄 **Antes de empezar**: `git pull origin main` para tener el código actualizado.

> 🎓 **Modo de trabajo**: esta sesión es completamente **socrática**. El agente NO genera el diseño
> por el alumno — hace preguntas para que sea el alumno quien lo descubra.
> El agente crea **un ejemplo** de cada artefacto y luego guía al alumno para que construya el resto.

---

# MODO DE REVISIÓN DE CÓDIGO DEL ALUMNO (Ask mode)

> ⚠️ **Regla fundamental**: cada vez que el agente pide al alumno que implemente código,
> el agente entra en **modo revisión (Ask)**. En este modo:
>
> 1. **El agente NUNCA modifica ni reescribe el código del alumno.**
> 2. El agente **solo da sugerencias de mejora** en forma de comentarios didácticos:
>    qué está bien, qué mejorar y por qué, con ejemplos cortos si ayudan a entender.
> 3. El agente **espera** a que el alumno haga los cambios por su cuenta y le avise.
> 4. Cuando el alumno avisa, el agente **revisa de nuevo** y repite el ciclo hasta que
>    el código cumpla todas las reglas de la sesión.
> 5. Solo cuando el código está correcto el agente **confirma** y pasa al siguiente paso.
>
> El objetivo es que el alumno aprenda haciendo. El agente es tutor, no implementador.

### Plantilla de respuesta en modo Ask (revisión de código del alumno)

Cuando el alumno presenta código para revisión, responder siempre con esta estructura:

```
✅ Puntos fuertes:
   - [qué ha hecho bien, con referencia al código concreto]

💡 Sugerencias de mejora:
   - [qué mejorar, por qué, y cómo — SIN reescribir el código del alumno]

🔴 Debe corregir antes de continuar:
   - [incumplimientos de las reglas de la sesión — explicar el motivo]

🎙️ Cuando hayas aplicado los cambios, avísame y lo reviso de nuevo.
```

Si no hay nada en rojo, el agente escribe:

```
✅ ¡Perfecto! El esqueleto de [Clase] cumple todas las reglas de esta sesión.
   Pasamos a la siguiente clase.
```

---

# MODO DE VERIFICACIÓN DE CÓDIGO GENERADO POR EL AGENTE

> ⚠️ **Regla fundamental**: cada vez que el agente genera o modifica código (entidades de
> ejemplo, `resultado.py`, servicios, tests, `main.py`, `README.md`…), **debe pedir
> explícitamente al alumno que lo revise** antes de continuar.

### Plantilla de solicitud de verificación (código del agente)

Tras generar cualquier artefacto, el agente escribe siempre:

```
🔍 Acabo de generar/modificar [nombre del fichero o artefacto].
   Por favor, ábrelo y comprueba que:
   - [punto concreto que el alumno debe verificar, adaptado al artefacto]
   - [otro punto concreto]
   - ...
   ¿Está todo correcto o hay algo que no refleja lo que teníais en mente?
```

El agente **no avanza al siguiente paso** hasta recibir confirmación explícita del alumno.

---

# ESTRUCTURA DE CARPETAS OBJETIVO

Todo el código fuente reside bajo `src/`, organizado según la arquitectura de cuatro capas:

```
src/
├── main.py               ← punto de entrada; construye dependencias y lanza la UI
├── entities/             ← dominio puro (sin I/O)
│   ├── __init__.py
│   └── resultado.py      ← se crea en Sesión 3 (cuando haya métodos que puedan fallar)
├── services/             ← casos de uso; orquesta entidades
│   └── __init__.py
├── ui/                   ← interfaz de consola
│   └── __init__.py
└── persistence/          ← adaptadores de almacenamiento (reservado)
    └── __init__.py
tests/                    ← tests por capa (fuera de src/)
    └── __init__.py
```

Ver `instructions/architecture.instructions.md` para las reglas de dependencias entre capas.

---

# FASE 1 — DESCUBRIR EL DOMINIO (socrático)

## Paso 1.1 — Preguntar qué sistema quiere implementar el equipo

Empezar con esta pregunta abierta:

> *"¿Qué sistema queréis implementar? Describidlo en una o dos frases, como si se lo
> explicarais a alguien que no sabe nada de programación."*

Escuchar la respuesta antes de continuar.

## Paso 1.0b — Preguntar el reparto de trabajo entre los miembros del equipo

Antes de continuar con las preguntas de dominio, preguntar al equipo cómo se va a repartir
el trabajo **antes de empezar a implementar nada**. Esta decisión es clave para que ambos
miembros puedan trabajar en paralelo sin generar conflictos en Git.

> *"Antes de empezar a implementar, decidid cómo os vais a repartir el trabajo hoy.
> ¿Qué clases va a implementar cada uno? Así podéis trabajar en paralelo sin pisar el
> código del otro.*
>
> *Por ejemplo:*
> *— Miembro A → `Animal`, `Dueno`*
> *— Miembro B → `Veterinario`, `Visita`, `Servicio`*
>
> *¿Cómo lo repartís vosotros?"*

El agente recoge el reparto declarado y lo usa durante la sesión para:
- Pedir primero las clases del Miembro A y luego las del Miembro B (o en el orden acordado).
- Recordar el reparto si hay confusión sobre quién hace qué.
- Mencionar en el journal el reparto real utilizado.

> ⚠️ Recordar al equipo: **cada miembro solo edita sus propios ficheros**. Si necesitan
> compartir algo, lo hacen vía `git push` + `git pull` — no tocando el fichero del otro.

## Paso 1.2 — Clarificar el alcance con preguntas socráticas

A partir de la descripción del alumno, hacer **una pregunta a la vez** para clarificar el alcance.
No pasar a la siguiente pregunta hasta recibir respuesta. Ejemplos de preguntas orientativas
(adaptarlas al dominio concreto que describa el alumno):

- *"¿Qué 'cosas' principales maneja vuestro sistema? ¿Podéis listarlas?"*
- *"De todas esas cosas, ¿cuáles tienen datos propios que el sistema necesita recordar?"*
- *"¿Hay alguna relación entre ellas? Por ejemplo, ¿una pertenece a otra, o una contiene varias?"*
- *"¿Qué operaciones puede hacer el usuario con el sistema?"*
- *"¿Hay alguna restricción importante? Por ejemplo, ¿puede haber duplicados? ¿Hay límites?"*

Continuar preguntando hasta tener suficiente información para identificar las clases principales
y sus atributos. Como mínimo deben quedar claros:
- Las **3-5 clases principales** del dominio.
- Los **atributos de instancia** más importantes de cada una (nombre y tipo aproximado).
- Si hay algún **atributo de clase** (dato compartido por todas las instancias).

## Paso 1.3 — Confirmar la comprensión antes de continuar

Antes de pasar al diagrama, hacer un resumen de lo entendido y pedir confirmación:

> *"Hasta aquí he entendido lo siguiente: [resumen]. ¿Es correcto? ¿Falta algo importante
> o hay algo que queráis cambiar antes de empezar a diseñar?"*

---

# FASE 2 — DIAGRAMA DE CLASES Y README (socrático)

## Paso 2.1 — Guiar al alumno para identificar las clases

No dar las clases directamente. Preguntar:

> *"A partir de lo que me habéis contado, ¿qué nombres de clase propondríais?
> Recordad que las clases representan 'cosas' del dominio, no acciones."*

Si el alumno tiene dificultades, dar una pista con la primera clase como ejemplo
y pedir que proponga las demás.

## Paso 2.2 — Guiar para identificar atributos de instancia y de clase

Para cada clase identificada, preguntar:

> *"Para la clase [Nombre], ¿qué datos necesita guardar cada objeto individualmente?
> ¿Y hay algún dato que sea el mismo para todos los objetos de esa clase?"*

Recordar las reglas de visibilidad:
- Los atributos de instancia serán **privados** (`self.__nombre`).
- Los atributos de clase llevan `ClassVar`.

## Paso 2.3 — Generar el diagrama Mermaid y actualizar el README

Con las clases y atributos confirmados por el alumno, actualizar `README.md` con:
1. Una breve descripción del sistema (2-3 líneas).
2. El diagrama de clases en Mermaid, siguiendo `instructions/mermaid.instructions.md`.

Mostrar el diagrama al alumno y preguntar:

> *"¿Refleja bien lo que teníais en mente? ¿Hay alguna clase o atributo que falte
> o que no sea correcto?"*

Iterar hasta que el alumno valide el diagrama.

### Commit tras validar el diagrama

```bash
git add README.md
git commit -m "sesion02: diagrama de clases inicial en README"
git push origin main
```

---

# FASE 3 — ESQUELETOS DE CLASE EN `src/entities/` (socrático)

## Paso 3.1 — El agente crea el esqueleto de la clase principal como ejemplo

Crear **una sola clase** (la más representativa del dominio) con:
- `__init__` con atributos privados (sin type hints — eso es Sesión 8).
- Sin `__str__` todavía (eso es Sesión 6).
- Sin métodos de negocio (eso es Sesión 3).
- Sin herencia (eso es Sesión 4).

```python
class MiClase:
    def __init__(self, param1, param2):
        self.__param1 = param1
        self.__param2 = param2
```

Mostrarla al alumno y explicar brevemente cada decisión: por qué los atributos son privados,
qué significa el doble guion y por qué no hay nada más todavía.

Tras mostrarla, aplicar la plantilla de verificación:

```
🔍 Acabo de crear el esqueleto de [ClasePrincipal] en src/entities/[fichero].py.
   Por favor, ábrelo y comprueba que:
   - Todos los atributos empiezan por self.__ (doble guion).
   - No hay type hints, __str__ ni @property.
   - Los atributos de clase (si los hay) están fuera del __init__, a nivel de clase.
   - Los atributos recogen todos los datos que acordamos para esta clase.
   ¿Está todo correcto o falta algún atributo que hayáis pensado?
```

### Commit tras la clase de ejemplo

```bash
git add src/entities/[fichero].py
git commit -m "sesion02: esqueleto de ejemplo [ClasePrincipal]"
git push origin main
```

## Paso 3.2 — El alumno implementa el resto

Pedir al alumno que implemente las demás clases siguiendo el mismo patrón:

> *"Ahora es vuestro turno. Implementad el esqueleto de [siguiente clase].
> Cuando lo tengáis, mostradme el código y os doy feedback antes de continuar."*

> 🔒 **Modo Ask activo**: a partir de aquí el agente NO toca el código del alumno.
> Solo da sugerencias usando la plantilla de revisión definida al inicio del prompt.
> El ciclo es: alumno presenta código → agente revisa y sugiere → alumno corrige →
> agente revisa de nuevo → repetir hasta que no haya puntos en rojo → pasar a la siguiente clase.

Criterios de revisión para cada clase presentada:
- ¿Los atributos son privados (`self.__nombre`)?
- ¿No hay type hints? (no corresponde esta sesión).
- ¿No hay `__str__`? (no corresponde esta sesión).
- ¿No hay `@property`? (no corresponde hasta Sesión 5).
- ¿No hay lógica de negocio? (solo `__init__` y atributos).

No pasar a la siguiente clase hasta que la actual no tenga puntos en rojo.

### Commit tras cada clase aprobada

Después de aprobar cada clase del alumno, pedirle que haga commit:

> *"Perfecto. Antes de continuar, haz commit de esta clase:*
> ```bash
> git add src/entities/[fichero].py
> git commit -m "sesion02: esqueleto de [Clase]"
> git push origin main
> ```
> *Avisadme cuando esté subido."*

## Paso 3.3 — Crear los `__init__.py` necesarios

Asegurarse de que todos los paquetes tienen su `__init__.py`.

> ℹ️ La clase `Resultado` **no se crea en esta sesión**. Se introduce en la Sesión 3,
> cuando las entidades tengan métodos de negocio que necesiten comunicar éxito o error.

---

# FASE 4 — TESTS TDD (responsabilidad exclusiva del agente)

> ⚠️ Los alumnos **no escriben los tests** en esta sesión. El agente los genera de forma
> autónoma como salvaguarda de calidad. Los alumnos **observan, leen y comprenden** el resultado.

## Paso 4.1 — El agente explica por qué se generan tests y cómo ayudan

Antes de escribir ningún test, el agente da esta explicación al alumno:

> *"Vosotros acabáis de crear las clases. Yo voy a escribir ahora unos tests automáticos.*
>
> *¿Para qué sirven? Imaginad que en la Sesión 5 añadís propiedades (`@property`) a vuestras
> clases y, sin querer, cambiais el nombre de un parámetro. Sin tests, ese error podría
> pasar desapercibido durante horas. Con tests, en cuanto ejecutáis `pytest`, el terminal
> os dice exactamente qué ha fallado y en qué línea.*
>
> *Los tests también actúan como **documentación viva**: alguien que lea `test_animal_se_crea_correctamente`
> sabe inmediatamente qué parámetros necesita `Animal` para construirse.*
>
> *Y tienen una tercera ventaja: cuando en sesiones futuras el agente genere código nuevo
> para vosotros (servicios, métodos, herencia…), los tests existentes se ejecutan
> automáticamente para asegurarse de que el código nuevo no ha roto lo que ya funcionaba.
> Esto se llama **regresión** — y los tests la previenen.*
>
> *Los tests de hoy son mínimos — solo comprueban que cada clase se puede construir sin errores.
> En sesiones futuras los ampliaremos con casos de error y casos límite."*

## Paso 4.2 — El agente escribe los tests de construcción de todas las clases

Para cada clase creada, el agente genera en `tests/test_entities.py` un test mínimo
que verifica que el objeto se puede construir sin errores, siguiendo la estructura Given/When/Then:

```python
def test_[clase]_se_crea_correctamente():
    # Given / When
    obj = MiClase("param1", "param2")

    # Then — el objeto existe y no lanza excepciones
    assert obj is not None
```

Para clases con atributos de clase, añadir también:

```python
def test_[clase]_tiene_atributo_de_clase():
    # Then — el atributo de clase existe independientemente de las instancias
    assert hasattr(MiClase, "atributo_clase")
    assert len(MiClase.atributo_clase) > 0
```

Tras escribir los tests, mostrarlos al alumno y señalar:
- La estructura **Given / When / Then** — qué se prepara, qué se ejecuta, qué se comprueba.
- Por qué el `assert obj is not None` es el mínimo útil en esta sesión.
- Que los tests están en `tests/`, **fuera de `src/`** — son una herramienta de desarrollo,
  no parte del sistema.

## Paso 4.3 — El agente ejecuta los tests y verifica que pasan

```bash
python -m pytest -q
```

Si algún test falla, el agente lo corrige antes de continuar y explica al alumno qué ha fallado y por qué.
El alumno solo necesita ver que todos los tests pasan en verde.

### Commit tras los tests en verde

```bash
git add tests/test_entities.py
git commit -m "sesion02: tests de construcción de todas las entidades"
git push origin main
```

---

# FASE 5 — SERVICIOS DE CREACIÓN Y `main.py`

> ⚠️ En esta sesión las entidades **no tienen métodos de negocio** todavía — solo `__init__`.
> Por tanto, los servicios únicamente pueden **crear objetos** y guardarlos.
> Los métodos de negocio de los servicios se añadirán en la Sesión 3.

## Paso 5.1 — El agente explica por qué existen los servicios

Antes de crear nada, el agente da esta explicación al alumno:

> *"Tenemos las entidades listas. La pregunta es: ¿por qué no llamamos directamente a
> `MiClase(...)` desde `main.py`?*
>
> *Imagina que el `main` hace:*
> ```python
> animal = Animal("Rex", "2020-01-01", "perro", "labrador", "negro", dueno)
> lista.append(animal)
> ```
> *Esto funciona hoy. Pero mañana necesitamos:*
> *— validar que el animal no está ya registrado,*
> *— comprobar que el dueño existe antes de asociarle el animal,*
> *— registrar en un log cada alta…*
>
> *Si esa lógica vive en `main`, o en la UI, o repartida por todos lados, se vuelve
> imposible de mantener y de probar.*
>
> *El **servicio** es la única capa que tiene permiso para orquestar entidades.
> La UI solo llama al servicio y muestra lo que devuelve — no sabe nada de cómo funciona por dentro.*
>
> *Hoy nuestros servicios serán muy simples — solo crean y listan objetos —, pero la
> estructura que dejamos montada nos permitirá añadir lógica real en la Sesión 3 sin tocar la UI."*

Preguntar al alumno si ha entendido antes de continuar:

> *"¿Tiene sentido la separación? ¿Alguna pregunta antes de ver el código?"*

## Paso 5.2 — El agente crea el servicio de la entidad principal como ejemplo

Crear **un solo servicio** (el de la entidad más representativa del dominio) y explicar
cada decisión al alumno.

Patrón del servicio de ejemplo:

```python
from src.entities.xxx import Xxx


class GestionXxxService:
    """Orquesta la creación y consulta de Xxx.

    En esta sesión solo se crean objetos.
    Los métodos de negocio y el uso de Resultado se añadirán en la Sesión 3.

    Ejemplo:
        >>> servicio = GestionXxxService()
        >>> elemento = servicio.registrar("param1", "param2")
        >>> elemento is not None
        True
    """

    def __init__(self):
        self.__elementos = []

    def registrar(self, param1, param2):
        """Crea un objeto Xxx y lo guarda en memoria."""
        elemento = Xxx(param1, param2)
        self.__elementos.append(elemento)
        return elemento

    def listar(self):
        """Devuelve todos los objetos Xxx creados."""
        return list(self.__elementos)
```

Tras crearlo, explicar al alumno:
- Por qué `__elementos` es privado — nadie fuera del servicio debe modificar la lista directamente.
- Por qué `registrar` devuelve el objeto creado — para que quien llame pueda usarlo de inmediato.
- Por qué `listar` devuelve `list(self.__elementos)` — una **copia**, no la lista interna. Si alguien modifica la lista devuelta, no corrompe el estado interno del servicio.

Aplicar la plantilla de verificación:

```
🔍 Acabo de crear src/services/gestion_[xxx]_service.py como ejemplo.
   Por favor, ábrelo y comprueba que:
   - Solo importa de src.entities (nunca de ui ni de persistence).
   - registrar crea el objeto, lo guarda y lo devuelve directamente.
   - listar devuelve list(self.__elementos) — una copia, no la lista interna.
   - No hay lógica de negocio (validaciones, reglas) — eso es Sesión 3.
   ¿Está todo correcto?
```

### Commit tras el servicio de ejemplo

```bash
git add src/services/gestion_[xxx]_service.py
git commit -m "sesion02: servicio de ejemplo GestionXxxService"
git push origin main
```

## Paso 5.3 — El alumno implementa los servicios restantes (modo Ask)

Pedir al alumno que implemente los demás servicios siguiendo el mismo patrón:

> *"Ahora es vuestro turno. Implementad el servicio de [siguiente entidad] en
> `src/services/gestion_[yyy]_service.py`. Cuando lo tengáis, mostradme el código."*

> 🔒 **Modo Ask activo**: el agente NO toca el código del alumno.
> El ciclo es: alumno presenta código → agente revisa con la plantilla → alumno corrige →
> agente revisa de nuevo → repetir hasta que no haya puntos en rojo → pasar al siguiente.

Criterios de revisión para cada servicio:
- ¿La lista interna es privada (`self.__elementos`)?
- ¿`registrar` crea el objeto y lo devuelve?
- ¿`listar` devuelve una copia (`list(...)`)?
- ¿Solo importa de `src.entities`?
- ¿Tiene docstring de clase?
- ¿No hay lógica de negocio?

### Commit tras cada servicio aprobado

Después de aprobar cada servicio, pedir al alumno que haga commit:

> *"Perfecto. Antes de continuar, haz commit de este servicio:*
> ```bash
> git add src/services/gestion_[yyy]_service.py
> git commit -m "sesion02: GestionYyyService"
> git push origin main
> ```
> *Avisadme cuando esté subido."*

## Paso 5.4 — El agente inicia `src/main.py` y el alumno lo completa

El agente crea el esqueleto de `main.py` con **el primer servicio ya integrado** y deja
el resto incompleto para que el alumno lo complete:

```python
from src.services.gestion_xxx_service import GestionXxxService
# TODO: importar el resto de servicios


def main():
    """Punto de entrada: demuestra la arquitectura de extremo a extremo."""

    # Servicio de ejemplo — creado por el agente
    xxx_service = GestionXxxService()
    elemento = xxx_service.registrar("param1", "param2")
    print(f"✅ Registrado: {elemento}")
    print(f"Total: {len(xxx_service.listar())}")

    # TODO: instanciar y usar el resto de servicios


if __name__ == "__main__":
    main()
```

Aplicar la plantilla de verificación:

```
🔍 Acabo de crear el esqueleto de src/main.py con el primer servicio.
   Por favor, ábrelo y fíjate en:
   - main.py solo importa services — ningún "from src.entities" directo.
   - La estructura: instanciar servicio → registrar → listar → print.
   ¿Lo veis claro? Ahora completadlo vosotros con el resto de servicios.
```

A continuación, el agente guía al alumno para completar `main.py` en **modo Ask**:

> *"Ahora añadid el resto de servicios siguiendo el mismo patrón. Por cada servicio:*
> *1. Importadlo arriba.*
> *2. Instanciadlo en `main()`.*
> *3. Registrad un objeto de ejemplo.*
> *4. Imprimid el total con `listar()`.*
>
> *Cuando lo tengáis, pegad el código y lo reviso."*

El agente **no escribe el código de los servicios restantes** en `main.py` — solo da
pistas si el alumno se atasca. Cuando el alumno termine y el agente lo apruebe:

```bash
python -m src.main   # debe arrancar sin errores y mostrar ✅ por cada objeto
```

Señalar explícitamente que `main.py` **no importa ninguna entidad directamente**.

### Commit final de main.py

```bash
git add src/main.py
git commit -m "sesion02: main.py con todos los servicios"
git push origin main
```


Cuando el alumno indique que ha terminado, el agente realiza una **revisión técnica completa y autónoma** del código generado durante la sesión antes de dar feedback. Esta revisión tiene cuatro dimensiones.

---

## 6.1 — Completitud del dominio

El agente comprueba que todas las entidades y relaciones acordadas en la Fase 1 están implementadas:

- ¿Existe un fichero `.py` en `src/entities/` por cada clase identificada en el diagrama?
- ¿Cada clase tiene todos los atributos de instancia acordados con el alumno?
- ¿Los atributos de clase identificados en la Fase 1 están presentes a nivel de clase (fuera del `__init__`)?
- ¿Las relaciones entre clases se reflejan en los `__init__`? Por ejemplo:
  - Si `Animal` tiene un `Dueno`, ¿hay `self.__dueno` en `Animal.__init__`?
  - Si `Animal` tiene una lista de `Visita`, ¿hay `self.__visitas = []` en `Animal.__init__`?
- ¿El diagrama Mermaid en `README.md` refleja fielmente el código final (incluidas las clases añadidas durante la sesión)?

Si falta alguna entidad, atributo o relación, el agente lo crea directamente y aplica la plantilla de verificación.

---

## 6.2 — Convenciones Python (`python-conventions.instructions.md`)

El agente revisa cada fichero de `src/entities/` y comprueba:

- ✅ Nombres de clase en `PascalCase`.
- ✅ Nombres de atributos y parámetros en `snake_case`.
- ✅ Docstring corto en la clase (aunque sea mínimo).
- ✅ **Sin type hints** en esta sesión (Sesión 8) — si los hay, señalarlos como error.
- ✅ **Sin `__str__`** en esta sesión (Sesión 6) — si lo hay, señalarlo como error.
- ✅ Imports en orden: stdlib → third-party → proyecto, separados por línea en blanco.
- ✅ No hay imports innecesarios (especialmente circulares entre entidades).

---

## 6.3 — Arquitectura y reglas de dominio (`architecture.instructions.md` + `entities.instructions.md`)

El agente ejecuta o simula las siguientes comprobaciones:

```bash
# Ningún fichero de ui/ importa entities/
grep -r "from src.entities" src/ui/     # debe devolver vacío

# Ninguna entidad importa services/, ui/ o persistence/
grep -r "from src.services" src/entities/   # debe devolver vacío
grep -r "from src.ui" src/entities/         # debe devolver vacío

# main.py no importa entidades directamente
grep "from src.entities" src/main.py        # debe devolver vacío
```

Además, revisa en el código:
- ✅ Todos los atributos de instancia en `entities/` son privados (`self.__nombre`).
- ✅ No hay `print()`, `input()` ni acceso a ficheros en `entities/`.
- ✅ Los servicios solo importan de `src.entities`.
- ✅ `src/entities/resultado.py` **no existe todavía** — se crea en Sesión 3.

---

## 6.4 — Cobertura de tests (`tests/test_entities.py`)

El agente comprueba que la suite de tests cubre todo lo realizado en la sesión:

- ✅ Existe al menos un test de construcción (`test_XXX_se_crea_correctamente`) por cada clase de `src/entities/`.
- ✅ Los tests de clases con atributos de clase verifican que el atributo existe (`assert hasattr(ClaseX, 'atributo_clase')`).
- ✅ `python -m pytest -q` pasa con **0 fallos y 0 errores**.

Si falta algún test, el agente lo añade directamente y vuelve a ejecutar `pytest`.

---

## 6.5 — Feedback final al alumno

Tras completar las cuatro revisiones, el agente emite el feedback con este formato:

```
✅ Puntos fuertes:
   - [lo que han hecho bien, con ejemplos concretos del código]

⚠️  Aspectos a mejorar (para próximas sesiones):
   - [lo que no está del todo bien, con explicación del por qué]

🔴 Errores corregidos por el agente en la revisión final:
   - [lo que el agente ha tenido que añadir o corregir, con explicación didáctica]

📊 Cobertura de tests: [N] tests — todos en verde ✅
```

Si hay correcciones en rojo, el agente explica **por qué** era un error y **qué regla** se incumplía, para que el alumno lo interiorice de cara a la siguiente sesión.

---

# REGLAS ESTRICTAS PARA HOY

- **Modo Ask cuando el alumno implementa**: el agente NUNCA modifica el código del alumno. Solo da sugerencias con la plantilla de revisión y espera a que el alumno corrija por su cuenta. Aplica tanto a entidades como a servicios y a `main.py`.
- **Reparto de trabajo declarado al inicio**: el agente respeta el orden acordado al pedir las implementaciones al alumno.
- **Commits tras cada paso**: el agente no avanza al siguiente paso sin que el alumno haya hecho commit y push del artefacto actual.
- Los atributos de dominio son privados (`self.__nombre`). Ver `instructions/entities.instructions.md`.
- **Sin type hints** — eso es Sesión 8. Si el alumno los añade, explicar que no corresponde todavía.
- **Sin `__str__`** — eso es Sesión 6. Si el alumno lo añade, explicar que no corresponde todavía.
- No implementar lógica de negocio en entidades todavía — solo estructura (`__init__` y atributos).
- No añadir `@property` todavía — eso es Sesión 5.
- `ui/` no importa nada de `entities/`.
- `entities/resultado.py` **no se crea en esta sesión** — se introduce en Sesión 3.
- Los tests los escribe **exclusivamente el agente** — el alumno no debe escribirlos.
- El agente crea **el primer servicio** como ejemplo; el alumno implementa el resto en modo Ask.
- El agente crea **el esqueleto de `main.py`** con el primer servicio; el alumno completa el resto en modo Ask.
- **Los servicios solo tienen métodos de creación y listado** — los métodos de negocio se añadirán en Sesión 3.
- El agente **siempre explica el porqué** de la capa de servicios y de los tests antes de crearlos.

---

# ✅ DEFINITION OF DONE (DoD)

Antes de cerrar la sesión, verifica que se cumplen **todos** los criterios:

## Quality gates generales (aplican en todas las sesiones)
- [ ] `python -m pytest -q` → 0 fallos, 0 errores
- [ ] `python src/main.py` arranca sin errores
- [ ] No hay imports de `entities/` en `src/ui/`: `grep -r "from entities" src/ui/` → vacío
- [ ] Commits del día con patrón `sesion02: descripción corta`

## Quality gates específicos de esta sesión
- [ ] El equipo ha declarado el reparto de trabajo al inicio (quién implementa qué clases)
- [ ] El alumno ha descrito el sistema y el agente lo ha confirmado antes de diseñar
- [ ] Diagrama de clases Mermaid actualizado en `README.md` y validado por el alumno — con commit
- [ ] Al menos 3 clases de dominio creadas en `src/entities/` con atributos `self.__privado` — con commit por clase
- [ ] Sin type hints en el código del alumno (no corresponde hasta Sesión 8)
- [ ] Sin `__str__` en las clases (no corresponde hasta Sesión 6)
- [ ] `src/entities/resultado.py` **no existe** — se crea en Sesión 3
- [ ] El agente ha explicado la utilidad de los tests antes de generarlos
- [ ] El agente ha escrito al menos un test de construcción por clase y todos pasan (`pytest -q`) — con commit
- [ ] El agente ha creado el **primer servicio** como ejemplo; el alumno ha implementado el resto en modo Ask — con commit por servicio
- [ ] Los servicios **solo tienen métodos de creación y listado** — sin lógica de negocio (eso es Sesión 3)
- [ ] El alumno ha confirmado que entiende **por qué** existe la capa de servicios antes de implementarlos
- [ ] El agente ha creado el esqueleto de `src/main.py`; el alumno lo ha completado en modo Ask — con commit
- [ ] `src/main.py` importa solo servicios (no entidades directamente) y arranca sin errores
- [ ] **Revisión final completada** (Fase 6): completitud del dominio, convenciones Python, arquitectura y cobertura de tests — sin puntos en rojo pendientes

---

# 📓 JOURNAL DE SESIÓN

Al terminar, crea o actualiza `journal/sesion02.md` y haz commit:

```markdown
# Journal — Sesión 02 — [fecha]

## Integrantes
-
-

## Reparto de trabajo
<!-- Quién implementó qué clases y servicios -->
<!-- Ej: Miembro A → Animal, Dueno | Miembro B → Veterinario, Visita, Servicio -->

## Sistema elegido
<!-- Describe en 2-3 frases el sistema que vais a implementar -->

## Clases identificadas y atributos principales
<!-- Lista las clases creadas y sus atributos más relevantes -->

## Decisiones de diseño tomadas (y por qué)

## Problemas encontrados y cómo los resolvimos

## Feedback recibido del agente
<!-- Resume los puntos fuertes y las mejoras indicadas -->

## ¿Qué queda pendiente para la próxima sesión?


## Tiempo invertido
- Horas de trabajo en equipo:
```

```bash
git add journal/sesion02.md
git commit -m "sesion02: journal de sesión"
git push origin main
```
