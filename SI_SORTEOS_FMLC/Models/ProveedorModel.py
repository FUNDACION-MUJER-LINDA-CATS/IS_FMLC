from pypika import Query, Table
from DatabaseModel import Database
from Interface.ProveedorInterface import IProviderModel
import oracledb as odbl
import sys, os

path_lib = os.path.dirname(os.path.abspath(__file__))
path_l = os.path.dirname(path_lib)
sys.path.append(path_l)

class Proveedor(IProviderModel):
    db = Database()
    def __init__(self, nombre, correo, celular, description, tipo, activo, id):
        self.FMLC_PRV_ID = id
        self.FMLC_PRV_NOMBRE = nombre
        self.FMLC_PRV_CORREO = correo
        self.FMLC_PRV_CELULAR = celular
        self.FMLC_PRV_DESCRIPCION = description
        self.FMLC_PRV_TIPO = tipo
        self.FMLC_PRV_ACTIVO = activo

    def __str__(self):
        return f"Proveedor({self.FMLC_PRV_NOMBRE}, {self.FMLC_PRV_CORREO}, {self.FMLC_PRV_CELULAR}, {self.FMLC_PRV_DESCRIPCION}, {self.FMLC_PRV_TIPO}, {self.FMLC_PRV_ACTIVO})"
    
    def to_dict(self):
        return {
            "FMLC_PRV_NOMBRE": self.FMLC_PRV_NOMBRE,
            "FMLC_PRV_CORREO": self.FMLC_PRV_CORREO,
            "FMLC_PRV_CELULAR": self.FMLC_PRV_CELULAR,
            "FMLC_PRV_DESCRIPCION": self.FMLC_PRV_DESCRIPCION,
            "FMLC_PRV_TIPO": self.FMLC_PRV_TIPO,
            "FMLC_PRV_ACTIVO": self.FMLC_PRV_ACTIVO
        }
    def insert(self):
        try:
            dbsession, statusconn = self.db.databaseconnection()
            if statusconn["statusCode"] == "00":
                with dbsession.cursor() as dbcursor:
                    sql = """INSERT INTO FMLC_PROVEEDOR (FMLC_PRV_NOMBRE, FMLC_PRV_CORREO, FMLC_PRV_CELULAR, FMLC_PRV_DESCRIPCION, FMLC_PRV_TIPO, FMLC_PRV_ACTIVO, FMLC_PRV_ID) 
                    VALUES (:nombre, :correo, :celular, :descripcion, :tipo, :activo, FMLC_PROVEEDOR_TX_SEQ.NEXTVAL)"""
                    dbcursor.execute(sql, (self.FMLC_PRV_NOMBRE, self.FMLC_PRV_CORREO, self.FMLC_PRV_CELULAR, self.FMLC_PRV_DESCRIPCION, self.FMLC_PRV_ACTIVO, self.FMLC_PRV_ACTIVO))
                    dbsession.commit()
                    statusconn["statusDesc"] = "Proveedor agregado correctamente" 
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
