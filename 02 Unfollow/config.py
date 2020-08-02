from datetime import datetime

# Change Chrome Driver Path Here
chromePath = '/mnt/E4687B61687B3182/CSE/Insta script/Unfollow/chromedriver'

def getUser():
    f = open("User.txt", "r")
    user = f.readline()
    f.close()
    return user

def setUser(user):
    f = open("User.txt", "w")
    f.write(user)
    f.close()

def decideUser():
    now = datetime.now()
    currentHour = now.strftime("%H")
    print("Current Hour =", currentHour)
    slot2 = ['1','3','5','7','9','11','13','15','17','19','21']#,'23']
    slot1 = ['2','4','6','8','10','12','14','16','18','20','22']
    if(currentHour in slot1):
        print("Photography User Selected")
        setUser("Photography")
    elif(currentHour in slot2):
        print("Coding User Selected")
        setUser("Coding")
    else:
        print("Exiting")
        setUser("Null")
