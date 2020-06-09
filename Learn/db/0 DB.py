"""
Playlist : https://www.youtube.com/playlist?list=PLB5jA40tNf3tRMbTpBA0N7lfDZNLZAa9G

"""

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

mycursor = mydb.cursor()

mycursor.execute("select * from test")
result = mycursor.fetchone()

for i in result:
    print(i)
