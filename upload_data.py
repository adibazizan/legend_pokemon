from hashlib import new
from itertools import count
import mysql.connector


HOSTNAME=input()
USERNAME='kathy'
USERPASW=input()
DB_NAME="pokemon"
TAB_NAME="poke_leg"

mydb = mysql.connector.connect(
    host=HOSTNAME,
    user=USERNAME,
    password=USERPASW,
    database = DB_NAME
    )
mycursor = mydb.cursor()
countErr= 0
with open ("C:\\Users\\deeph\\visual_studio_projects\\pokemon_database\\pokemon_true.csv") as data:
    for line in data:
        newPoke = 'INSERT INTO ' + TAB_NAME + " VALUES("
        attribute = line.strip().split(",")
        aux=""
        if attribute[3] == "":
            attribute[3]="-"
        xx = attribute[1]
        attribute[1] = '"'+ xx + '"'
        xx = attribute[2]
        attribute[2]  = '"'+ xx + '"'
        xx = attribute[3]
        attribute[3]  = '"'+ xx + '"'
        for item in attribute:
            if not item  == "#":
                aux = aux + str(item) + ","
        aux =aux[:-1] + ")"
        yy=newPoke + aux
        try:
            mycursor.execute(yy)
            mydb.commit()
            print(newPoke + aux + "OK")
        except:
            countErr = countErr + 1

            print(newPoke + aux)

data.close()

        