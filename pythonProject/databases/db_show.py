
# ---------------------------------- CHECKING THE EXISTENCE OF ANY MYSQL DATABASE ----------------------------------

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for db in mycursor:
  print(db)