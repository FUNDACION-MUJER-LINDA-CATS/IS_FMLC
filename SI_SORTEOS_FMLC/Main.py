from Controlator.ProveedorController import ProveedorController

def main():
     # Crear el controlador
    controller = ProveedorController()
    controller.consultar_proveedorById("2")
    
    # Mostrar participante
    #controller.mostrar_participante("juan.perez@example.com")

    # Actualizar un participante
    #controller.actualizar_participante("juan.perez@example.com", "Juan Pérez Actualizado", "0987654321")
    #controller.mostrar_participante("juan.perez@example.com")

if __name__ == "__main__":
    main()