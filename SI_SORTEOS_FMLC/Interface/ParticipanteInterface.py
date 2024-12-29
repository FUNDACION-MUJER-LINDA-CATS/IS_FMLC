from abc import ABC, abstractmethod

class IParticipanteModel(ABC):  
    @abstractmethod
    def insert(self):
        pass
    ''' @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def getByCellphone(self, cellphone):
        pass
    '''

class IParticipanteView(ABC):
    @abstractmethod
    def show_participante(self, participante):
        pass

class IParticipanteController(ABC):
    @abstractmethod
    def crear_participante(self, mail, name, lastname, cellphone, id):
        pass

    ''' 
   @abstractmethod
    def actualizar_participante(self, mail, name, lastname, cellphone):
        pass

    @abstractmethod
    def mostrar_participante(self, cellphone):
        pass'''