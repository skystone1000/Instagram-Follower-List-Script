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


