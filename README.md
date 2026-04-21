# Clínica Veterinaria

Aplicación de consola en Python para gestionar una clínica veterinaria.
Permite registrar dueños, animales y veterinarios, y llevar el historial de visitas asociadas a cada mascota con el servicio realizado.

Arquitectura de cuatro capas: `ui → services → entities → persistence`.

---

## Diagrama de clases

```mermaid
classDiagram
    class Animal {
        -str __nombre
        -str __fecha_nacimiento
        -str __tipo
        -str __raza
        -str __color
        -list __afecciones
        -Dueno __dueno
        +contador_por_tipo$
    }
    class Dueno {
        -str __nif
        -str __nombre
        -str __email
        -str __tfno
        -list __lista_animales
    }
    class Veterinario {
        -str __nif
        -str __nombre
        -str __email
        -str __tfno
        -list __esp_clinicas
        -list __tipos_animales
        +especialidades_clinicas$
        +tipos_animales_atendidos$
    }
    class Visita {
        -str __fecha
        -Servicio __servicio
        -Animal __animal
        -Veterinario __veterinario
        -bool __pagada
    }
    class Servicio {
        -str __codigo
        -str __nombre
        -str __descripcion
        -float __precio
        -str __duracion_estimada
    }

    Animal "many" --> "1" Dueno : pertenece a
    Dueno "1" o-- "many" Animal : tiene
    Animal "1" *-- "many" Visita : tiene historial
    Visita --> "1" Servicio : realiza
    Visita --> "1" Veterinario : atendida por
```
