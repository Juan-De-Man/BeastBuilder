import os
import sys
import mysql.connector


from classes.dagschema import *
import classes.dbconfig as db


mydb = db.Connect()

myschema = Dagschema.lijst_dagschema(mydb)
print(myschema)

dagid = Dagschema.get_by_dagid(mydb,2)
print(dagid)

geplandedag = Dagschema.get_by_gepland(mydb,"2026-03-26")
print(geplandedag)

schemanr = Dagschema.get_by_schemanr(mydb,1)
print(schemanr)