from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pickle
from time import sleep, strftime
from random import randint

"""
    Ref
    Setting user profile
        https://sqa.stackexchange.com/questions/15311/adding-user-data-dir-option-to-chromedriver-makes-it-not-work-and-timeout-only
        https://stackoverflow.com/questions/31062789/how-to-load-default-profile-in-chrome-using-python-selenium-webdriver
"""


class InstagramBot():
    def __init__(self, chromePath, url = "0", session_id = "0" ):
        if (url == "0"):
            self.browserProfile = webdriver.ChromeOptions()
            self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
            self.browserProfile.add_argument("user-data-dir=//home//skystone//.config//google-chrome//")
            self.browser = webdriver.Chrome(chromePath, options=self.browserProfile)

            # Initializing cookies
            """
            cookies = pickle.load(open("cookies.pkl", "rb"))
            for cookie in cookies:
                self.browser.add_cookie(cookie)
            """
        else:
            self.browserProfile = webdriver.ChromeOptions()
            self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
            #self.browser = webdriver.Chrome(chromePath, chrome_options=self.browserProfile)
            self.browser = webdriver.Remote(command_executor=url,desired_capabilities={})
            self.browser.session_id = session_id
            # Initializing cookies
            """
            cookies = pickle.load(open("cookies.pkl", "rb"))
			for cookie in cookies:
			    self.browser.add_cookie(cookie)
			"""
                  
    def initializeUser(self,email,password):
        self.email = email
        self.password = password
        print("User Initialized\n")

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        sleep(2)
        username = self.browser.find_element_by_name('username')
        username.send_keys('adityaspmahajan@gmail.com')
        password = self.browser.find_element_by_name('password')
        password.send_keys('pass')
        sleep(2)
        password.send_keys(Keys.ENTER)
        print("SignIn Done")
        sleep(3)
        pickle.dump( self.browser.get_cookies() , open("cookies.pkl","wb"))
        print("Cookies written to file")

    def followWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text != 'Following'):
            followButton.click()
            time.sleep(2)
        else:
            print("You are already following this user")

    def followWithLink(self, link, followedCount):
        self.browser.get(link)
        time.sleep(2)
        try:
            #if follow is not present it will throw an exception
            #followButton = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/button')
            followButton = self.browser.find_element_by_css_selector('button')
            #print(followButton).value
            if (followButton.text == 'Follow'):
                followButton.click()
                followedCount = followedCount + 1
                time.sleep(2)
                return followedCount
            else:
                print("You are already following this user")
                return followedCount
        except:
            return followedCount

    def unfollowWithUsername(self, username):
        #self.browser.get('https://www.instagram.com/' + username + '/')
        self.browser.get(username)        
        time.sleep(15)
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text == 'Following'):
            followButton.click()
            time.sleep(2)
            confirmButton = self.browser.find_element_by_xpath('//button[text() = "Unfollow"]')
            confirmButton.click()
        else:
            print("You are not following this user")




    def unfollowWithFile(self, fileName):
        f = open(fileName, "r")
        count = 0
        for username in f:
        	#count+=1
        	#if (count > 20):
        	#	break
            self.browser.get(username)        
            time.sleep(10)
            loopCount = 0
            if (loopCount > 15):
            	break

            followButton = self.browser.find_element_by_css_selector('button')
            if (followButton.text == 'Following'):
                followButton.click()
                time.sleep(2)
                confirmButton = self.browser.find_element_by_xpath('//button[text() = "Unfollow"]')
                confirmButton.click()
            else:
                print("You are not following this user")
    
    def getUserFollowers(self, username):
        print("\nGetting User {} followers".format(username))
        self.browser.get('https://www.instagram.com/' + username)
        time.sleep(2)

        totalFollowers = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text
        totalFollowers = int(totalFollowers.replace(',',''))
        print("Total Followers user has : {}".format(totalFollowers))
        followersLink = self.browser.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(5)
        followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        #followersList = self.browser.find_element_by_partial_link_text('Follow')        
        
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))        
        followersList.click()
        print("DOne sleeping")
        actionChain = webdriver.ActionChains(self.browser)
        while (numberOfFollowersInList < totalFollowers-10):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList,)
            if(numberOfFollowersInList % 4 == 0):
                print(numberOfFollowersInList,end=" : ")
        
        followers = []
        print("Creating Follower[] List")
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            print(userLink)
            """
                userLink = userLink[::-1] #Reverse UserLink
                userName = ''
                for letter in range(1,len(userLink)):
                    if(letter == '/'):
                        break
                    userName += letter
                print(userName)
                followers.append(userName)
            """
            followers.append(userLink)
            if (len(followers) == totalFollowers):
                break
        return followers

    def getUserFollowing(self, username):
        print("\nGetting User {} followings".format(username))
        self.browser.get('https://www.instagram.com/' + username)
        totalFollowing = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').text
        totalFollowing = int(totalFollowing.replace(',',''))
        print("User Following Count : {}".format(totalFollowing))
        time.sleep(2)
        #followersLink = self.browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[3]/a')
        followersLink = self.browser.find_element_by_partial_link_text('following')
        followersLink.click()
        time.sleep(2)
        followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
    
        followersList.click()
        actionChain = webdriver.ActionChains(self.browser)
        while (numberOfFollowersInList < totalFollowing-10):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)
        
        following = []
        print("Creating following[] List ...")
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            #print(".",end=" ")
            print(userLink)
            following.append(userLink)
            if (len(following) == totalFollowing):
                break
        return following

    def closeBrowser(self):
        self.browser.close()

    # Extract Url and Session Id
    def extractSession(self):
        print("Session Details :")
        url = self.browser.command_executor._url   
        session_id = self.browser.session_id
        print("url : {}".format(url))
        print("session_id : {}".format(session_id))
   
    def __exit__(self, exc_type, exc_value, traceback):
        self.closeBrowser()





