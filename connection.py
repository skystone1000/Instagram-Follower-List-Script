import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Instagram"
)

mycursor = mydb.cursor()

def addFollowed(name,url,userName,posts,followers,following,response):
    ts = datetime.datetime.now()
    sql = "INSERT INTO followedUsers (name,url,userName,posts,followers,following,response,timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    person = (name,url,userName,posts,followers,following,response,ts)
    mycursor.execute(sql,person)
    print("affected rows = {}".format(mycursor.rowcount))
    mydb.commit()


def listFollowers(tableName,followers):
    for user in followers:
        sql = "INSERT INTO " + tableName + " (url) VALUES ('" + user + "')"
        # print(user) 
        mycursor.execute(sql)
        mydb.commit()

def addSingle(tableName, user):
    sql = "INSERT INTO " + tableName + " (url) VALUES ('" + user + "')"
    # print(user) 
    mycursor.execute(sql)
    mydb.commit()

def getDataTable(tableName):
    mycursor.execute("SELECT id,url FROM " + tableName + " LIMIT 100")
    myResult = mycursor.fetchall()
    return myResult


def delUser(tableName,url):
    ts = datetime.datetime.now()
    sql = "DELETE FROM " + tableName + " WHERE url = '" + url + "'" 
    mycursor.execute(sql)
    mydb.commit()

def delUserWithId(tableName,id):
    ts = datetime.datetime.now()
    sql = "DELETE FROM " + tableName + " WHERE id = '" + str(id) + "'" 
    mycursor.execute(sql)
    mydb.commit()

def createTable(name):
    #name = name + 'Followers' 
    try:
        sql = "CREATE TABLE `" + name + "` (`id` int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,`url` varchar(500) NOT NULL )"
        mycursor.execute(sql)
        mydb.commit()
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    
    print("Table created : {0}".format(name))


### SQL FOR followedUsers 
# sql = "CREATE TABLE `" + name + "` (`id` int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,`name` varchar(50) NOT NULL,`url` varchar(500) NOT NULL,`posts` int(5) NOT NULL,`followers` int(10) NOT NULL,`following` int(10) NOT NULL,`response` varchar(5) NOT NULL,`timestamp` datetime NOT NULL DEFAULT current_timestamp())"


# addFollowed("Aditya Mahajan", "https://www.instagram.com/_still.hungry_/","_still.hungry_", 71, 1028, 1274, 0)
# createTable('followedRaw')
#delUser('sggsFollowers','http://google.com')