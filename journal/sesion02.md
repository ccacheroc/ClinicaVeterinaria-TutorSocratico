# Journal — Sesión 02 — 21 de abril de 2026

## Integrantes
- Cristina Cachero
-

## Sistema elegido
Sistema de gestión para una clínica veterinaria. Permite registrar dueños de mascotas,
animales y veterinarios, y llevar el historial de visitas de cada animal con el servicio
realizado y el veterinario que lo atendió.

## Clases identificadas y atributos principales

| Clase | Atributos de instancia | Atributos de clase |
|---|---|---|
| `Animal` | `__nombre`, `__fecha_nacimiento`, `__tipo`, `__raza`, `__color`, `__afecciones` (lista), `__dueno` | `contador_por_tipo` (dict) |
| `Dueno` | `__nif`, `__nombre`, `__email`, `__tfno`, `__lista_animales` (lista) | — |
| `Veterinario` | `__nif`, `__nombre`, `__email`, `__tfno`, `__esp_clinicas` (lista), `__tipos_animales` (lista) | `especialidades_clinicas` (lista), `tipos_animales_atendidos` (lista) |
| `Visita` | `__fecha`, `__servicio`, `__animal`, `__veterinario`, `__pagada` | — |
| `Servicio` | `__codigo`, `__nombre`, `__descripcion`, `__precio`, `__duracion_estimada` | — |

## Decisiones de diseño tomadas (y por qué)

- **Todos los atributos son privados (`self.__nombre`)**: para proteger los invariantes del
  dominio. Nadie fuera de la clase puede modificarlos directamente.
- **`Animal.contador_por_tipo` como diccionario**: en lugar de un contador total, se decidió
  contar por tipo de animal (`{"perro": 2, "gato": 1, …}`) para tener estadísticas más útiles.
- **`Veterinario` con dos atributos de clase separados**: se separaron `especialidades_clinicas`
  (tipo de servicio) y `tipos_animales_atendidos` (especie atendida) porque son dos dimensiones
  independientes. Así se puede buscar "veterinarios que hacen cirugía" y "veterinarios que
  atienden aves" de forma independiente.
- **`Visita.pagada = False` por defecto**: cuando se crea una visita, aún no está pagada.
  Es el estado inicial lógico.
- **`Dueno` tiene `__lista_animales`**: aunque la relación principal es `Animal → Dueno`,
  se añadió la lista inversa en `Dueno` para poder consultar todos los animales de un dueño
  sin recorrer toda la lista de animales.
- **`Servicio` tiene `__codigo`**: se añadió por iniciativa propia para identificar
  unívocamente cada servicio del catálogo.
- **`resultado.py` no se crea en esta sesión**: `Resultado` se introducirá en la Sesión 3,
  cuando las entidades tengan métodos de negocio que necesiten comunicar éxito o error.

## Problemas encontrados y cómo los resolvimos

- **Import circular en `Dueno`**: en el primer intento se importó `Animal` dentro de `Dueno`,
  lo que creaba una dependencia circular. Se eliminó el import — en esta sesión no hay
  type hints, así que no era necesario.
- **Atributo condicional en `Dueno`**: `if animal: self.__animal = animal` hacía que el
  atributo no existiese si no se pasaba nada. Se corrigió inicializando siempre la lista:
  `self.__lista_animales = [] if lista_animales is None else lista_animales`.
- **Atributos de clase sueltos en `Veterinario`**: en un intento intermedio aparecieron
  `tfno = None` y `__especialidades = None` a nivel de clase por error. Se eliminaron —
  solo `especialidades_clinicas` y `tipos_animales_atendidos` son atributos de clase.

## Feedback recibido del agente

✅ **Puntos fuertes:**
- Identificación de 5 clases de dominio ricas y bien delimitadas.
- Todos los atributos de instancia privados con doble guion en todas las clases.
- Se detectó de forma autónoma que `Visita` necesitaba el atributo `__animal`.
- Propuesta autónoma de añadir `__codigo` a `Servicio`.
- Diseño de `Veterinario` con dos dimensiones separadas — decisión madura.

⚠️ **Aspectos a mejorar:**
- Usar `telefono` en lugar de `tfno` para ser más expresivo y consistente.
- Recordar que los atributos siempre deben inicializarse en `__init__`, aunque sean
  `None` o lista vacía — nunca de forma condicional.

## ¿Qué queda pendiente para la próxima sesión?

- Crear `src/entities/resultado.py` con `Resultado.exito` y `Resultado.error`.
- Añadir métodos de negocio a las entidades (Sesión 3).
- Actualizar los servicios para usar `Resultado` en lugar de devolver el objeto directamente.
- Ampliar los tests con Given/When/Then para cada método nuevo.

## Tiempo invertido
- Horas de trabajo en equipo:

