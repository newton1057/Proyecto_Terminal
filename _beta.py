import requests
import sys
import json
from bs4 import BeautifulSoup

#from seleniumrequests import Chrome

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def Connect_Mathscinet():
    with open('config.json') as config_file:
        data = json.load(config_file)

    Mathscinet = data['Mathscinet']

    driver.get('https://mathscinet.uam.elogim.com/mathscinet/')
    driver.maximize_window()
    driver.find_element(By.NAME, "httpd_username").send_keys(Mathscinet['username'])
    driver.find_element(By.NAME, "httpd_password").send_keys(Mathscinet['password'])
    driver.find_element(By.NAME, "login-form-submit").click()

def get_Author(AuthorID):
    driver.get('https://mathscinet.uam.elogim.com/mathscinet/author?authorId='+AuthorID)
    print(driver.find_element(By.XPATH, "//*[@id='main-content']/div/div/div[1]/div[1]/span").text)
    
    
def main():
    Connect_Mathscinet()
    get_Author(str(199913))
    input()

if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')
    driver = webdriver.Chrome(options=chrome_options) 
    main()