import os
import sys
import mysql.connector


from classes.klant import *
import classes.dbconfig as db


mydb = db.Connect()

myKlant = Klant.get_by_naam(mydb,'De Coster')
print (myKlant)


myKlant.change_pw(mydb,'99')

print(myKlant)

myKlant = Klant.lijst_klanten(mydb)
print(myKlant)

myKlant = Klant.get_by_id(mydb,2)
print(myKlant)