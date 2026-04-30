from flask import Blueprint, render_template, session

import classes.dbconfig as db
import mysql.connector
from classes.oefening import Oefening 

mydb = db.Connect()



index_bp = Blueprint('index', __name__)
@index_bp.route('/')

def index():
    
    return render_template('index.html')

    

