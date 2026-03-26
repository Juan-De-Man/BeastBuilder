import mysql.connector
from classes.dbconfig import Connect

class Dagschema:
    def __init__(self,dagid =None,schemanr=None, gepland=None,oefnr=None,aantal=None, rust=None, herhalingen=None,uitgevoerd=None):
        self.dagid = dagid
        self.schemanr = schemanr
        self.gepland = gepland
        self.oefnr = oefnr
        self.aantal = aantal
        self.rust = rust
        self.herhalingen = herhalingen
        self.uitgevoerd = uitgevoerd
        

    def __repr__(self):
        return f"Dagid ={self.dagid}, Schemanummer = {self.schemanr}, Geplande dag = {self.gepland}, oefnr={self.oefnr}, aantal={self.aantal}, rust={self.rust}, herhalingen={self.herhalingen},Uitgevoerd={self.uitgevoerd}"
    

    def lijst_dagschema(the_db):
        sqltxt ='SELECT dagid, schemanr, gepland, oefnr, aantal, rust,herhalingen, uitgevoerd from dagschema'
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,)
        result = mycursor.fetchall()
        mycursor.close()
        return[Dagschema(*row) for row in result]
    
    def get_by_dagid(the_db,dagid):
        sqltxt = "SELECT dagid, schemanr, gepland, oefnr, aantal, rust,herhalingen, uitgevoerd from dagschema WHERE dagid like %s"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,(dagid,))
        result = mycursor.fetchone()
        mycursor.close()
        if result:
            return Dagschema(*result)
        else:
            return None
        
    def get_by_gepland(the_db,gepland):
        sqltxt = "SELECT dagid, schemanr, gepland, oefnr, aantal, rust,herhalingen, uitgevoerd from dagschema WHERE gepland like %s"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,(gepland,))
        result = mycursor.fetchone()
        mycursor.close()
        if result:
            return Dagschema(*result)
        else:
            return None
        
    def get_by_schemanr(the_db,schemanr):
        sqltxt = "SELECT dagid, schemanr, gepland, oefnr, aantal, rust,herhalingen, uitgevoerd from dagschema WHERE schemanr like %s"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,(schemanr,))
        result = mycursor.fetchone()
        mycursor.close()
        if result:
            return Dagschema(*result)
        else:
            return None
    