import os
import sys
import mysql.connector


from classes.trainingschema import *
import classes.dbconfig as db


mydb = db.Connect()

myKlant = Trainingschema.get_by_naam(mydb,'Start Week')
print (myKlant)


myKlant = Trainingschema.get_by_schemanr(mydb,2)
print(myKlant)

myKlant = Trainingschema.lijst_trainingschema(mydb,1)
print(myKlant)