from selenium.webdriver.common.by import By
from time import sleep
class Login:
    def __init__(self, driver):
        self.driver = driver
        self.email_xpath = "//input[@id='field-1']"
        self.password_xpath="//input[@id='field-2']"
        self.Submit_Button_Xpath = " //button[@type='submit']"

    def enter_email(self, UserEmail):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(UserEmail)

    def enter_password(self,UserPassword):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(UserPassword)

    def Click_On_Login_Button(self):
        self.driver.find_element(By.XPATH, self.Submit_Button_Xpath).click()
        sleep(3)