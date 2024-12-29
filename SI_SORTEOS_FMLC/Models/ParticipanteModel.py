from pypika import Query, Table
from  .DatabaseModel import Database
from Interface.ParticipanteInterface import IParticipanteModel
import oracledb as odbl
import sys, os


path_lib = os.path.dirname(os.path.abspath(__file__))
path_l = os.path.dirname(path_lib)
sys.path.append(path_l)

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

