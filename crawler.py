import requests
import pandas
import os
import sys
import re
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup, element
import time
import argparse
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


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
    postNumber = 5
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
        postList = soup.find_all('span', class_='d2edcug0 hpfvmrgz qv66sw1b c1et5uql b0tq1wua a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb hrzyx87i jq4qci2q a3bd9o3v knj5qynh oo9gr5id hzawbc8m')
        counter = len(postList)
        print(counter)
        # time.sleep(1)
    
    
    # Print post content
    for post in postList:
        print('\n=======================')        
        if not any([ignore_word in post.text for ignore_word in ["Unread", "posts", "See More"]]):        
            print(post.text)
            time.sleep(1)
            lineNotifyMessage(token, post.text)

    # Quit driver
    time.sleep(1)    
    driver.quit()
    print('\n======Driver Stop Execute======\n')

if __name__ == "__main__":
    main()





