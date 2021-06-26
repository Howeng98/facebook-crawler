import requests
import pandas as pd
import os
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import argparse



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--account' , required=True, type=str, help='facebook account')
    parser.add_argument('-p', '--password' , required=True, type=str, help='facebook password')
    args = parser.parse_args()
        
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage') # for interface progressing
    
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
    driver.get('https://www.facebook.com/')

    driver.find_element_by_css_selector('#email').send_keys(args.account)
    driver.find_element_by_css_selector("input[type='password']").send_keys(args.password)
    driver.find_element_by_css_selector("button[name='login']").click()
    time.sleep(1)

    cookies = driver.get_cookies()
    driver.close()
    print('Check check')


if __name__ == "__main__":
    main()





