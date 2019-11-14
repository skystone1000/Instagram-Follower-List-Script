from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pickle
from time import sleep, strftime
from random import randint

class InstagramBot():
    def __init__(self, chromePath, url = "0", session_id = "0" ):
        if (url == "0"):
            self.browserProfile = webdriver.ChromeOptions()
            self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
            self.browser = webdriver.Chrome(chromePath, chrome_options=self.browserProfile)
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
        password.send_keys('password')
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
        totalFollowers = int(self.browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[2]/a/span').text)
        print("Total Followers user has : {}".format(totalFollowers))
        followersLink = self.browser.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(2)
        followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
    
        loopCount = 0
        followersList.click()
        actionChain = webdriver.ActionChains(self.browser)
        while (numberOfFollowersInList < totalFollowers):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            loopCount +=1
            if(loopCount > 5000):
                print("Loop Count Excedded {}".format(loopCount))
                break
            if(numberOfFollowersInList % 4 == 0):
                print(numberOfFollowersInList,end=" : ")
        
        loopCount = 0
        followers = []
        print("Creating Follower[] List")
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            print(".",end=" ")
            #print(userLink)
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
            loopCount +=1
            if(loopCount > 5000):
                print("Loop Count Excedded {}".format(loopCount))
                break
            if (len(followers) == totalFollowers):
                break
        return followers

    def getUserFollowing(self, username):
        print("\nGetting User {} followings".format(username))
        self.browser.get('https://www.instagram.com/' + username)
        totalFollowing = int(self.browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[3]/a/span').text)
        print("User Following Count : {}".format(totalFollowing))
        time.sleep(3)
        #followersLink = self.browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[3]/a')
        followersLink = self.browser.find_element_by_partial_link_text('following')
        followersLink.click()
        time.sleep(2)
        followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
    
        followersList.click()
        actionChain = webdriver.ActionChains(self.browser)
        loopCount = 0 
        while (numberOfFollowersInList < totalFollowing):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            loopCount +=1
            if(loopCount > 2000):
                print("Loop Count Excedded {}".format(loopCount))
                break
            if(numberOfFollowersInList % 4 == 0):
                print(numberOfFollowersInList,end=" : ")
        
        loopCount = 0
        following = []
        print("Creating following[] List ...")
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            print(".",end=" ")
            #print(userLink)
            following.append(userLink)
            loopCount +=1
            if(loopCount > 5000):
                print("Loop Count Excedded {}".format(loopCount))
                break
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

    def test(self):
        username = '_still.hungary_'
        self.browser.get('https://www.instagram.com/' + username + '/')

    def __exit__(self, exc_type, exc_value, traceback):
        self.closeBrowser()

# Change Chrome Driver Path Here
chromePath = '/mnt/E4687B61687B3182/CSE/Insta script chromedriver_linux64/Unfollow/chromedriver'

# If you want to continue a previous open session
url = 'http://127.0.0.1:41347'
session_id = 'a59757fdb3ff9a31dab76e8bcbdf609c'

bot = InstagramBot(chromePath)
#bot = InstagramBot(chromePath, url, session_id)

bot.initializeUser('email','password')
bot.extractSession()
bot.signIn()


followers = ['Followers']
followers = bot.getUserFollowers('_still.hungry_')

following = ['Following']
following = bot.getUserFollowing('_still.hungry_')

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
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


print("Unfollowing Peoples")

for i in range(1,10):
    bot.unfollowWithUsername(doNotFollowBack[i])

#unfollowWithUsername(person)
"""

bot.unfollowWithFile('unfollowlist.txt')
"""