def findMyEnemies():
    followers = ['Followers']
    followers = bot.getUserFollowers('_still.hungry_')

    following = ['Following']
    following = bot.getUserFollowing('_still.hungry_')

    print("\n\n")
    print("nonFollowers : \n")
    nonFollowers = 0
    doNotFollowBack = ['Not Following Back']

    f = open("unfollowlist.txt", "w")
    for person in following:
        if (person in followers):
            continue
        else:
            print(person)
            f.write(person+"\n")
            doNotFollowBack.append(person)
            nonFollowers += 1 
    f.close()

    print("Total People Who Dont Follow back : {}".format(nonFollowers))



def sggs():
    followers = ['Followers']
    followers = bot.getUserFollowers('sggs.memes')

    print("\n\n")

    f = open("sggs.txt", "w")
    for person in followers:
        print(person)
        f.write(person+"\n")
    f.close()

    print("Created file sggs")


def followLimited():
    followedCount = 0
    f = open("sggs.txt", "r")
    nf = open("sggsFollowed.txt", "a")
    for person in f:
        nf.write(person)
        followedCount = bot.followWithLink(person,followedCount)
        print("Follow Count = {}" .format(followedCount))
        if followedCount > 25:
            break

    f.close()




# Change Chrome Driver Path Here
chromePath = '/mnt/E4687B61687B3182/CSE/Insta script/Unfollow/chromedriver'

"""
# If you want to continue a previous open session
url = 'http://127.0.0.1:12551'
session_id = '09d7b2e41adeacafba34111ed1b0f026'

#bot = InstagramBot(chromePath, url, session_id)

bot.initializeUser('email','password')
bot.extractSession()
#bot.signIn()
"""

bot = InstagramBot(chromePath)
bot.initializeUser('email','password')
bot.extractSession()

#findMyEnemies()
#sggs()
followLimited()

"""
print("Unfollowing Peoples")

for i in range(1,10):
    bot.unfollowWithUsername(doNotFollowBack[i])

#unfollowWithUsername(person)


bot.unfollowWithFile('unfollowlist.txt')
"""