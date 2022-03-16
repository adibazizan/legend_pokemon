from sqlite3 import dbapi2
import mysql.connector

HOSTNAME="192.168.0.159" #input()
USERNAME='kathy'
USERPASW="galileo2022" #input()
DB_NAME="pokemon"
TAB_NAME="poke_leg"

def create_db():

    mydb = mysql.connector.connect(
    host=HOSTNAME,
    user=USERNAME,
    password=USERPASW)
    mycursor = mydb.cursor()
    x = "CREATE DATABASE " + DB_NAME
    mycursor.execute(x)
    mycursor.execute("SHOW DATABASES")

#if db exist then USE db
#else create_db()
mydb = mysql.connector.connect(
    host=HOSTNAME,
    user=USERNAME,
    password=USERPASW,
    database = DB_NAME
    )
mycursor = mydb.cursor()
cre_tab = "CREATE TABLE " + TAB_NAME + "(id INT, name VARCHAR(50), type_1 VARCHAR(10), type_2 VARCHAR(10), total INT, hp INT, attack INT, defense INT, sp_attack INT, sp_deffend INT, speed INT, generation INT, legendary BOOLEAN)"
mycursor.execute(cre_tab)

mycursor.execute("SHOW TABLES")
