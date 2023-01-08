from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class SignupBot:

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get("")
        self.driver.maximize_window()

    def loginPage(self):
        login_link = self.driver.find_element_by_link_text("Login / Register")
        login_link.click()

    def enterDetails(self):
        username = ""
        password = ""
        email_name = "email"
        password_name = "password"

        email_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_name(email_name))
        email_input.clear()
        email_input.send_keys(username)
        email_input.submit()

        password_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_name(password_name))
        password_input.clear()
        password_input.send_keys(password)
        password_input.submit()
    
    def selectSession(self, day, time):
        day_column_dictionary = {
            "Mon": "2",
            "Tue": "3",
            "Wed": "4",
            "Thu": "5",
            "Sat": "6"
        }
        time_row_dictionary = {
            "8am": "6",
            "9am": "8"
        }
        class_day_index = day_column_dictionary[day]
        class_time_index = time_row_dictionary[time]

        session_clickable = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[7]/div[4]/div[1]/table/tbody/tr["+ class_time_index +"]/td["+ class_day_index +"]/a"))
        session_clickable.click()

    def bookButton(self):
        book_button = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[3]/div/div[1]/center/div[1]/div[1]/form/button"))
        book_button.click()


    def tearDown(self):
        self.driver.quit()

    def main(self):
        day = "Mon"
        time = "8am"

        self.setUp()
        self.loginPage()
        self.enterDetails()
        self.selectSession(day, time)
        self.bookButton()

        self.tearDown()
        

if __name__ == "__main__":
    bot = SignupBot()
    bot.main()
