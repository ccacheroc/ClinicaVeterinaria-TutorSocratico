# Gestión de Aulas

Aplicación de consola en Python para gestionar la reserva de aulas en una escuela.
Permite registrar aulas y profesores, y gestionar las reservas de aulas por franja horaria,
garantizando que no se solapen dos reservas sobre el mismo aula.

Arquitectura de cuatro capas: `ui → services → entities → persistence`.

---

## Diagrama de clases

```mermaid
classDiagram
    class Aula {
        +list tipos_validos$
        -str __identificador
        -str __nombre
        -str __descripcion
        -int __capacidad
        -str __tipo
        -list __reservas
    }
    class Profesor {
        -str __nif
        -str __nombre
        -str __departamento
        -str __email
        -list __reservas
    }
    class Reserva {
        -str __fecha
        -str __hora_inicio
        -str __hora_fin
        -str __motivo
        -Aula __aula
        -Profesor __profesor
    }

    Aula "1" o-- "many" Reserva : tiene
    Profesor "1" o-- "many" Reserva : realiza
    Reserva "many" --> "1" Aula : reserva
    Reserva "many" --> "1" Profesor : realizada por
```
