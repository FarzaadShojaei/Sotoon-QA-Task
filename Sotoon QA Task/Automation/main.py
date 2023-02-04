from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from Login import Login

# driver=webdriver.chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver_service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=driver_service)
login=Login(driver=driver)
driver.get("https://ocean.sotoon.ir/account/login")
login.enter_email('sotoonqainterview3@gmail.com')
login.enter_password('ponjhjw3%')
login.Click_On_Login_Button()
# Browser Action 1 > Open Web

driver.get("https://ocean.sotoon.ir/dashboard")
MainObject_element=driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/main[1]/div[2]/div[1]/div[1]/a[4]/div[1]")
MainObject_element.click()
#driver.forward()

driver.get("https://ocean.sotoon.ir/storages/storage/neda/buckets")



# Browser Action  1 > Title
#window_title = driver.title
#print(window_title)

# Browser Action 1 > Tabs

Current_element = driver.find_element(By.XPATH,"//body/div[@id='app']/div[1]/main[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]")
Current_element.click()
driver.back()


EndpointButton_element = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/main[1]/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]")
EndpointButton_element.click()

ObjectStorage_button = driver.find_element(By.CLASS_NAME, "nav__title")
ObjectStorage_button.click()

Sent_element = driver.find_element("class", "text-subtitle")
Sent_element.click()

AccessKeys_element=driver.find_element(By.CLASS_NAME,"nav__title")
driver.forward()
driver.get("https://ocean.sotoon.ir/storages/storage/neda/access/keys")
roleManagement=driver.find_element(By.CLASS_NAME,"nav__icon")
roleManagement.click()
driver.forward()
driver.get("https://ocean.sotoon.ir/storages/storage/neda/roles-management/users")
Monitoring_element = driver.find_element(By.XPATH,"//body/div[@id='app']/div[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/a[4]")
Monitoring_element.click()
driver.forward()
driver.get("https://ocean.sotoon.ir/storages/storage/neda/monitoring")
driver.find_element(By.CSS_SELECTOR,"input[placeholder='انتخاب کنید']").click()



