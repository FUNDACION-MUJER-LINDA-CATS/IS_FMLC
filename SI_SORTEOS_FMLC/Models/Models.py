from pypika import Query, Table
import oracledb as odbl
import sys, os

path_lib = os.path.dirname(os.path.abspath(__file__))
path_l = os.path.dirname(path_lib)
sys.path.append(path_l)

from Interface.Interfaces import InterfaceConection, IParticipanteModel

class Database(InterfaceConection):
    def databaseconnection(self):
        conector = None
        statusconn = {
            "statusCode" : "00",
            "statusDesc" : "Conexión Exitosa"
        }
        try:
            # Intentar conectar a la base de datos
            conector = odbl.connect(**self.config_odbc_connection)
        except odbl.Error as error:
            error_ob, = error.args
            statusconn["statusCode"] = "10"
            statusconn["statusDesc"] = "Error al conectarse a la base de datos."
            statusconn["additionalCodeStatus"] = error_ob.full_code
            statusconn["additionalStatus"] = error_ob.message
        return conector, statusconn

    def getColumnsByTable(self, table):
        columnstable = []
        db, statusconn = self.databaseconnection()
        try:
            if statusconn["statusCode"] == "00":
                with db.cursor() as dbcursor:
                    user_table = Table("USER_TAB_COLS")
                    query = Query.from_(user_table).select(user_table.COLUMN_NAME).where(user_table.TABLE_NAME == table)
                    print(str(query))
                    dbcursor.execute(str(query))
                    columnstable = [column[0] for column in dbcursor.fetchall()]
        except odbl.Error as error:
            error_ob, = error.args
            statusconn["statusCode"] = "11"
            statusconn["statusDesc"] = "Error en la consulta"
            statusconn["additionalCodeStatus"] = error_ob.full_code
            statusconn["additionalStatus"] = error_ob.message
        except Exception as e:
            error_ob = e.args
            statusconn["statusCode"] = "12"
            statusconn["statusDesc"] = "Error al consultar columnas de la tabla."
            statusconn["additionalCodeStatus"] = "14"
            statusconn["additionalStatus"] = error_ob[0]
        return columnstable, statusconn


class Participante(IParticipanteModel):
    db = Database()
    def __init__(self, correo, nombre, apellido, celular, id):
        self.FMLC_CORREO = correo
        self.FMLC_NOMBRE = nombre
        self.FMLC_APELLIDO = apellido
        self.FMLC_CELULAR = celular
        self.FMLC_PARTICIPANTE = id

    def __str__(self):
        return f"Participante({self.FMLC_NOMBRE}, {self.FMLC_APELLIDO}, {self.FMLC_CORREO}, {self.FMLC_CELULAR}, {self.FMLC_PARTICIPANTE})"
    
    def to_dict(self):
        return {
            "FMLC_CORREO": self.FMLC_CORREO,
            "FMLC_NOMBRE": self.FMLC_NOMBRE,
            "FMLC_APELLIDO": self.FMLC_APELLIDO,
            "FMLC_CELULAR": self.FMLC_CELULAR,
            "FMLC_PARTICIPANTE": self.FMLC_PARTICIPANTE
        }
        
    def insert(self):
        try:
            dbsession, statusconn = self.db.databaseconnection()
            if statusconn["statusCode"] == "00":
                with dbsession.cursor() as dbcursor:
                    sql = """INSERT INTO FMLC_PARTICIPANTE_RIFA (FMLC_CORREO, FMLC_NOMBRE, FMLC_APELLIDO, FMLC_CELULAR, FMLC_PARTICIPANTE) 
                    VALUES (:correo, :nombre, :apellido, :celular, FMLC_PARTICIPANTE_RIFA_TX_SEQ.NEXTVAL)"""
                    dbcursor.execute(sql, (self.FMLC_CORREO, self.FMLC_NOMBRE, self.FMLC_APELLIDO, self.FMLC_CELULAR))
                    dbsession.commit()
                    statusconn["statusDesc"] = "Participante agregado correctamente" 
        except odbl.Error as dberror:
            error_ob, = dberror.args
            statusconn["statusCode"] = "13"
            statusconn["statusDesc"] = "Error al insertar en base de datos "
            statusconn["additionalCodeStatus"] = error_ob.full_code
            statusconn["additionalStatus"] = error_ob.message
        except Exception as e:
            error_ob = e.args
            statusconn["statusCode"] = "14"
            statusconn["statusDesc"] = "Error al procesar la transacción."
            statusconn["additionalCodeStatus"] = "12"
            statusconn["additionalStatus"] = error_ob[0]
        return statusconn