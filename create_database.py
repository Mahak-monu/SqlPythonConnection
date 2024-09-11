import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Dashore1299@"
)
mycursor = mydb.cursor()
print(mydb)
query = "create database if not exist MySchool"
mycursor.execute(query)
mydb.close()

