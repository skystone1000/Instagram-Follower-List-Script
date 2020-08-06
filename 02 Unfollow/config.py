from datetime import datetime

# Change Chrome Driver Path Here
# chromePath = '/mnt/E4687B61687B3182/CSE/Insta script/Unfollow/chromedriver'

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
    # slot1 = ['01','03','05','07','09','11','13','15','17','19','21','23','2','4','6','8','10','12','14','16','18','20','22']
    slot1 = ['01','03','05','07','09','11','13','15','17','19','21','23']
    slot2 = ['02','04','06','08','10','12','14','16','18','20','22']
    if(currentHour in slot2):
        print("Photography User Selected")
        setUser("Photography")
    elif(currentHour in slot1):
        print("Coding User Selected")
        setUser("Coding")
    else:
        print("Exiting")
        setUser("Null")
