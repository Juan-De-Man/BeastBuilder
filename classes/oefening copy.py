import mysql.connector
from classes.dbconfig import Connect

# klasse voor oefeningen

class Oefening:
    def __init__(self,oefnr=None, naam = None,spier=None, moeilijkheidsgraad= None, beschrijving =None, instructie= None):
        self.oefnr = oefnr
        self.naam = naam
        self.spier = spier
        self.moeilijkheidsgraad= moeilijkheidsgraad
        self.beschrijving = beschrijving
        self.instructie = instructie

    def __repr__(self):
        return f"Oefnummer = {self.oefnr}, naam = {self.naam}, spier = {self.spier}, moeilijkheidsgraad= {self.moeilijkheidsgraad}, beschrijving = {self.beschrijving}, instructie = {self.instructie}"
    
    def lijst_oefeningen(the_db):
        sqltxt ='Select oefnr, naam, spier, moeilijkheidsgraad, beschrijving, instructie from oefening'
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,)
        result = mycursor.fetchall()
        mycursor.close()
        return[Oefening(*row) for row in result]
    
    def get_by_nr(the_db,oefnr):
        sqltxt = "SELECT oefnr, naam, spier, moeilijkheidsgraad, beschrijving, instructie FROM oefening WHERE oefnr like %s"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,(oefnr,))
        result = mycursor.fetchone()
        mycursor.close()
        if result:
            return Oefening(*result)
        else:
            return None
        
    def get_by_moeilijkheidsgraad(the_db, moeilijkheidsgraad):
        sqltxt ='Select oefnr, naam, spier, moeilijkheidsgraad, beschrijving, instructie from oefening where moeilijkheidsgraad like %s'
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,(moeilijkheidsgraad,))
        result = mycursor.fetchall()
        mycursor.close()
        return[Oefening(*row) for row in result]
 

    
