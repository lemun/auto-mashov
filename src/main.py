from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.expected_conditions import presence_of_element_located

import time, json, colorama, random, sys

from .webhook import Webhook
from .img import Remove
from .color import *
from .intro import intro

class Main:

    def app():
        # config
        # DO NOT EDIT
        config_path = (r"./config/main.json")
        with open(config_path) as data:
            config = json.load(data)
        mashov_user = config["user"]
        mashov_pass = config["pass"]
        mashov_school = config["school"]
        #config
        # DO NOT EDIT

        # intro
        sys.stdout.write(intro())
        print('    Github Profile - https://github.com/lemun \n\n\n')

        ### start of program ###

        options = webdriver.ChromeOptions()

        # headless options:
        # 1: SHOW BROWSER 
        # 2: HIDE BROWSER
        headless_option = 1 # set here

        if headless_option == 2:
            print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'headless_option: ' + fy + '2' + ' - ' + fg + 'Enabled')
            options.add_argument("--headless")
            options.add_argument("--log-level=3")
            driver = webdriver.Chrome('./driver/chromedriver', chrome_options=options)

        elif headless_option == 1:
            print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'headless_option: ' + fy + '1' + ' - ' + fm + 'Disabled')
            options.add_argument("--log-level=3")
            driver = webdriver.Chrome('./driver/chromedriver', chrome_options=options)

        elif headless_option != 1:
            print(fc + sd + '[' + fr + '*' + fc + '] ' + fg + 'headless_option: ' + fr + 'ERROR!' + fy + ' - ' + fr + 'RUNNING WITH BROWSER SHOWING!!!')
            options.add_argument("--log-level=3")
            driver = webdriver.Chrome('./driver/chromedriver', chrome_options=options)

        elif headless_option != 2:
            print(fc + sd + '[' + fr + '*' + fc + '] ' + fg + 'headless_option: ' + fr + 'ERROR!' + fy + ' - ' + fr + 'RUNNING WITH BROWSER SHOWING!!!')
            options.add_argument("--log-level=3")
            driver = webdriver.Chrome('./driver/chromedriver', chrome_options=options)

        wait = WebDriverWait(driver, 30)
        

        print('\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Hold on Starting now, Check this terminal for progress')

        # open mashov
        driver.get("https://web.mashov.info/students/login")



        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + 'Progress - 1/7', end='')

        # wait until the login page loads and open the school box
        wait.until(presence_of_element_located((By.ID, "mat-input-3")))
        time.sleep(random.uniform(1, 3))
        driver.find_element(By.ID, "mat-input-3").click()

        # typing school ID
        driver.find_element(By.ID, "mat-input-3").send_keys(mashov_school)

        # wait for the login page to show your school and click it
        driver.find_element(By.CSS_SELECTOR, ".mat-option-text").click()
        print(fg + ' (Success)')


        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + 'Progress - 2/7', end='')

        # find and click the username box
        driver.find_element(By.ID, "mat-input-0").click()

        # enter username
        driver.find_element(By.ID, "mat-input-0").send_keys(mashov_user)
        print(fg + ' (Success)')


        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + 'Progress - 3/7', end='')

        # click the password
        wait.until(presence_of_element_located((By.CSS_SELECTOR, ".mat-button-wrapper > .ng-star-inserted")))
        element = driver.find_element(By.CSS_SELECTOR, ".mat-button-wrapper > .ng-star-inserted")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()


        # enter password
        wait.until(presence_of_element_located((By.ID, "mat-input-4")))
        driver.find_element(By.ID, "mat-input-4").send_keys(mashov_pass)

        # login to account
        wait.until(presence_of_element_located((By.CSS_SELECTOR, ".mat-button-wrapper > .ng-star-inserted")))
        driver.find_element(By.CSS_SELECTOR, ".mat-button-wrapper > .ng-star-inserted").click()
        print(fg + ' (Success)')


        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + 'Progress - 4/7', end='')

        # go to daily statement page
        time.sleep(random.uniform(1, 2)) 
        driver.get("https://web.mashov.info/students/main/covidClearance")

        # accept daily statement
        wait.until(presence_of_element_located((By.CSS_SELECTOR, ".mat-primary > .mat-button-wrapper")))
        driver.find_element(By.CSS_SELECTOR, ".mat-primary > .mat-button-wrapper").click()
        time.sleep(random.uniform(1, 2)) 
        print(fg + ' (Success)')
        

        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + 'Progress - 5/7', end='')
        # take screenshot
        driver.save_screenshot('./img/proof.png')
        print(fg + ' (Success)')


        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + 'Progress - 6/7', end='')
        # send webhook
        Webhook.app()
        print(fg + ' (Success)')


        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + 'Progress - 7/7', end='')
        # remove proof.png
        Remove.img()
        print(fg + ' (Success)')


        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Script finished with: ' + fw + '0' + fr + ' errors')
