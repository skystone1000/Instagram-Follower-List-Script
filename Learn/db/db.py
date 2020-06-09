"""
Playlist : https://www.youtube.com/playlist?list=PLB5jA40tNf3tRMbTpBA0N7lfDZNLZAa9G

"""

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Instagram"
)

mycursor = mydb.cursor()


# ----------- Tutorial 1 --------------
# Create a Database
#mycursor.execute("CREATE DATABASE Instagram")

mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)


# ----------- Tutorial 2 --------------
# Create Table
#mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")
mycursor.execute("SHOW TABLES")


# ----------- Tutorial 3 --------------
# Populating our table in database

# Single entry
sqlFormula = "INSERT INTO students (name,age) VALUES (%s, %s)"
student1 = ("Aditya", 22)

mycursor.execute(sqlFormula,student1)
mydb.commit()

# Multiple entries
array = [("Atharva", 15),("user1", 11),("User3", 23),("User4", 25)]

mycursor.executemany(sqlFormula, array)
mydb.commit()



# ----------- Tutorial 4 --------------
# Retriving Data

mycursor.execute("SELECT * FROM students")
# Get all entries
myResult = mycursor.fetchall()

mycursor.execute("SELECT * FROM students")
# Get one entry
oneResult = mycursor.fetchone()

print("Printing fetchall( Results : ==========")
for row in myResult:
    print(row)

print("Printing fetchone() results: ==========")
print(oneResult)


# ----------- Tutorial 5 --------------
# Using WHERE query

sql1 = "SELECT * FROM students WHERE age < 17"
sql2 = "SELECT * FROM students WHERE name LIKE '%a%'"
sql = "SELECT * FROM students WHERE name = %s"

mycursor.execute(sql, ("Aditya",))
myresult = mycursor.fetchall()

for result in myresult:
    print(result)


# ----------- Tutorial 6 --------------
# Update Entries 

sql = "UPDATE students SET age = 13 WHERE name = 'Aditya'"
mycursor.execute(sql)
mydb.commit()

# Limiting Queries

mycursor.execute("SELECT * FROM students LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()
for result in myresult:
    print(result)


# ----------- Tutorial 7 --------------
# Ordering

sql = "SELECT * FROM students ORDER BY name DESC" 

# ----------- Tutorial 8 --------------

# Deleting Record
sql = "DELETE FROM students WHERE name = 'Aditya'" 

# Deleting Table
sql = "DROP TABLE IF EXISTS students" 
mycursor.execute(sql)
mydb.commit()
