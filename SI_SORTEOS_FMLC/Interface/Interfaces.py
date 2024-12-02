from abc import ABC, abstractmethod

class InterfaceConection:
    def __init__(self):
        self.config_odbc_connection = {
            'username' : '',
            'password' : '',
            'dsn'   : '',
            'encoding': 'UTF-8'  
        }
    
    @abstractmethod
    def Conection(self):
        pass

    @abstractmethod
    def Select(self, table, word):
        pass

    @abstractmethod
    def SQLQuery(self, conector, word, table):
        pass