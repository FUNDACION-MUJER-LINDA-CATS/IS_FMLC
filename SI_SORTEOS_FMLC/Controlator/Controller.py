import sys, os

path_lib = os.path.dirname(os.path.abspath(__file__))
path_l = os.path.dirname(path_lib)
sys.path.append(path_l)

from Interface.Interfaces import IParticipanteController, IProviderController
from Models.Models import Participante, Proveedor
from View.View import ParticipanteView, ProveedorView

class ParticipanteController(IParticipanteController):
    def __init__(self):
        self.view = ParticipanteView()

    def crear_participante(self, email, name, lastname, cellphone, id):
        # Crea un nuevo participante y lo inserta en la base de datos
        new_participante = Participante(email, name, lastname, cellphone, id)
        statusconn = new_participante.insert()
        return new_participante, statusconn

class ProveedorController(IProviderController):
    def __init__(self):
        self.view = ProveedorView()

    def crear_proveedor(self, name, mail, cellphone, description, type, active, id):
        # Crea un nuevo participante y lo inserta en la base de datos
        new_proveedor = Proveedor(name, mail, cellphone, description, type, active, id)
        statusconn = new_proveedor.insert()
        return new_proveedor, statusconn
