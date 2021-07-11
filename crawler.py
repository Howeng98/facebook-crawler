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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--account' , required=True, type=str, help='facebook account')
    parser.add_argument('-p', '--password' , required=True, type=str, help='facebook password')
    args = parser.parse_args()
        
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {\
        "profile.default_content_setting_values.notifications":1
        })    
    chrome_options.add_argument("--disable-infobars")    
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage') # for interface progressing
    
    driver = webdriver.Chrome(ChromeDriverManager().install() ,chrome_options=chrome_options)
    print('Driver Start Execute')
    driver.get('https://www.facebook.com/')

    driver.find_element_by_css_selector("input[name='email']").send_keys(args.account)
    driver.find_element_by_css_selector("input[name='pass']").send_keys(args.password)
    driver.find_element_by_css_selector("button[name='login']").click()
    time.sleep(1)

    url = 'https://www.facebook.com/groups/817620721658179'
    driver.get('https://www.facebook.com/groups/817620721658179')    
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    js = 'window.scrollTo(0, document.body.scrollHeight)'

    postList = soup.find_all('span', class_='d2edcug0 hpfvmrgz qv66sw1b c1et5uql b0tq1wua a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb hrzyx87i jq4qci2q a3bd9o3v knj5qynh oo9gr5id hzawbc8m')
    seeMore = driver.find_elements_by_link_text('See More')
    [more.click() for more in seeMore]
    postList = soup.find_all('span', class_='d2edcug0 hpfvmrgz qv66sw1b c1et5uql b0tq1wua a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb hrzyx87i jq4qci2q a3bd9o3v knj5qynh oo9gr5id hzawbc8m')
    postN = len(postList)

    while postN < 50:
        driver.execute_script(js)        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        seeMore = driver.find_elements_by_link_text('See More')
        [more.click() for more in seeMore]
        postList = soup.find_all('span', class_='d2edcug0 hpfvmrgz qv66sw1b c1et5uql b0tq1wua a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb hrzyx87i jq4qci2q a3bd9o3v knj5qynh oo9gr5id hzawbc8m')
        seeMore_content = soup.find_all('div', class_='o9v6fnle cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q')
        postN = len(postList)
        seeMoreN = len(seeMore_content)
        print(postN)
        time.sleep(1)
    
    for post in postList:
        print('\n======================================================')
        print(post.text.strip('See More'))
        # try:
        #     seeMore_content = soup.find_all('div', class_='o9v6fnle cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q')
        #     [print(s_c.text+'\n') for s_c in seeMore_content]
        # except:
        #     continue
            


    driver.quit()
    print('Driver Stop Execute')    

if __name__ == "__main__":
    main()





