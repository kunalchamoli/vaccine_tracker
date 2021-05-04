import os
import time
from collections import defaultdict
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path=os.path.abspath(
    "chromedriver.exe"), options=options)


driver.get('https://www.cowin.gov.in/home')
time.sleep(2)

input = driver.find_element_by_css_selector('input#mat-input-0')
input.send_keys('302017')
input.send_keys(Keys.ENTER)

time.sleep(1)
age_restrict = driver.find_elements_by_css_selector(
    'div:nth-child(3) > label')[0]
age_restrict.click()


total_div = driver.find_elements_by_xpath(
    '/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[6]/div/div/div/div')


for item in total_div:
    print('\n')
    div1 = item.find_elements_by_xpath('./div/div/div')

    hospital = div1[0].text
    print(hospital)

    slots = div1[1].find_elements_by_xpath('./ul/li')

    for elem in slots:
        print('\n')
        print(elem.text)
