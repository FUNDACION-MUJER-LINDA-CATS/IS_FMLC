from Interface.ProveedorInterface import IProviderView

class ProveedorView(IProviderView):
    def show_proveedor(self, proveedor):
        print("Detalles del Proveedor:")
        print(f"Nombre: {proveedor.FMLC_PRV_NOMBRE}")
        print(f"Correo: {proveedor.FMLC_PRV_CORREO}")
        print(f"Celular: {proveedor.FMLC_PRV_CELULAR}")
        print(f"Descripcion: {proveedor.FMLC_PRV_DESCRIPCION}")
        print(f"Tipo: {proveedor.FMLC_PRV_TIPO}")
        print(f"Activo: {proveedor.FMLC_PRV_ACTIVO}")