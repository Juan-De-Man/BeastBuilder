import os
import sys
import mysql.connector


from classes.motivatie import *
import classes.dbconfig as db


mydb = db.Connect()

myMotivatie = Motivatie.get_by_motivatienr(mydb,1)
print(myMotivatie)