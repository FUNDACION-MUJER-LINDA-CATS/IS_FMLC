from Interface.ParticipanteInterface import IParticipanteView

class ParticipanteView(IParticipanteView):
    def show_participante(self, participante):
        print("\nDetalles del Participante:\n")
        print(f"Nombre: {participante.FMLC_NOMBRE}")
        print(f"Apellido: {participante.FMLC_APELLIDO}")
        print(f"Celular: {participante.FMLC_CELULAR}")
        print(f"Correo: {participante.FMLC_CORREO}")
        print("\n")
