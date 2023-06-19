import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


path = r'/home/olytvynov/Projects/HL/drivers/chromedriver_linux64_111.0.5563.64'
driver = Chrome(service=Service(path))
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://www.saucedemo.com/')

# username = driver.find_element(By.ID, 'user-name')
# password = driver.find_element(By.ID, 'password')
# login_button = driver.find_element(By.ID, 'login-button')


print(driver.get_cookies())
print()
driver.add_cookie({'name': 'My cookie', 'value': 'QQQQQ'})

import datetime
new_date = int(datetime.datetime.now().timestamp() + 3600)
my_cookie = {'domain': 'www.saucedemo.com', 'expiry': new_date, 'httpOnly': False, 'name': 'session-username', 'path': '/', 'secure': False, 'value': 'standard_user'}
driver.add_cookie(my_cookie)




driver.get('https://www.saucedemo.com/inventory.html')


# username.send_keys('standard_user')
# password.send_keys('secret_sauce')
# login_button.click()

print(driver.get_cookies())

time.sleep(2)
driver.quit()