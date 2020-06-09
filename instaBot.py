from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pickle
from time import sleep, strftime
from random import randint
import re
import connection
import myMeth

"""
    Ref
    Setting user profile
        https://sqa.stackexchange.com/questions/15311/adding-user-data-dir-option-to-chromedriver-makes-it-not-work-and-timeout-only
        https://stackoverflow.com/questions/31062789/how-to-load-default-profile-in-chrome-using-python-selenium-webdriver
"""

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)


class InstagramBot():
    def __init__(self, chromePath, url = "0", session_id = "0" ):
        if (url == "0"):
            self.browserProfile = webdriver.ChromeOptions()
            self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
            self.browserProfile.add_argument("user-data-dir=//home//skystone//.config//google-chrome//")
            self.browser = webdriver.Chrome(chromePath, options=self.browserProfile)
        else:
            self.browserProfile = webdriver.ChromeOptions()
            self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
            #self.browser = webdriver.Chrome(chromePath, chrome_options=self.browserProfile)
            self.browser = webdriver.Remote(command_executor=url,desired_capabilities={})
            self.browser.session_id = session_id
                  
    def initializeUser(self,email,password):
        self.email = email
        self.password = password
        print("User Initialized\n")
        self.browser.get("https://www.instagram.com/")
        value = randint(5, 8)
        time.sleep(value)

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

    def followWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)
        followButton = self.browser.find_element_by_css_selector('button')

        # This is required for private profiles
        if(followButton.text == ''):
            print(followButton.text)
            print("changing button")
            followButton = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/button')

        if (followButton.text != 'Following'):
            followButton.click()
            time.sleep(2)
        else:
            print("You are already following this user")

    def followWithLink(self, link):
        self.browser.get(link)
        time.sleep(2)
           
        ############## Get Name
        ## TO DO  -- when Name field is blank || Name emoji ##
        try:
            name = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/h1').text
            name = emoji_pattern.sub(r'', name)
            # print(name)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            # print(message)
            print("Name element not found")
            return 2
            

        ############## Get UserName
        try:
            userName = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/h2').text
            # userName = myMeth.linkToUsername(link)
            print(userName)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print("UserName element not found || User does not exixt")
            return 3

        ############## Get URL
        url = link
        
        ############## Get Posts
        try:
            posts = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[1]/a/span').text
            posts = re.sub('\D', '', posts)
            posts = int(posts.replace(',',''))
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            posts = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span').text
            posts = int(posts.replace(',',''))
            

        ############## Get Followers
        try:        
            followers = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text
            followers = re.sub('\D', '', followers)
            followers = int(followers.replace(',',''))
            print(followers)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)  
            followers = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/span/span').text
            followers = int(followers.replace(',',''))     

        ############## Get Following
        try: 
            following = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').text
            following = re.sub('\D', '', following)
            following = int(following.replace(',',''))
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            following = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/span/span').text
            following = int(following.replace(',',''))

        ############## Default Response = 0
        response = 0            
        
        ############## Pressing Follow Button
        try:
            followButton = self.browser.find_element_by_css_selector('button')
            # Required for private profiles
            print(followButton.text)
            if(followButton.text == ''):
                print("Follow button changed")
                followButton = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/button')
                print(followButton.text)

            if (followButton.text != 'Message' and followButton.text != 'Requested' and followButton.text != 'Follow Back' ):
                followButton.click()
                connection.addFollowed(name,url,userName,posts,followers,following,response)
                time.sleep(2)
                return 1
            else:
                print("You are already following this user")
                #### TO DELETE after done my followers ##
                # print(name)
                # print(url)
                # print(userName)
                # print(posts)
                # print(followers)
                # print(following)
                # print(response)
                # connection.addFollowed(name,url,userName,posts,followers,following,response)
                time.sleep(2)
                return 0

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            return 4

    def unfollowWithUsername(self, username):
        # self.browser.get('https://www.instagram.com/' + username + '/')
        self.browser.get(username)        
        

        ############## Get Name
        ## TO DO  -- when Name field is blank || Name emoji ##
        try:
            name = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/h1').text
            name = emoji_pattern.sub(r'', name)
            # print(name)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            # print(message)
            print("Name element not found")
            return 2

        followButton = self.browser.find_element_by_css_selector('button')
        # Required for private profiles
        print(followButton.text)
        if(followButton.text == ''):
            print("Follow button changed")
            followButton = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/button')
            print(followButton.text)

        if (followButton.text == 'Message' or followButton.text == 'Following'):
            try:
                unfollowButton = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button/div/span')
                unfollowButton.click()
            except:
                unfollowButton = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/button/div/span')
                print("Unfollow button Chnaged")
                unfollowButton.click()
            time.sleep(2)
            confirmButton = self.browser.find_element_by_xpath('//button[text() = "Unfollow"]')
            confirmButton.click()
            return 1
        else:
            print("You are not following this user")
            return 0


    
    def getUserFollowers(self, username):
        print("\nGetting User {} followers".format(username))
        self.browser.get('https://www.instagram.com/' + username)
        time.sleep(2)

        totalFollowers = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text
        totalFollowers = int(totalFollowers.replace(',',''))
        print("Total Followers user has : {}".format(totalFollowers))
        followersLink = self.browser.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(7)
        followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        #followersList = self.browser.find_element_by_partial_link_text('Follow')        
        
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))        
        followersList.click()
        print("Done sleeping")
        actionChain = webdriver.ActionChains(self.browser)
        while (numberOfFollowersInList < totalFollowers-10):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList,)
            if(numberOfFollowersInList % 4 == 0):
                time.sleep(2)
                print(numberOfFollowersInList,end=" : ")
        
        followers = []
        print("Creating Follower[] List")
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
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
            if(numberOfFollowersInList % 4 == 0):
                time.sleep(2)
                print(numberOfFollowersInList,end=" : ")
        
        following = []
        print("Creating following[] List ...")
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
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


