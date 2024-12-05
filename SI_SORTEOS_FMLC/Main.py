from Controlator.Controller import ParticipanteController

def main():
     # Crear el controlador
    controller = ParticipanteController()

    # Crear un nuevo participante
    controller.crear_participante(
        email="juan.perez@example.com",
        name="Juan Pérez",
        lastname = "Herrera Quinoes",
        cellphone = "1234567890",
        id = "0000002"
    )

    # Mostrar participante
    #controller.mostrar_participante("juan.perez@example.com")

    # Actualizar un participante
    #controller.actualizar_participante("juan.perez@example.com", "Juan Pérez Actualizado", "0987654321")
    #controller.mostrar_participante("juan.perez@example.com")

if __name__ == "__main__":
    main()