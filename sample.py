import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Dashore1299@"
)
print("connection string---> ")
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("use library")
mycursor.execute("show tables")
for i in mycursor.fetchall():
    print(i)
mydb.close()


