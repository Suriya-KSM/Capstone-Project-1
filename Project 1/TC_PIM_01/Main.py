#Test Case => Adding new employee in PIM module
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from Data import data
from Locators import locators

class Project:
    def __init__(self):
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(data.WebApp_Data().url)

    def Login(self):
        try:
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
    #Going to PIM module
    def PIM_module(self):
        try:
            #Switching to PIM module using explicit wait
            wait = WebDriverWait(self.driver, 20)
            PIM = wait.until(EC.element_to_be_clickable((By.XPATH, locators.WebApp_Locators().PIM_module)))
            PIM.click()
            #Switching to Add employee using explicit wait
            AddEmployee = wait.until(EC.element_to_be_clickable((By.XPATH, locators.WebApp_Locators().add_employee)))
            AddEmployee.click()
            sleep(5)
            #Entering the details in the provided place and saving
            self.driver.find_element(by=By.NAME, value=locators.WebApp_Locators().first_name).send_keys(data.WebApp_Data().first_name)
            self.driver.find_element(by=By.NAME, value=locators.WebApp_Locators().middle_name).send_keys(data.WebApp_Data().middle_name)
            self.driver.find_element(by=By.NAME, value=locators.WebApp_Locators().last_name).send_keys(data.WebApp_Data().last_name)
            self.driver.find_element(by=By.XPATH, value=locators.WebApp_Locators().save_button).click()
            print("Successful Employee addition ")
        #exception handling     
        except NoSuchElementException as selenium_error:
            print(selenium_error) 
        except TimeoutException as e:
            print("Time Out error",e)
        #and finally executing the success operation closing the browser
        finally:
            sleep(2)
            self.driver.close()

Obj=Project()

Obj.Login()
Obj.PIM_module()