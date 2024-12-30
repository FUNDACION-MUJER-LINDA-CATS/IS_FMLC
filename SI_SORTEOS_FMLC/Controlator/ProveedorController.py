import sys, os

path_lib = os.path.dirname(os.path.abspath(__file__))
path_l = os.path.dirname(path_lib)
sys.path.append(path_l)
from Interface.ProveedorInterface import IProviderController
from Models.ProveedorModel import Proveedor
from View.View import ProveedorView

class ProveedorController(IProviderController):
    def __init__(self):
        self.view = ProveedorView()

    def crear_proveedor(self, name, mail, cellphone, description, type, active, id):
        # Crea un nuevo Proveedor y lo inserta en la base de datos
        new_proveedor = Proveedor(name, mail, cellphone, description, type, active, id)
        statusconn = new_proveedor.insert()
        return new_proveedor, statusconn
    
    def consultar_proveedorById(self, id):
        # Consultar Proveedor por Id
        provider  = Proveedor(None,None,None,None,None,None,id=id)
        proveedor,statusconn = provider.query(id)
        return provider, statusconn