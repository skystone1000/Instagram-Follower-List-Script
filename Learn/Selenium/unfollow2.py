from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint

from selenium.webdriver.chrome.options import Options
#import pandas as pd

chromedriver_path = '/mnt/E4687B61687B3182/CSE/Insta script chromedriver_linux64/Unfollow/chromedriver' # Change this to your own chromedriver path!

driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(1)

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
driver = webdriver.Chrome(chromedriver_path, options = chrome_options)


print('here1')

driver.get('https://www.instagram.com/_still.hungry_/')
totalFollowers = 0
followersList = ['Follower Names']
totalFollowers = int(driver.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[2]/a/span').text)
print(totalFollowers)

followers = driver.find_element_by_partial_link_text('followers')
followers.click()
# followerBtnPath = driver.find_element_by_class_name('glyphsSpriteUser__outline__24__grey_9 u-__7')
# followerBtnPath.click()
sleep(3)
driver.execute_script("window.scrollTo(0, Y)")

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

"""
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
"""

for i in range(totalFollowers):
    if(i%5 == 0):
        sleep(3)
    string = str('/html/body/div[3]/div/div[2]/ul/div/li[{}]/div/div[2]/div[1]/div/div/a'.format(i+1))
    username = driver.find_element_by_xpath(string).text
    #followersList.append[username]
    print(username)



"""

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
"""