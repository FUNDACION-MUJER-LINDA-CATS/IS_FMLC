import oracledb as odbl
import sys
sys.path.append("E:/MUJER_LINDA_CATS/SI_FMLC/SI_SORTEOS_FMLC")
from Interface.Interfaces import InterfaceConection, InterfaceParticipante

class DatabaseConection(InterfaceConection):
    def databaseconnection(self):
        conector = None
        try:
            # Intentar conectar a la base de datos
            conector = odbl.connect(**self.config_odbc_connection)
            print("Conexión exitosa a la base de datos.")
        except odbl.Error as error:
            print(f"Error al conectar a la base de datos: {error}")
        return conector
class Participante(InterfaceParticipante):
    dbconn = DatabaseConection()
    
    def addparticipante(self, query, args):
        dbsession = self.dbconn.databaseconnection()
        cursor = dbsession.cursor()
        try:
            cursor.execute(query, args)
            dbsession.commit
            return True
        except odbl.Error as e:
            return e
        finally:
            cursor.close()
            dbsession.close()
        return super().addparticipante(query, args)
if __name__ == "__main__":
    # Configuración de conexión (reemplaza con tus credenciales)
    
    modelo = DatabaseConection()

    # Probar la conexión
    conexion = modelo.databaseconnection()

    if conexion:
        print("Prueba de conexión completada.")
        conexion.close()