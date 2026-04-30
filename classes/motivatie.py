import mysql.connector
from classes.dbconfig import Connect

class Motivatie:
    def __init__(self, motivid=None, tekst=None):
        self.motivid = motivid
        self.tekst =tekst

    def __repr__(self):
        return f" Motivatie ID ={self.motivid}, Motivatie = {self.tekst}"
    
    def get_by_motivatienr(the_db, motivid):
        sqltxt = "SELECT motivid, tekst FROM motivatie WHERE motivid like %s"
        mycursor = the_db.cursor()
        mycursor.execute(sqltxt,(motivid,))
        result = mycursor.fetchone()
        mycursor.close()
        if result:
            return Motivatie(*result)
        else:
            return None