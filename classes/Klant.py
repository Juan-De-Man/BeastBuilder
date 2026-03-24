import mysql.connector
from classes.dbconfig import Connect

class Klant():
    def __init__(self,lidnr=None,vnaam=None,naam=None,geboortejaar=None,telnummer=None,gewicht=None,lengte=None,lidstart=None,lidstop=None,straat=None,huisnummer=None,email=None,passwoord = None):
        self.lidnr= lidnr
        self.vnaam = vnaam
        self.naam = naam
        self.geboortejaar = geboortejaar
        self.telnummer = telnummer
        self.gewicht = gewicht
        self.lengte = lengte
        self.lidstart = lidstart
        self.lidstop = lidstop
        self.straat = straat
        self.huisnummer = huisnummer
        self.email = email
        self.passwoord = passwoord

    #Weergeven van de gegevens(representen)
    def __repr__(self):
        return f'Klant(lidnr={self.lidnr},voornaam={self.vnaam},\
            naam={self.naam},geboortejaar={self.geboortejaar},telefoonnummer={self.telnummer},gewicht={self.gewicht},\
            lengte={self.lengte},lidstart={self.lidstart},lidstop={self.lidstop},huisnummer={self.huisnummer},email={self.email})'
    
    def get_by_naam (the_db,naam):
        sqltxt = "SELECT lidnr, naam, passwoord, email FROM klant WHERE naam like %s"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,(naam,))
        result = mycursor.fetchone()
        mycursor.close()
        if result:
            return Klant(*result)
        else:
            return None



    def change_pw(the_db,naam,pw):
        sqltxt = "UPDATE klant SET passwoord = %s WHERE naam = %s"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,(pw,naam))
        the_db.mydb.commit()
        mycursor.close()


if __name__ == "__main__":
    mydb = Connect()
    try:
        my_user = Klant.get_by_naam(mydb,"Jolan")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    print(my_user)
    mydb.close()