from  .DatabaseModel import Database
from Interface.ParticipanteInterface import IParticipanteModel
import oracledb as odbl
import sys, os


path_lib = os.path.dirname(os.path.abspath(__file__))
path_l = os.path.dirname(path_lib)
sys.path.append(path_l)

class Participante(IParticipanteModel):
    ERROR_DESCRIPTION = "Error al procesar la transacción"
    db = Database()
    def __init__(self, correo, nombre, apellido, celular, id):
        self.FMLC_CORREO = correo
        self.FMLC_NOMBRE = nombre
        self.FMLC_APELLIDO = apellido
        self.FMLC_CELULAR = celular
        self.FMLC_PARTICIPANTE = id

    def __str__(self):
        return f"Participante ({self.FMLC_NOMBRE}, {self.FMLC_APELLIDO}, {self.FMLC_CORREO}, {self.FMLC_CELULAR})"
    
    def to_dict(self):
        return {
            "NOMBRE": self.FMLC_NOMBRE,
            "APELLIDO": self.FMLC_APELLIDO,
            "CELULAR": self.FMLC_CELULAR,
            "CORREO": self.FMLC_CORREO
        }
        
    def insert(self):
        try:
            dbsession, statusconn = self.db.databaseconnection()
            if statusconn["statusCode"] == "00":
                with dbsession.cursor() as dbcursor:
                    sql = """INSERT INTO FMLC_PARTICIPANTE_RIFA (FMLC_CORREO, FMLC_NOMBRE, FMLC_APELLIDO, FMLC_CELULAR, FMLC_PARTICIPANTE) 
                    VALUES (:correo, :nombre, :apellido, :celular, FMLC_PARTICIPANTE_RIFA_TX_SEQ.NEXTVAL)"""
                    dbcursor.execute(sql, (self.FMLC_CORREO, self.FMLC_NOMBRE.upper(), self.FMLC_APELLIDO.upper(), self.FMLC_CELULAR))
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
            statusconn["statusDesc"] = self.ERROR_DESCRIPTION
            statusconn["additionalCodeStatus"] = "12"
            statusconn["additionalStatus"] = error_ob[0] + " Error al realizar insert"
        return statusconn

    def getByCellphone(self, cellphone):
        try:
            dbsession, statusconn = self.db.databaseconnection()
            if statusconn["statusCode"] == "00":
                with dbsession.cursor() as dbcursor:
                    sql = """SELECT FMLC_NOMBRE, FMLC_APELLIDO, FMLC_CORREO, FMLC_CELULAR, FMLC_PARTICIPANTE FROM FMLC_PARTICIPANTE_RIFA WHERE FMLC_CELULAR = :celular"""
                    dbcursor.execute(sql, {"celular": cellphone})
                    row = dbcursor.fetchone()
                    if row:
                        participante = Participante(nombre=row[0], apellido=row[1], correo=row[2],celular=row[3], id=row[4])
                        statusconn["statusDesc"] = "Participante encontrado"
                        return participante, statusconn
        except odbl.Error as dberror:
            error_ob, = dberror.args
            statusconn["statusCode"] = "15"
            statusconn["statusDesc"] = "Error al consultar en base de datos "
            statusconn["additionalCodeStatus"] = error_ob.full_code
            statusconn["additionalStatus"] = error_ob.message
        except Exception as e:
            error_ob = e.args
            statusconn["statusCode"] = "14"
            statusconn["statusDesc"] = self.ERROR_DESCRIPTION
            statusconn["additionalCodeStatus"] = "12"
            statusconn["additionalStatus"] = error_ob[0] + " Error al generar la consulta"
        return None, statusconn
    
    def getById(self, id):
        try:
            dbsession, statusconn = self.db.databaseconnection()
            if statusconn["statusCode"] == "00":
                with dbsession.cursor() as dbcursor:
                    sql = """SELECT FMLC_NOMBRE, FMLC_APELLIDO, FMLC_CORREO, FMLC_CELULAR, FMLC_PARTICIPANTE FROM FMLC_PARTICIPANTE_RIFA WHERE FMLC_PARTICIPANTE = :id"""
                    dbcursor.execute(sql, {"id": id})
                    row = dbcursor.fetchone()
                    if row:
                        participante = Participante(nombre=row[0], apellido=row[1], correo=row[2],celular=row[3], id=row[4])
                        statusconn["statusDesc"] = "Participante encontrado"
                        return participante, statusconn
        except odbl.Error as dberror:
            error_ob, = dberror.args
            statusconn["statusCode"] = "15"
            statusconn["statusDesc"] = "Error al consultar en base de datos "
            statusconn["additionalCodeStatus"] = error_ob.full_code
            statusconn["additionalStatus"] = error_ob.message
        except Exception as e:
            error_ob = e.args
            statusconn["statusCode"] = "14"
            statusconn["statusDesc"] = "Error al procesar la transacción."
            statusconn["additionalCodeStatus"] = "12"
            statusconn["additionalStatus"] = error_ob[0] + " Error al generar la consulta"
        return None, statusconn
    
    def update(self):
        try:
            dbsession, statusconn = self.db.databaseconnection()
            if statusconn["statusCode"] == "00":
                with dbsession.cursor() as dbcursor:
                    sql = """UPDATE FMLC_PARTICIPANTE_RIFA SET FMLC_NOMBRE=:nombre, FMLC_APELLIDO=:apellido, FMLC_CORREO=:correo, FMLC_CELULAR = :celular WHERE FMLC_PARTICIPANTE=:id"""
                    dbcursor.execute(sql, {"nombre":self.FMLC_NOMBRE.upper(), "apellido": self.FMLC_APELLIDO.upper(), "correo": self.FMLC_CORREO, "celular":self.FMLC_CELULAR, "id": self.FMLC_PARTICIPANTE})
                    dbsession.commit()
                    statusconn["statusDesc"] = "Datos Actualizados Correctamente"
                    return statusconn
        except odbl.Error as dberror:
            error_ob, = dberror.args
            statusconn["statusCode"] = "16"
            statusconn["statusDesc"] = "Error al actualizar en base de datos "
            statusconn["additionalCodeStatus"] = error_ob.full_code
            statusconn["additionalStatus"] = error_ob.message
        except Exception as e:
            error_ob = e.args
            statusconn["statusCode"] = "14"
            statusconn["statusDesc"] = self.ERROR_DESCRIPTION
            statusconn["additionalCodeStatus"] = "12"
            statusconn["additionalStatus"] = error_ob[0] + " Error al generar la actualización"
        return statusconn