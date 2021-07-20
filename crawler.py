import requests
import time
import re
import argparse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup, NavigableString, Tag
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token        
    }

    payload = {
        "message": msg
    }

    r = requests.post('https://notify-api.line.me/api/notify', headers=headers, params=payload)
    print(r.status_code)

def main():
    # Getting and setup arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--account' , required=True, type=str, help='facebook account')
    parser.add_argument('-p', '--password' , required=True, type=str, help='facebook password')
    args = parser.parse_args()
    
    token = 'pj4zAv0SHrx80RGRQ3gINSg6nfOBbzgLdgsReqQGxNN'

    # Chrome driver options    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {\
        "profile.default_content_setting_values.notifications":1
        })    
    chrome_options.add_argument("--disable-infobars")    
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("start-maximized")    
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage') # for interface progressing

    cred = credentials.Certificate('serviceAccount.json')

    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://facebook-crawler-2b822-default-rtdb.firebaseio.com/'
    })

    
    # Prepare driver
    driver = webdriver.Chrome(ChromeDriverManager().install() ,chrome_options=chrome_options)    
    print('\n======Driver Start Execute======\n')
    driver.get('https://www.facebook.com/')

    # Input Facebook Username and Password
    driver.find_element_by_css_selector("input[name='email']").send_keys(args.account)
    driver.find_element_by_css_selector("input[name='pass']").send_keys(args.password)
    driver.find_element_by_css_selector("button[name='login']").click()
    time.sleep(1)

    # Switch to '清交二手版' fb page
    url = 'https://www.facebook.com/groups/817620721658179'
    driver.get(url)
    time.sleep(1)

    # Global variables
    js = 'window.scrollTo(0, document.body.scrollHeight)'    
    postNumber = 20
    counter = 0
            
    # Get post content
    while counter < postNumber:
        # Expanse windows scroll page and release 'See More' content
        driver.execute_script(js)
        # time.sleep(3)
        links = driver.find_elements_by_xpath('//div[contains(text(),"See More")]')           
        for link in links:
            try:                
                link.click()
            except:
                pass
        
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'html.parser')        
        postList = soup.find_all('div', class_='ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a')
        
        po_link = soup.find_all('div', class_='ni8dbmo4 stjgntxs pmk7jnqg')

        counter = len(postList)
        # print(counter)
        # time.sleep(1)
    
    keyword = [     
        '螢幕',
        '家教',
        '鏡頭',
        '顯卡',
        'GeForce',
        'BTS',
        'Airpod'
    ]
    # print('PostList')
    # print(len(postList))
    # print('PostLink')
    # print(len(po_link))

    # for link in po_link:
    #     result = re.search('pcb.(.*?)&amp',str(link.a)).group(1).split('/')[0]
    #     print(result)
    #     print('\n')
    
    # Print post content
    for idx, post in enumerate(postList):
        # print('\n=======================')        
        if not any([ignore_word in post.text for ignore_word in ["Unread", "posts", "See More"]]):            
            # print(post.text)                        
            if any([ky in post.text for ky in keyword]):
                # time.sleep(1)

                
                dateTime = datetime.now()
                datestamp = dateTime.strftime("%d-%b-%Y")
                timestamp = dateTime.strftime("%H:%M:%S.%f")
                # print(timestamp)
                # print(post.text)
                for ky in keyword:
                    if ky in post.text:
                        k = '' + ky

                ref = db.reference('/'+datestamp+'/'+k+'/')
                try:
                    count = len(ref.get())
                    # check post exist already or not
                    # print('here')
                    for exist_post_idx in range(count):
                        IS_EXIST = False
                        exist_post_data = db.reference('/'+datestamp+'/'+k+'/'+str(exist_post_idx)+'/').get()
                        if post.text in exist_post_data['content']:
                            # if it is exist, break for loop, and do nothing
                            IS_EXIST = True
                            break

                    if IS_EXIST is False:                        
                        ref = db.reference('/'+datestamp+'/'+k+'/'+str(count)+'/')
                        post = {                                   
                            'timestamp': timestamp,            
                            'content': post.text
                        }                    
                        ref.set(post)
                        # new post, send notification
                        lineNotifyMessage(token, post.text)

                except Exception as e:
                    print(e)
                    count = str(0)
                    ref = db.reference('/'+datestamp+'/'+k+'/'+str(count)+'/')
                    post = {                                   
                        'timestamp': timestamp,            
                        'content': post.text
                    }
                    # print('first post')
                    ref.set(post)
                                

    # Quit driver
    time.sleep(1)    
    driver.quit()
    print('\n======Driver Stop Execute======\n')

if __name__ == "__main__":
    main()





