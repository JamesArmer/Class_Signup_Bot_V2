import datetime
import logging

import azure.functions as func
from azure.identity import DefaultAzureCredential, ClientSecretCredential
from azure.storage.blob import BlobServiceClient
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    day_int = datetime.datetime.today().weekday()
    day = ""
    time = ""

    if(day_int == 0):
        day = "Fri"
        time = "8am"
    if(day_int == 1):
        day = "Sat"
        time = "9am"
    if(day_int == 3):
        day = "Mon"
        time = "8am"
    if(day_int == 4):
        day = "Tue"
        time = "8am"
    if(day_int == 5):
        day = "Wed"
        time = "8am"

    if(day == "") or (time == ""):
        logging.info("No class to book today.")
        return func.HttpResponse(
             status_code=200
        )

    day_column_dictionary = {
        "Mon": "1",
        "Tue": "2",
        "Wed": "3",
        "Thu": "4",
        "Fri": "5",
        "Sat": "6"
    }
    time_row_dictionary = {
        "8am": "6",
        "9am": "8"
    }

    username = ""
    password = ""
    email_name = "email"
    password_name = "password"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('window-size=1920,1080')

    driver = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=chrome_options)
    driver.get("https://goteamup.com/p/904391-dawn-strength-conditionin/")

    logging.info('Loaded Website.')

    login_link = driver.find_element_by_xpath("/html/body/div[1]/div[1]/nav/div/div[1]/div[2]/ul/li[4]/a")
    login_link.click()

    logging.info('At login page.')

    email_input = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name(email_name))
    email_input.clear()
    email_input.send_keys(username)
    email_input.submit()

    password_input = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name(password_name))
    password_input.clear()
    password_input.send_keys(password)
    password_input.submit()

    logging.info('Logged in successfully.')

    if(day != "Fri") and (day != "Sat"):
        next_page = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[3]/table/tbody/tr[1]/td/div[2]/a"))
        next_page.click()

    logging.info('On next page.')
    
    class_day_index = day_column_dictionary[day]
    class_time_index = time_row_dictionary[time]

    session_clickable = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[7]/div[4]/div[1]/table/tbody/tr["+ class_time_index +"]/td["+ class_day_index +"]/a"))
    session_clickable.click()

    logging.info('On class page.')

    book_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[3]/div/div[1]/center/div[1]/div[1]/form/button"))
    book_button.click()

    logging.info('Class booked!')

    return func.HttpResponse(
             status_code=200
    )