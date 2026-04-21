import os
import sys
import mysql.connector


import classes.klant as kla
import classes.dbconfig as db


mydb = db.Connect()

myKlant = kla.get_by_naam(mydb,'Jola%')
print (myKlant)