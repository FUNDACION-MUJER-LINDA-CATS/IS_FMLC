import sys, os

path_lib = os.path.dirname(os.path.abspath(__file__))
path_l = os.path.dirname(path_lib)
sys.path.append(path_l)

from Interface.ParticipanteInterface import IParticipanteController
from Models.ParticipanteModel import Participante
from View.ParticipanteView import ParticipanteView

class ParticipanteController(IParticipanteController):
    def __init__(self):
        self.view = ParticipanteView()

    def addParticipante(self, email, name, lastname, cellphone):
        # Crea un nuevo participante y lo inserta en la base de datos
        new_participante = Participante(email, name, lastname, cellphone, None)
        statusconn = new_participante.insert()
        return new_participante, statusconn
    
    def getParticpanteByid(self, id):
        participante = Participante(None,None,None,None,None)
        participante, status = participante.getById(id)
        return participante, status
    
    def getParticpanteBycellPhone(self, cellphone):
        participante = Participante(None,None,None,None,None)
        participante, status = participante.getByCellphone(cellphone)
        return participante, status
    
    def updateParticipante(self, participante):
        print(f"actualizando {participante}")
        status = participante.update()
        participante, _ = participante.getById(participante.FMLC_PARTICIPANTE)
        return status

