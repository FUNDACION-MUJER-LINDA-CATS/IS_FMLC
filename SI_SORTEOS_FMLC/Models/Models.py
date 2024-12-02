import oracledb as odbl
import sys
sys.path.append("E:/MUJER_LINDA_CATS/SI_FMLC/SI_SORTEOS_FMLC")
from Interface.Interfaces import InterfaceConection

class ModeloConexion(InterfaceConection):
    def dbconn(self):
        conector = None
        try:
            # Intentar conectar a la base de datos
            conector = odbl.connect(**self.config_odbc_connection)
            print("Conexión exitosa a la base de datos.")
        except odbl.Error as error:
            print(f"Error al conectar a la base de datos: {error}")
        return conector
if __name__ == "__main__":
    # Configuración de conexión (reemplaza con tus credenciales)
    
    modelo = ModeloConexion()

    # Probar la conexión
    conexion = modelo.dbconn()

    if conexion:
        print("Prueba de conexión completada.")
        conexion.close()