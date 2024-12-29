from abc import ABC, abstractmethod
import json,os

class InterfaceConection(ABC):
    def __init__(self):
        config_file_path = 'config.json'
        if not os.path.exists(config_file_path):
            raise FileNotFoundError(f"El archivo {config_file_path} no existe.")
        
        with open('config.json','r') as config_file:
            config = json.load(config_file)
        
        self.config_odbc_connection = {
            'user' : config['user'],
            'password' : config['password'],
            'dsn'   : config['dsn']
        }
    
    @abstractmethod
    def databaseconnection(self):
        pass

    @abstractmethod
    def getColumnsByTable(self, table):
        pass

