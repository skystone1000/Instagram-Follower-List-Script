import instaBot 
import connection
import time
import os
import pandas as pd
from random import randint

# INITIALIZATION ---------------------------
bot = instaBot.InstagramBot()
bot.initializeUser('email','password')
bot.extractSession()
connection.createLogTable('Logs')
connection.addLog("Logs", "follow limited")
# INITIALIZATION END ---------------------------


## INCOMPLETE  Casuing problems in some
# Check last digit == n
def linkToUsername(link):
    # Check if '\n' is present at last
    # link = link[:-2]
    """
    print(link[-3:])
    if(link[-2:] == '\n'):
        link = link[:-2]
        print('present')
    """
    
    link = link[::-1] #Reverse UserLink
    userName = ''
    for letter in range(1,len(link)):
        if(link[letter] == '/'):
            break
        userName = userName + link[letter]
    userName = userName[::-1]
    # print(userName)
    return userName

## COMPLETE
def fileToDb(fileName,tableName):
    f = open(fileName, "r")
    count = 0
    for person in f:
        connection.addSingle(tableName,person)
        if (count % 50 == 0):
            print("Count = {}".format(count))
            time.sleep(2)
        count = count + 1
    f.close()

## COMPLETE
def listToFile(listToAdd,fileName):
    f = open(fileName, "w")
    for person in listToAdd:
        #print(person)
        f.write(person+"\n")
    f.close()

def onComplete():
    bot.closeBrowser()

############################################################################################

## COMPLETE
def followLimited(tableName):
    followedCount = 0
    MAX_PEOPLE_TO_FOLLOW = randint(60, 80)
    peopleToFollow = connection.getDataTable(tableName)
    for i in range(0,len(peopleToFollow)):
        print("Loop Count = {}".format(i))
        timeToSleep = randint(10, 20)
        time.sleep(timeToSleep)

        userUrl = peopleToFollow[i][1]
        
        val = bot.followWithLink(userUrl)
        # print(val)     

        ## There is to change after sggs memes ##
        if(val == 0):
            connection.delUser(tableName,userUrl)
            print("Already Following")

        if(val == 1):
            connection.delUser(tableName,userUrl)
            print("User added to followed people")
            followedCount = followedCount + 1
            # To remove once followed (Helpful in removing duplicate)    
            connection.addSingle("followedRaw",userUrl)

        if(val == 2):
            connection.addSingle("nameEmoji",userUrl)
            connection.delUser(tableName,userUrl)
            print("User moved to nameEmoji || Name is not present")
            # To remove once followed (Helpful in removing duplicate)    
            connection.addSingle("followedRaw",userUrl)


        if(val == 3):
            connection.delUser(tableName,userUrl)
            print("User does not exist || Username Changed")
            # To remove once followed (Helpful in removing duplicate)    
            connection.addSingle("followedRaw",userUrl)

        if(val == 4):
            print("Follow button Xpath did not match")

        if(val == 5):
            print("Explicit reason")
        
        if(followedCount > 25):
            print("Completed Following 25 people")
            break

        if(i > MAX_PEOPLE_TO_FOLLOW):
            print("{} profile visits done".format(MAX_PEOPLE_TO_FOLLOW))
            break
        
        print("People Followed now : {0}".format(followedCount))    
        print("================================================")

# INCOMPLETE
def unfollowEnemiesLimited():
    unfollowedCount = 0
    MAX_PEOPLE_TO_VISIT = randint(60, 80)
    tableName = "myEnemies"
    peopleToUnfollow = connection.getDataTable(tableName)
    for i in range(0,len(peopleToUnfollow)):
        print("Loop Count = {}".format(i))
        timeToSleep = randint(20, 30)
        time.sleep(timeToSleep)

        userName = peopleToUnfollow[i][1]
        # userUrl = "https://www.instagram.com/" + userName + "/"

        val = bot.unfollowWithUsername(userName)
        # print(val)     

        if(val == 0):
            connection.delUser(tableName,userName)
            print("Not Following")

        if(val == 1):
            connection.delUser(tableName,userName)
            print("Unfollowed {}".format(userName))
            unfollowedCount = unfollowedCount + 1

        if(val == 2):
            connection.delUser(tableName,userName)
            print("UserName Does not exist")

        if(unfollowedCount > 30):
            print("Completed UnFollowing 25 people")
            break

        if(i > MAX_PEOPLE_TO_VISIT):
            print("{} profile visits done".format(MAX_PEOPLE_TO_VISIT))
            break
        
        print("People UnFollowed now : {0}".format(unfollowedCount))    
        print("================================================")

    
