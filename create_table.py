import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Dashore1299@"
)
mycursor = mydb.cursor()
query = "create table student(rollno int primary key, name varchar(20) not null, marks float, grade char(1), city varchar(20))"
mycursor.execute("use MySchool")
mycursor.execute(query)
mydb.close()