#Test case 1 => Success login using username and password
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Data import data
from Locators import locators

class Project:
    def __init__(self):
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def Login(self):
        try:
            self.driver.maximize_window()
            self.driver.get(data.WebApp_Data().url)
            self.driver.implicitly_wait(20)
            #Input username, password and logging in.
            self.driver.find_element(by=By.NAME, value=locators.WebApp_Locators().username_input_box).send_keys(data.WebApp_Data().username)
            self.driver.find_element(by=By.NAME, value=locators.WebApp_Locators().password_input_box).send_keys(data.WebApp_Data().password)
            self.driver.find_element(by=By.XPATH, value=locators.WebApp_Locators().submit_button).click()
            #Checking whether the dashboard url and current url after successful login
            self.driver.implicitly_wait(10)
            if data.WebApp_Data.dashboard_url in self.driver.current_url:
                print("The user is logged in successfully.")
            else:#Displaying the text appeared when login was unsuccesful
                invalid_message = self.driver.find_element(by=By.XPATH, value=locators.WebApp_Locators().invalid_message)
                print(invalid_message.text)
                print("Login Unsuccessful")
        #Exception handling
        except NoSuchElementException as selenium_error:
            print(selenium_error)
        #Closing browser        
        finally:
            self.driver.close()

Obj=Project()

Obj.Login()