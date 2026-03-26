import mysql.connector
from classes.dbconfig import Connect

class Trainingschema:
    def __init__(self,schemanr=None, naam=None, lidnr=None, startdat=None, einddat=None):
        self.schemanr = schemanr
        self.naam = naam
        self.lidnr = lidnr
        self.startdat = startdat
        self.einddat = einddat
    
    def __repr__(self):
        return f"Schema nummer: {self.schemanr}, Naam: {self.naam}, Voor lid nummer: {self.lidnr}, Start Datum: {self.startdat}, Eind Datum: {self.einddat}"
    
    def get_by_schemanr (the_db,schemanr):
        sqltxt = "SELECT schemanr, naam, lidnr, startdat, einddat FROM trainingschema WHERE schemanr like %s"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,(schemanr,))
        result = mycursor.fetchone()
        mycursor.close()
        if result:
            return Trainingschema(*result)
        else:
            return None

    def get_by_naam (the_db,naam):
        sqltxt = "SELECT schemanr, naam, lidnr, startdat, einddat FROM trainingschema WHERE naam like %s"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,(naam,))
        result = mycursor.fetchone()
        mycursor.close()
        if result:
            return Trainingschema(*result)
        else:
            return None
        
    
    
    def lijst_trainingschema(the_db,lidnr):
        sqltxt ='SELECT schemanr, naam, lidnr, startdat, einddat FROM trainingschema WHERE lidnr like %s'
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,(lidnr,))
        result = mycursor.fetchall()
        mycursor.close()
        return[Trainingschema(*row) for row in result]   