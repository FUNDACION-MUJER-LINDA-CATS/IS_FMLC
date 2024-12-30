from abc import ABC, abstractmethod

class IParticipanteModel(ABC):  
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def getById(self, id):
        pass
    @abstractmethod
    def getByCellphone(self, cellphone):
        pass

class IParticipanteView(ABC):
    @abstractmethod
    def show_participante(self, participante):
        pass

class IParticipanteController(ABC):
    @abstractmethod
    def addParticipante(self, mail, name, lastname, cellphone):
        pass
        
    @abstractmethod
    def getParticpanteBycellPhone(self, cellphone):
        pass
    
    @abstractmethod
    def getParticpanteByid(self, id):
        pass
    
    @abstractmethod
    def updateParticipante(self, participante):
        pass
