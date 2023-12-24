# ---------------------------------- SHOWING ALL TABLES IN THE NEW MYSQL DATABASE ----------------------------------

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)


