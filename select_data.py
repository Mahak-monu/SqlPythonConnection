import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Dashore1299@"
)
mycursor = mydb.cursor()
query = "select * from student"
mycursor.execute("use MySchool")
mycursor.execute(query)
for i in mycursor.fetchall():
    print(i)
mydb.close()