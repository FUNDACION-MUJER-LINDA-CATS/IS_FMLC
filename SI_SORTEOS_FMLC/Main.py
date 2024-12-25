from Controlator.Controller import ProveedorController

def main():
     # Crear el controlador
    controller = ProveedorController()

    # Crear un nuevo participante
    proveedor, statusconn = controller.crear_proveedor(
        name="Johan Lopera",
        mail = None,
        cellphone = "3127937598",
        description = "Arena de Maiz",
        type = "Arena",
        active = 1,
        id = None
    )
    print(statusconn)

    # Mostrar participante
    #controller.mostrar_participante("juan.perez@example.com")

    # Actualizar un participante
    #controller.actualizar_participante("juan.perez@example.com", "Juan Pérez Actualizado", "0987654321")
    #controller.mostrar_participante("juan.perez@example.com")

if __name__ == "__main__":
    main()