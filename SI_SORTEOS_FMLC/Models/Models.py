import cx_Oracle as odbl
from Interface.Interfaces import InterfaceConection

class ModeloConexion(InterfaceConection):
    def __init__(self, user, password, dsn, encoding="UTF-8"):
        super().__init__()
        # Configuración de la conexión
        self.config_odbc_connection = {
            'user': user,
            'password': password,
            'dsn': dsn,
            'encoding': encoding
        }

    def Conection(self):
        conector = None
        try:
            # Intentar conectar a la base de datos
            conector = odbl.connect(**self.config_odbc_connection)
            print("Conexión exitosa a la base de datos.")
        except odbl.Error as error:
            print(f"Error al conectar a la base de datos: {error}")
        finally:
            return conector
        

# Bloque principal
if __name__ == "__main__":
    # Configuración de conexión (reemplaza con tus credenciales)
    user = "MUJERLINDA"
    password = "MUJERCATS"
    dsn = "localhost:1521/XEPDB1"

    # Crear instancia de conexión
    modelo = ModeloConexion(user, password, dsn)

    # Probar la conexión
    conexion = modelo.Conection()

    if conexion:
        print("Prueba de conexión completada.")
        conexion.close()
