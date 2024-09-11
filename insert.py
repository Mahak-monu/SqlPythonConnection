import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Dashore1299@"
)
mycursor = mydb.cursor()
query = "insert into student (rollno, name, marks, grade, city) values (1, 'amit', 90.7, 'B','Mumbai'), (2, 'billu', 85.6, 'B','Pune'), (3, 'kalu', 60.8, 'C','Mumbai'), (4, 'kanak', 62.4, 'C','Delhi')"
mycursor.execute("use MySchool")
mycursor.execute(query)
mydb.commit()
mydb.close()

