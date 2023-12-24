
# ---------------------------------- CONNECTING TO THE MYSQL DATABASE ----------------------------------

import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345"
)

print(mydb)

if mydb:
  print("Connection successful")
else:
  print("Connection unsuccessful")
