from abc import ABC, abstractmethod

class InterfaceConection:
    mujerlinda = 'MUJERCATS'
    def __init__(self):
        self.config_odbc_connection = {
            'user' : 'MUJERLINDA',
            'password' : self.mujerlinda,
            'dsn'   : 'localhost:1521/XEPDB1'
        }
    
    @abstractmethod
    def conection(self):
        pass

    @abstractmethod
    def select(self, table, word):
        pass

    @abstractmethod
    def sqlquery(self, conector, word, table):
        pass
class InterfaceParticipante(InterfaceConection):
    nombreParticipante = ""
    celularParticipante = ""
    correoParticioante = ""
    
    @abstractmethod
    def addparticipante(self, query, args):
        pass
    @abstractmethod
    def modparticipante(self,query,args):
        pass
    @abstractmethod
    def getparticipante(self, query):
        pass