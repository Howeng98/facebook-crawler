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

def main():
    # Getting and setup arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--account' , required=True, type=str, help='facebook account')
    parser.add_argument('-p', '--password' , required=True, type=str, help='facebook password')
    args = parser.parse_args()

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
    driver.get('https://www.facebook.com/groups/817620721658179')    
    time.sleep(1)

    # Global variables
    js = 'window.scrollTo(0, document.body.scrollHeight)'    
    postNumber = 5
    counter = 0
    
    
    

    # Get post content
    while counter < postNumber:
        # Expanse windows scroll page and release 'See More' content
        driver.execute_script(js)
        time.sleep(1)
        links = driver.find_elements_by_xpath('//div[contains(text(),"See More")]')                    
        for link in links:
            try:                
                link.click()
            except:
                print('not work')        
        print('Expanse post done')

        soup = BeautifulSoup(driver.page_source, 'html.parser')        
        postList = soup.find_all('div', class_='ecm0bbzt hv4rvrfc e5nlhep0 dati1w0a')
        counter = len(postList)
        time.sleep(1)
        # //*[@id="jsc_c_2p"]
        # //*[@id="jsc_c_3b"]
    
    # Print post content
    for post in postList:
        print('\n=======================')
        if "Unread" not in post.text:
            print(post.text)        

    # Quit driver
    time.sleep(30)    
    driver.quit()
    print('\n======Driver Stop Execute======\n')

if __name__ == "__main__":
    main()





