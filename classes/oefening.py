import mysql.connector
from classes.dbconfig import Connect

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
    