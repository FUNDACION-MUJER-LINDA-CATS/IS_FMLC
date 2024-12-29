from Controlator.ParticipanteController import ParticipanteController

def main():
     # Crear el controlador
    controller = ParticipanteController()

    # Crear un nuevo participante
    _, statusconn = controller.crear_participante(
        email="ajherrera9810@gmail.com",
        name="Arnold Julian",
        lastname = "Herrera Quiñones",
        cellphone = "3124884360")

    '''_, statusconn = controller.crear_proveedor(
        name="Johan Lopera",
        mail = None,
        cellphone = "3127937598",
        description = "Arena de Maiz",
        type = "Arena",
        active = 1,
        id = None
    )'''
    #print(statusconn)

    # Mostrar participante
    #controller.mostrar_participante("juan.perez@example.com")

    # Actualizar un participante
    #controller.actualizar_participante("juan.perez@example.com", "Juan Pérez Actualizado", "0987654321")
    #controller.mostrar_participante("juan.perez@example.com")

if __name__ == "__main__":
    main()