## COMPLETE From Phantom Generated CSVs
def findMyEnemies(userName):
    followerDf = pd.read_csv("Followers my.csv")
    followingDf = pd.read_csv("Following my.csv")
    followers = followerDf['username'].tolist()
    following = followingDf['username'].tolist()

    f = open("whitelist.txt", "r")
    whiteList = []
    for person in f:
        person = person[:-1]
        whiteList.append(person)
    # print(whiteList)

    print("\n\n")
    print("nonFollowers : \n")
    nonFollowers = 0
    doNotFollowBack = ['Not Following Back']

    f = open("unfollowlist.txt", "w")
    for person in following:
        if (person in followers):
            continue
        elif(person in whiteList):
            continue
        else:
            # print(person)
            f.write(person+"\n")
            doNotFollowBack.append(person)
            nonFollowers += 1 
    f.close()
    
    print("Total People Who Dont Follow back : {}".format(nonFollowers))
    print("Adding to database")
    try:
        connection.createTable("myEnemies")
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)

    fileToDb("unfollowlist.txt","myEnemies")
    if os.path.exists("unfollowlist.txt"):
        os.remove("unfollowlist.txt")
    else:
        print("The file does not exist") 

## COMPLETE
def getUserFollowers(link):
    """
    tableName = userName.replace('.','')
    tableName = "followers" + tableName.capitalize()
    """
    userName = linkToUsername(link)
    tableName = "peopleToFollow"
    
    try:
        connection.createTable(tableName)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        
    followers = bot.getUserFollowers(userName)

    fileName = tableName + "Temp.txt"
    listToFile(followers,fileName)    

    print("Created file {}".format(fileName))
    print("Writitng file to Db")
    fileToDb(fileName,tableName)

    # print("Adding to database")
    time.sleep(2)
    # connection.listFollowers(tableName,followers)

## Group Following
def getUserFollowing(link):
    userName = linkToUsername(link)
    tableName = userName.replace('.','')
    tableName = "groups" + tableName.capitalize()
    try:
        connection.createTable(tableName)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)

    followers = bot.getUserFollowing(userName)

    fileName = tableName + "Temp.txt"
    listToFile(followers,fileName)    

    print("Created file {}".format(fileName))
    print("Writitng file to Db")
    fileToDb(fileName,tableName)


    # INCOMPLETE

## Not able to delete all the followed users (Find reason:name blank,emoji in name)
def deleteEarlierFollowed(tableName):
    earlierFollowed = connection.getDataTable("followedUsers")
    earlierFollowedList = []
    earlierFollowedUname = []
    # Uname = ''
    loopcount = 0
    for record in earlierFollowed:
        earlierFollowedList.append(record[1])
        Uname = linkToUsername(record[1])
        earlierFollowedUname.append(Uname)

    checkList = connection.getDataTable(tableName) 
    deletedCount = 0
    print("deletedCount = {}".format(deletedCount),end=", ")
    for i in range(0,len(checkList)):
        
        # Match Link
        if(checkList[i][1] in earlierFollowedList):
            deletedCount = deletedCount + 1
            print("deletedCount = {}".format(deletedCount))
            id = checkList[i][0]
            connection.delUserWithId(tableName,id)
            print("{}".format(deletedCount),end=", ")
            

        ## Match to check username
        checkUserName = linkToUsername(checkList[i][1])
        print(checkUserName)
        if(checkUserName in earlierFollowedUname):
            deletedCount = deletedCount + 1
            print("deletedCount = {}".format(deletedCount))
            id = checkList[i][0]
            connection.delUserWithId(tableName,id)
            print("{}".format(deletedCount),end=", ")


####################################################

## COMPLETE
def findMyEnemiesOld(userName):
    followers = ['Followers']
    followers = bot.getUserFollowers(userName)
    following = ['Following']
    following = bot.getUserFollowing(userName)

    print("\n\n")
    print("nonFollowers : \n")
    nonFollowers = 0
    doNotFollowBack = ['Not Following Back']

    f = open("unfollowlist.txt", "w")
    for person in following:
        if (person in followers):
            continue
        else:
            # print(person)
            f.write(person+"\n")
            doNotFollowBack.append(person)
            nonFollowers += 1 
    f.close()

    print("Total People Who Dont Follow back : {}".format(nonFollowers))
    print("Adding to database")
    try:
        connection.createTable("myEnemies")
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)

    fileToDb("unfollowlist.txt","myEnemies")
    if os.path.exists("unfollowlist.txt"):
        os.remove("unfollowlist.txt")
    else:
        print("The file does not exist") 


def followFromFile():
    followedCount = 0
    f = open("sggs.txt", "r")
    for person in f:
        followedCount = bot.followWithLink(person,followedCount)
        print("Follow Count = {}" .format(followedCount))
        if followedCount > 25:
            break
    f.close()

def UsingLastSession():
    # If you want to continue a previous open session
    url = 'http://127.0.0.1:12551'
    session_id = '09d7b2e41adeacafba34111ed1b0f026'

    #bot = InstagramBot(chromePath, url, session_id)

    bot.initializeUser('email','password')
    bot.extractSession()
    #bot.signIn()
