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
import pandas as pd

chromedriver_path = '/home/skystone/Documents/chromedriver' # Change this to your own chromedriver path!

# 'photography' ,'naturephotography','love' ,'travelblog', 'travelblogger', 'traveler','roads' ,'photooftheday', 'follow' ,  'photography'  ,'happy','cachorro','adoptdontshop','picoftheday' ,'petsofinstagram','art',
hashtag_list = [ 'sunset','photography','landscape' ]#,'travel' ,'photooftheday' ,'instagood' ,'beautiful' ,'landscape' ,'art' ,'picoftheday' ,'sky' ,'photo' ,'like' ,'sunset' ,'instagram' ,'naturelovers' ,'spring' ,'sun', 'follow' ,'ig' ,'flowers' ,'life','nature', 'sunset'  ,'travelphotography', 'sea' ,'beauty' ,'happy' ,'beach','adventure' ,'bhfyp' , 'green', 'wildlife', 'photographer', 'mountains', 'fun', 'fashion', 'cute', 'clouds', 'wanderlust', 'bhfyp', 'animals', 'followme', 'smile', 'instadaily', 'amazing', 'outdoors', 'explore', 'hiking', 'style', 'water', 'friends', 'landscapephotography', 'forest', 'tree', 'me', 'travelgram', 'canon', 'trees', 'birds', 'dog']

prev_user_list = [] 
#- if it's the first time you run it, use this line and comment the two below

#prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2] # useful to build a user log
#prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0







driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(1)
driver.maximize_window()
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)
    
username = driver.find_element_by_name('username')
username.send_keys('email@gmail.com')
password = driver.find_element_by_name('password')
password.send_keys('p@sswor(|')
sleep(2)
password.send_keys(Keys.ENTER)
#button_login = driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > button')
#button_login.click()

sleep(3)
        
#notnow = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
#notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications
  




for hashtag in hashtag_list:
    
    tag += 1
    driver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    sleep(1)
    first_thumbnail = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    
    first_thumbnail.click()
    sleep(1)  
    
    try:        
        for x in range(1,1000):
            try:
                username = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text
                print(username)
                if username not in prev_user_list:
                    # If we already follow, do not unfollow
                    if driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                        
                        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                        
                        new_followed.append(username)
                        followed += 1
    
                        # Liking the picture
                        button_like = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')
                        
                        button_like.click()
                        likes += 1
                        sleep(2)
    
                        # Comments and tracker
                        comm_prob = randint(1,10)
                        print('{}_{}: {}'.format(hashtag, x,comm_prob))
                        if comm_prob > 2:
                            comments += 1
                            driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[3]/div/form/textarea').click()
                            comment_box = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
    
                            if (comm_prob == 1):
                                comment_box.send_keys('Really cool!')
                                sleep(1)
                           
                            
                            elif comm_prob == 4:
                                comment_box.send_keys('Great one!!')
                                sleep(1)
                            elif comm_prob == 5:
                                comment_box.send_keys('Awesome!!')
                                sleep(1)
                           
                            elif comm_prob == 7:
                                comment_box.send_keys('Nice !!')
                                sleep(1)
                            elif comm_prob == 8:
                                comment_box.send_keys('Superb!!')
                                sleep(1)
                            
                           
                            # Enter to post comment
                            comment_box.send_keys(Keys.ENTER)
                            sleep(3)   
                    # Next picture
                    driver.find_element_by_link_text('Next').click()
                    sleep(3)
                else:
                    driver.find_element_by_link_text('Next').click()
                    sleep(3)
            except:
                continue
    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except:
        continue

for n in range(0,len(new_followed)):
    prev_user_list.append(new_followed[n])
    
updated_user_df = pd.DataFrame(prev_user_list)
updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))