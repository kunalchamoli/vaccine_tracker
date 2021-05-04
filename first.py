import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"))


driver.get('https://www.cowin.gov.in/home')
time.sleep(2)

input = driver.find_element_by_css_selector('input#mat-input-0')
input.send_keys('302017')
input.send_keys(Keys.ENTER)

time.sleep(1)
age_restrict = driver.find_elements_by_css_selector(
    'div:nth-child(3) > label')[0]
age_restrict.click()

# hospitals = driver.find_element_by_id("slot-available-wrap")
# hospitals = driver.find_element_by_css_selector(
#     'div:nth-child(1) > div > div > div.slot-available-main.col-padding.col.col-lg-9.col-md-9.col-sm-9.col-xs-12 > ul > li:nth-child(1)')

# total_div = driver.find_elements_by_xpath(
#     '//div[@class="mat-main-field center-main-field"]')

total_div = driver.find_elements_by_xpath(
    '/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[6]/div/div/div/div')

for item in total_div:
    div1 = driver.find_elements_by_xpath('.//div[@class = "row"]')
    div2 = driver.find_elements_by_xpath(
        './/div[@class = "col-sm-12 col-md-12 col-lg-12"]')
    div3 = driver.find_elements_by_xpath(
        './/div[@class = "main-slider-wrap col col-lg-3 col-md-3 col-sm-3 col-xs-12"]')[0]

    print(div3.text)

    div4 = driver.find_elements_by_xpath(
        './/div[@class = "main-slider-wrap col col-lg-3 col-md-3 col-sm-3 col-xs-12"]')[1]
    slots = driver.find_elements_by_xpath(
        './/ul[@class = "slot-available-wrap"]//li')

    for item in slots:
        print('\n')
        print(item.text)

    # for i in range(len(slots)):
    #     try:
    #         val = driver.find_elements_by_xpath(
    #             './/div[@class = "slots-box ng-star-inserted"]')
    #         a = 1
    #     except Exception:
    #         try:
    #             val = driver.find_elements_by_xpath(
    #                 './/div[@class = "slots-box no-available ng-star-inserted"]')
    #             b = 1
    #         except Exception:
    #             try:
    #                 val = driver.find_elements_by_xpath(
    #                     './/div[@class = "slots-box no-seat ng-star-inserted"]')
    #                 c = 1
    #             except Exception:
    #                 pass
