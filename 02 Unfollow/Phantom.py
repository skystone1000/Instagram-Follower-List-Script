import instaBot 
import connection
import time
import os
import pandas as pd
from random import randint

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
    


findMyEnemies('_still.hungry_')