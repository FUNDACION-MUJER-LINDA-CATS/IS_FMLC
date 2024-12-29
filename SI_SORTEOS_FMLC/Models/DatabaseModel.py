from pypika import Query, Table
import oracledb as odbl
import sys, os

path_lib = os.path.dirname(os.path.abspath(__file__))
path_l = os.path.dirname(path_lib)
sys.path.append(path_l)

from Interface.ConnectionInterface import InterfaceConection

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
