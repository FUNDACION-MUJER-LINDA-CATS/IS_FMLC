import sys, os

path_lib = os.path.dirname(os.path.abspath(__file__))
path_l = os.path.dirname(path_lib)
sys.path.append(path_l)

from Interface.Interfaces import IParticipanteController
from Models.Models import Participante
from View.View import ParticipanteView

class ParticipanteController(IParticipanteController):
    def __init__(self):
        self.view = ParticipanteView()

    def crear_participante(self, email, name, lastname, cellphone):
        # Crea un nuevo participante y lo inserta en la base de datos
        new_participante = Participante(email, name, lastname, cellphone, None)
        statusconn = new_participante.insert()
        return new_participante, statusconn