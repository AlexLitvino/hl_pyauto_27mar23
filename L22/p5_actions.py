import time

from selenium.webdriver import Chrome, Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = r'/home/olytvynov/Projects/HL/drivers/chromedriver_linux64_111.0.5563.64'
driver = Chrome(service=Service(path))
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://en.wikipedia.org/wiki/Croatia")
action = ActionChains(driver)
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
# action.reset_actions()
# action.perform()

# source = driver.find_element()
# target = driver.find_element()
# action.drag_and_drop(source, target).perform()


time.sleep(1)
driver.quit()