from abc import ABC, abstractmethod

class InterfaceConection(ABC):
    mujerlinda = 'MUJERCATS'
    def __init__(self):
        self.config_odbc_connection = {
            'user' : 'MUJERLINDA',
            'password' : self.mujerlinda,
            'dsn'   : 'localhost:1521/XEPDB1'
        }
    
    @abstractmethod
    def databaseconnection(self):
        pass

    @abstractmethod
    def getColumnsByTable(self, table):
        pass

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
    
### Proveedor ###
class IProviderModel(ABC):  
    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass

class IProviderView(ABC):
    @abstractmethod
    def show_proveedor(self, proveedor):
        pass

class IProviderController(ABC):
    @abstractmethod
    def crear_proveedor(self, name, mail, cellphone, description, type, active, id):
        pass