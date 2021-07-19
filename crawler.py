import requests
import time
import argparse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime



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
    # chrome_options.add_argument('--disable-dev-shm-usage') # for interface progressing
    
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
    postNumber = 10
    counter = 0
            
    # Get post content
    while counter < postNumber:
        # Expanse windows scroll page and release 'See More' content
        driver.execute_script(js)
        time.sleep(3)
        links = driver.find_elements_by_xpath('//div[contains(text(),"See More")]')           
        for link in links:
            try:                
                link.click()
            except:
                pass
        
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'html.parser')        
        postList = soup.find_all('div', class_='ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a')

        # postTime = soup.find_all('a', class_='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw')

        postLink = soup.find_all('div', class_='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0')
        counter = len(postList)
        print(counter)
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

    # Print post content
    for idx, post in enumerate(postList):
        print('\n=======================')        
        if not any([ignore_word in post.text for ignore_word in ["Unread", "posts", "See More"]]):
            # print(post.text)            
            soup.findall()
            # if any([ky in post.text for ky in keyword]):
            #     time.sleep(1)

            #     lineNotifyMessage(token, post.text)
            #     dateTime = datetime.now()
            #     timestamp = dateTime.strftime("%d-%b-%Y | %H:%M:%S.%f")
            #     print(timestamp)
            #     print(post.text)

            

    # Quit driver
    time.sleep(1)    
    driver.quit()
    print('\n======Driver Stop Execute======\n')

if __name__ == "__main__":
    main()





