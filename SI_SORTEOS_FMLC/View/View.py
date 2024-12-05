import sys, os

path_lib = os.path.dirname(os.path.abspath(__file__))
path_l = os.path.dirname(path_lib)
sys.path.append(path_l)

from Interface.Interfaces import IParticipanteView
class ParticipanteView(IParticipanteView):
    def show_participante(self, participante):
        print("Detalles del Participante:")
        print(f"Correo: {participante.FMLC_CORREO}")
        print(f"Nombre: {participante.FMLC_NOMBRE}")
        print(f"Celular: {participante.FMLC_CELULAR}")
        print(f"Participante: {participante.FMLC_PARTICIPANTE}")