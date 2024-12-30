import sys, os

path_lib = os.path.dirname(os.path.abspath(__file__))
path_l = os.path.dirname(path_lib)
sys.path.append(path_l)

from Interface.ParticipanteInterface import IParticipanteView
from Interface.ProveedorInterface import IProviderView

class ParticipanteView(IParticipanteView):
    def show_participante(self, participante):
        print("Detalles del Participante:")
        print(f"Correo: {participante.FMLC_CORREO}")
        print(f"Nombre: {participante.FMLC_NOMBRE}")
        print(f"Celular: {participante.FMLC_CELULAR}")
        print(f"Participante: {participante.FMLC_PARTICIPANTE}")


class ProveedorView(IProviderView):
    def show_proveedor(self, proveedor):
        print("Detalles del Proveedor:")
        print(f"Nombre: {proveedor.FMLC_PRV_NOMBRE}")
        print(f"Correo: {proveedor.FMLC_PRV_CORREO}")
        print(f"Celular: {proveedor.FMLC_PRV_CELULAR}")
        print(f"Descripcion: {proveedor.FMLC_PRV_DESCRIPCION}")
        print(f"Tipo: {proveedor.FMLC_PRV_TIPO}")
        print(f"Activo: {proveedor.FMLC_PRV_ACTIVO}")

class ProveedorGetById(IProviderView):
    def show_proveedor(self, proveedor):
        print("Proveedor:")
        print(f"Nombre: {proveedor.FMLC_PRV_NOMBRE}")
        print(f"Correo: {proveedor.FMLC_PRV_CORREO}")
        print(f"Celular: {proveedor.FMLC_PRV_CELULAR}")
        print(f"Descripcion: {proveedor.FMLC_PRV_DESCRIPCION}")
        print(f"Tipo: {proveedor.FMLC_PRV_TIPO}")
        print(f"Activo: {proveedor.FMLC_PRV_ACTIVO}")
