from Login import Login
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

driver_service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=driver_service)
driver.get("https://ocean.sotoon.ir/account/login")
driver.implicitly_wait(4)

login=Login(driver=driver)

login.enter_email('sotoonqainterview3@gmail.com')
login.enter_password('ponjhjw3%')
login.Click_On_Login_Button()
driver.implicitly_wait(3)




