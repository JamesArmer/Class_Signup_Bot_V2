from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from datetime import date
from datetime import timedelta
import time

import logging

class SignupBot:

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get("https://app.wodify.com/SignIn/Login")
        self.driver.maximize_window()
        logging.info('Webdriver setup')

    def loginPage(self):
        username = ""
        password = ""
        email_name = "Input_UserName"
        password_name = "Input_Password"

        email_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(email_name))
        email_input.clear()
        email_input.send_keys(username)
        logging.info('Entered username')

        password_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(password_name))
        password_input.clear()
        password_input.send_keys(password)
        logging.info('Entered password')

        signin_button = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div[1]/div/div/form/div[2]/div[5]/button"))
        signin_button.click()
        logging.info('Clicked sign in button')
    
    def gotoCalendarPage(self):
        calendarLink = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div[2]/a"))
        calendarLink.click()
        logging.info('Clicked calendar page link')

    def selectDate(self, date_string):        
        date_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("/html/body/form/div[6]/div[2]/div[2]/div/span/div[2]/table/tbody/tr/td/input[2]"))
        date_input.clear()
        date_input.send_keys(date_string)
        logging.info("Date '{date_string}' entered")

        # wait 10 seconds for page to load
        logging.info('Beginning sleep')
        time.sleep(10)
        logging.info('Ending sleep')

    def bookButton(self, day_of_week):
        if(0 <= day_of_week <= 4):
            book_button = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("/html/body/form/div[6]/div[2]/div[2]/div/span/table/tbody/tr[4]/td[3]/div/a"))
            book_button.click()
            logging.info('Class booked!')

    def tearDown(self):
        self.driver.quit()

    def main(self):
        class_date = date.today() + timedelta(days=3)
        date_string = class_date.strftime("%d/%m/%Y")

        # Mon=0, Sun=6
        day_of_week = class_date.weekday()

        self.setUp()
        self.loginPage()
        self.gotoCalendarPage()

        self.selectDate(date_string)

        self.bookButton(day_of_week)

        self.tearDown()
        

if __name__ == "__main__":
    bot = SignupBot()
    bot.main()
