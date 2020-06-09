#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 00:17:45 2019

@author: skystone
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 21:22:49 2019

@author: skystone
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
#import pandas as pd

chromedriver_path = '/mnt/E4687B61687B3182/CSE/Insta script chromedriver_linux64/Unfollow/chromedriver' # Change this to your own chromedriver path!

"""
driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(1)

#driver.maximize_window()
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)
    
username = driver.find_element_by_name('username')
username.send_keys('adityaspmahajan@gmail.com')
password = driver.find_element_by_name('password')
password.send_keys('ignatia200')
sleep(2)
password.send_keys(Keys.ENTER)


sleep(3)   

"""

url = 'http://127.0.0.1:59571'
session_id = 'c7be6b18960a0fd93238b318e527c90d'


driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.session_id = session_id


# url = driver.command_executor._url   
# session_id = driver.session_id
# print(url)
# print(session_id)



  

driver.get('https://www.instagram.com/_still.hungry_/')
totalFollowers = 0
followersList = ['Follower Names']
totalFollowers = int(driver.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[2]/a/span').text)
print(totalFollowers)

followers = driver.find_element_by_partial_link_text('followers')
followers.click()

sleep(3)


divToScroll = driver.find_element_by_class_name('isgrP')


for i in range(totalFollowers):
	
	    if(i%12 == 0):
	        sleep(5)
       		driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', divToScroll)
	    string = str('/html/body/div[3]/div/div[2]/ul/div/li[{}]/div/div[2]/div[1]/div/div/a'.format(i+1))
	    username = driver.find_element_by_xpath(string).text
	    #followersList.append[username]
	    print(username)
	
		

