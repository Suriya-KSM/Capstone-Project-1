#Test Case => Deleting the existing employee
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
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

    #Going to PIM module
    def PIM_module(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            action = ActionChains(self.driver)
            #Switching to PIM module using explicit wait
            PIM = wait.until(EC.element_to_be_clickable((By.XPATH, locators.WebApp_Locators().PIM_module)))
            PIM.click()
            #Searching existing employee by entering name and id in the respective input
            sleep(2)
            self.driver.find_element(by=By.XPATH, value=locators.WebApp_Locators().name_input).send_keys(data.WebApp_Data().emp_name)
            self.driver.find_element(by=By.XPATH, value=locators.WebApp_Locators().id_input).send_keys(data.WebApp_Data().emp_id)
            sleep(2)
            self.driver.find_element(by=By.XPATH,value=locators.WebApp_Locators().search_button).click()
            #Scrolling down the scroll bar to make visible of the employee
            sleep(2)
            action.key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).perform()
            #Selecting and clicking the delete icon
            self.driver.find_element(by=By.XPATH, value=locators.WebApp_Locators().select_emp).click()
            self.driver.find_element(by=By.XPATH, value=locators.WebApp_Locators().delete_icon).click()
            #Confirming to delete
            self.driver.find_element(by=By.XPATH, value=locators.WebApp_Locators().confirm_button).click()
            print("Deletion Successful")
        #exception handling     
        except NoSuchElementException as selenium_error:
            print(selenium_error) 
        except TimeoutException as e:
            print("Time Out error", e)
        #Closing the browser
        finally:
            self.driver.close()



Obj=Project()

Obj.Login()
Obj.PIM_module()