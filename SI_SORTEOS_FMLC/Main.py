from Controlator.Controller import ParticipanteController

def main():
     # Crear el controlador
    controller = ParticipanteController()

    # Crear un nuevo participante
    participante, statusconn = controller.crear_participante(
        email="geraldinpinzonb@gmail.com",
        name="Geraldin",
        lastname = "Pinzón Bayona",
        cellphone = "3213333191",
        id = "0000002"
    )
    print(statusconn)

    # Mostrar participante
    #controller.mostrar_participante("juan.perez@example.com")

    # Actualizar un participante
    #controller.actualizar_participante("juan.perez@example.com", "Juan Pérez Actualizado", "0987654321")
    #controller.mostrar_participante("juan.perez@example.com")

if __name__ == "__main__":
    main()