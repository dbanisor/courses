
# ---------------------------------- ADDING DATA IN THE NEW MYSQL TABLE ----------------------------------

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="mydatabase"
)

mycursor = mydb.cursor()

sqlform = "Insert into employee(name,salary) values(%s,%s)"
employees = [("Denise", 20000), ("Andrei", 15000), ("Olivia", 90000), ]

mycursor.executemany(sqlform, employees)

mydb.commit()