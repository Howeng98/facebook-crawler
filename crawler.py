import requests
import time
import argparse
import firebase_admin
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import datetime
from firebase_admin import credentials
from firebase_admin import db



def lineNotifyMessage(token, msg):
    # send msg through LINE-Notify
    headers = {
        "Authorization": "Bearer " + token        
    }

    payload = {
        "message": msg
    }

    r = requests.post('https://notify-api.line.me/api/notify', headers=headers, params=payload)
    # print(r.status_code)

def main():
    # Getting and setup arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--account' , required=True, type=str, help='facebook account')
    parser.add_argument('-p', '--password' , required=True, type=str, help='facebook password')
    args = parser.parse_args()
    
    # Line-Notify Token
    token = ''

    # Chrome driver options    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {\
        "profile.default_content_setting_values.notifications":1
        })    
    chrome_options.add_argument("--disable-infobars")    
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("start-maximized")    
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage') # for interface progressing

    # Setup Firebase credentials certificate and header
    cred = credentials.Certificate('serviceAccount.json') # get your own .json file 
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://facebook-crawler-2b822-default-rtdb.firebaseio.com/' # get your own databaseURL
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

    # Switch to '清交二手版' fb page (The page you want to crawl)
    url = 'https://www.facebook.com/groups/817620721658179'
    driver.get(url)
    time.sleep(1)

    # Global variables
    js = 'window.scrollTo(0, document.body.scrollHeight)'    
    postNumber = 3 # How many post you want get
    counter = 0
            
    # Get post content
    while counter < postNumber:
        # Expanse windows scroll page and release 'See More' content
        driver.execute_script(js)        
        links = driver.find_elements_by_xpath('//div[contains(text(),"See More")]')           
        for link in links:
            try:                
                link.click()
            except:
                pass
        
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'html.parser')        
        postList = soup.find_all('div', class_='ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a')
        counter = len(postList)        
    
    # Define your specific keyword in post that you looking for 
    keyword = [     
        '螢幕',
        '家教',
        '鏡頭',
        '顯卡',
        'GeForce',
        'BTS',
        'Airpod'
    ]
    
    # Extract and process post id to generate post URL link
    # for link in po_link:
    #     result = re.search('pcb.(.*?)&amp',str(link.a)).group(1).split('/')[0]
    #     print(result)
    #     print('\n')
    
    # Print post content
    for idx, post in enumerate(postList):           
        if not any([ignore_word in post.text for ignore_word in ["Unread", "posts", "See More"]]):                                          
            if any([ky in post.text for ky in keyword]):                
            
                dateTime = datetime.now()
                datestamp = dateTime.strftime("%d-%b-%Y")
                timestamp = dateTime.strftime("%H:%M:%S.%f")

                for ky in keyword:
                    if ky in post.text:
                        k = '' + ky

                ref = db.reference('/'+datestamp+'/'+k+'/')
                try:
                    count = len(ref.get())
                    # check post exist already or not                    
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
                    ref.set(post)
                                

    # Quit driver
    time.sleep(1)    
    driver.quit()
    print('\n======Driver Stop Execute======\n')

if __name__ == "__main__":
    main()





