from config import decideUser,getUser
decideUser()
import functions


currUser = getUser()

if(currUser == "Coding"):
    # functions.followLimited("peopleToFollow")
    functions.unfollowEnemiesLimited()
    # functions.findMyEnemies('skystone1000')
elif(currUser == "Photography"):
    functions.followLimited("peopleToFollow")
    # functions.unfollowEnemiesLimited()
    # functions.findMyEnemies('_still.hungry_')
    # functions.getUserFollowers('https://www.instagram.com/nanded_love/')
    # functions.fileToDb('ans.txt','peopleToFollow')


functions.onComplete()


# _still.hungry_
# skystone1000
# functions.findMyEnemies('skystone1000')

# functions.unfollowEnemiesLimited()
# functions.followLimited("peopleToFollow")

# functions.getUserFollowers('https://www.instagram.com/teamsankalp/')

# functions.deleteEarlierFollowed("peopleToFollow")
# functions.getGroups("https://www.instagram.com/sggs.memes/")

# functions.sggs()
# functions.test()

# functions.fileToDb("unfollowlist.txt","myEnemies")
# functions.fileToDb("sggs.txt","sggsmemes")

# SCRIPT Command crontab
# 49 * * * * export DISPLAY=:0; /opt/lampp/htdocs/github/Instagram-Follower-List-Script/start.sh


######################################################################################3

# Coding
# https://www.instagram.com/coding.maker/
# https://www.instagram.com/tech_monkee_/
# https://www.instagram.com/ludum_elit/
# https://www.instagram.com/tech_with_tim/
# https://www.instagram.com/hambarderahul/
# https://www.instagram.com/tech_monkee_/
# https://www.instagram.com/competitiveprograming/

# Photography
# https://www.instagram.com/a_mateen_as/
# https://www.instagram.com/sggs.memes/
# https://www.instagram.com/nanded_love/
# https://www.instagram.com/love_nanded_mh26/
# https://www.instagram.com/nanded_boys_and_girls/


# REF (Running slenium in cron)
# https://stackoverflow.com/questions/20575751/execute-python-selenium-script-in-crontab
# https://stackoverflow.com/questions/23908319/run-selenium-with-crontab-python