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
        return (
        f"klant(lidnr={self.lidnr}, voornaam={self.vnaam}, "
        f"naam={self.naam}, geboortejaar={self.geboortejaar}, "
        f"telefoonnummer={self.telnummer}, gewicht={self.gewicht}, "
        f"lengte={self.lengte}, lidstart={self.lidstart}, "
        f"lidstop={self.lidstop}, huisnummer={self.huisnummer}, "
        f"email={self.email}, passwoord={self.passwoord})"
    )

    def get_by_naam (the_db,naam):
        sqltxt = "SELECT lidnr, vnaam, naam, geboortejaar, telnummer, gewicht, lengte, lidstart, lidstop, straat, huisnummer, email, passwoord FROM klant WHERE naam like %s"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,(naam,))
        result = mycursor.fetchone()
        mycursor.close()
        if result:
            return Klant(*result)
        else:
            return None
        
    def get_by_id (the_db,lidnr):
        sqltxt = "SELECT lidnr, vnaam, naam, geboortejaar, telnummer, gewicht, lengte, lidstart, lidstop, straat, huisnummer, email, passwoord FROM klant WHERE lidnr like %s"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,(lidnr,))
        result = mycursor.fetchone()
        mycursor.close()
        if result:
            return Klant(*result)
        else:
            return None


    def lijst_klanten(the_db):
        sqltxt ='SELECT lidnr, vnaam, naam, geboortejaar, telnummer, gewicht, lengte, lidstart, lidstop, straat, huisnummer, email, passwoord FROM klant'
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,)
        result = mycursor.fetchall()
        mycursor.close()
        return[Klant(*row) for row in result]

    def change_pw(self,the_db,pw):
        sqltxt = "UPDATE klant SET passwoord = %s WHERE lidnr = %s"
        self.passwoord = pw
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,(pw,self.lidnr))
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