from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
#import pandas as pd

# Change this accoding to step1.py
url = 'http://127.0.0.1:41579'
session_id = '04ed7369ee8ffc8abc158b9bdb4407ee'

# Connect with the old session
driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.session_id = session_id

# Goto Profile Page
driver.get('https://www.instagram.com/_still.hungry_/')
sleep(3)

# List for followers
followersList = ['Follower Names']

# Followers Count
totalFollowers = 0
totalFollowers = int(driver.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[2]/a/span').text)

# Open Div 
followers = driver.find_element_by_partial_link_text('followers')
followers.click()
sleep(3)

# ID to scroll the div of followers
divToScroll = driver.find_element_by_class_name('isgrP')
for i in range(1,totalFollowers):
	try:
		print(i)
		if(i%13 == 0):
			#driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', divToScroll)
			driver.execute_script('arguments[0].scrollTop = (arguments[0].scrollHeight)/{}'.format(i-8), divToScroll)
			sleep(6)
		sleep(1)
		string = str('/html/body/div[3]/div/div[2]/ul/div/li[{}]/div/div[2]/div[1]/div/div/a'.format(i))
		username = driver.find_element_by_xpath(string).text
		#followersList.append[username]
		print(username)
	except:
		continue
