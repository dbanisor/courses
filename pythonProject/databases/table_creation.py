
# ---------------------------------- CREATING A TABLE IN THE NEW MYSQL DATABASE ----------------------------------

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="mydatabase"  # ---> must add the database name now
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE employee(name varchar(200), salary int(20))")