
# ---------------------------------- READING DATA FROM THE NEW MYSQL TABLE ----------------------------------

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="mydatabase"
)

mycursor = mydb.cursor()
####################################### The part below only fetches on field #######################################
# mycursor.execute("Select name from employee")
# myresult = mycursor.fetchone()
#
# for row in myresult:
#     print(row)
####################################### ----------------end----------------- #######################################

################################### The part below only fetches the entire tuple ###################################
mycursor.execute("Select * from employee")
myresult = mycursor.fetchall()

for row in myresult:
    print(row)
####################################### ----------------end----------------- #######################################

