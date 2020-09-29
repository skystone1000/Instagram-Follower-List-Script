
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
#import pandas as pd


# Change this to your own chromedriver path!
chromedriver_path = '/mnt/E4687B61687B3182/CSE/Insta script chromedriver_linux64/Unfollow/chromedriver' 
# Create new window and Maximize
driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(1)
driver.maximize_window()

# Extract Url and Session Id
url = driver.command_executor._url   
session_id = driver.session_id
print(url)
print(session_id)



# Goto Login Page and Fill Details
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)
username = driver.find_element_by_name('username')
username.send_keys('adityaspmahajan@gmail.com')
password = driver.find_element_by_name('password')
password.send_keys('ignatia200')
sleep(2)
password.send_keys(Keys.ENTER)
sleep(3)   

# Goto Profile Page
driver.get('https://www.instagram.com/_still.hungry_/')
"""

# Change this accoding to step1.py
url = 'http://127.0.0.1:51065'
session_id = 'a98986b4cc38c007a112e2b9e80cbf76'

# Connect with the old session
driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.session_id = session_id

"""


username = "_still.hungry_"
maximum = 780

driver.get('https://www.instagram.com/' + username)
followersLink = driver.find_element_by_css_selector('ul li a')
followersLink.click()
sleep(2)
followersList = driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))

followersList.click()
actionChain = webdriver.ActionChains(driver)
i=0
while (numberOfFollowersInList < maximum):
    actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    #actionChain.send_keys(Keys.SPACE).perform()
    numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
    print(numberOfFollowersInList)
    if(i>50):
    	break

followers = []
for user in followersList.find_elements_by_css_selector('li'):
    userLink = user.find_element_by_css_selector('a').get_attribute('href')
    print(userLink)
    followers.append(userLink)
    if (len(followers) == maximum):
        break







"""
followers_dialoge = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]")
n = 1
for i in range(int(allfoll / n)):
	next_length = len(driver.find_elements_by_class_name('FPmhX'))
	if next_length != prev_length:
		new_followers = driver.find_elements_by_class_name('FPmhX')[-12:]


		with open(followers_dir, "a") as followers_file:

			for element in new_followers:
				if element.get_property('href'):
					title = element.get_property('title')
					href = element.get_property('href')
					followers_file.write(title + "," + href + "," + "\n")

"""