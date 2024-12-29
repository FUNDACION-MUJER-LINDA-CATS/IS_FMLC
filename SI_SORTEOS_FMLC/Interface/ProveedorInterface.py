from abc import ABC, abstractmethod
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