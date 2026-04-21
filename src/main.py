from src.services.gestion_dueno_service import GestionDuenoService
from src.services.gestion_veterinario_service import GestionVeterinarioService
from src.services.gestion_servicio_service import GestionServicioService
from src.services.gestion_animal_service import GestionAnimalService
from src.services.gestion_visita_service import GestionVisitaService


def main():
    """Punto de entrada: demuestra la arquitectura de extremo a extremo."""

    # Servicios
    duenos = GestionDuenoService()
    veterinarios = GestionVeterinarioService()
    servicios = GestionServicioService()
    animales = GestionAnimalService()
    visitas = GestionVisitaService()

    # Dueños
    dueno = duenos.registrar("12345678A", "Ana García", "ana@email.com", "600111222")
    print(f"✅ Dueño registrado: {dueno._Dueno__nombre}")

    # Veterinarios
    vet = veterinarios.registrar(
        "87654321B", "Dr. López", "lopez@clinica.com", "600333444",
        esp_clinicas=["Medicina general", "Cirugía"]
    )
    print(f"✅ Veterinario registrado: {vet._Veterinario__nombre}")

    # Catálogo de servicios
    consulta = servicios.registrar("S001", "Consulta general", "Revisión rutinaria", 30.0, "30 min")
    print(f"✅ Servicio registrado: {consulta._Servicio__nombre}")

    # Animales
    animal = animales.registrar("Rex", "2020-03-15", "perro", "labrador", "negro", dueno)
    print(f"✅ Animal registrado: {animal._Animal__nombre}")

    # Visitas
    visita = visitas.registrar("2026-04-21", consulta, animal, vet)
    print(f"✅ Visita registrada para: {visita._Visita__animal._Animal__nombre}")

    # Resumen
    print(f"\n📋 Resumen:")
    print(f"   Dueños:      {len(duenos.listar())}")
    print(f"   Veterinarios:{len(veterinarios.listar())}")
    print(f"   Servicios:   {len(servicios.listar())}")
    print(f"   Animales:    {len(animales.listar())}")
    print(f"   Visitas:     {len(visitas.listar())}")


if __name__ == "__main__":
    main()

