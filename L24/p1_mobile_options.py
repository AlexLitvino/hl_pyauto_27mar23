import time

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome


# https://chromedriver.chromium.org/mobile-emulation
# https://chromedriver.chromium.org/capabilities
path = r'/home/olytvynov/Projects/HL/drivers/chromedriver_linux64_111.0.5563.64'

options = ChromeOptions()
mobile_emulation = {"deviceName": "Nexus 5"}
options.add_experimental_option("mobileEmulation", mobile_emulation)
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-gpu")
# options.add_argument("--headless")
# options.add_argument("--headless")
driver = Chrome(service=Service(path), options=options)

driver.maximize_window()
wait = WebDriverWait(driver, timeout=3)

driver.get('https://google.com')

input_query = driver.find_element(By.NAME, 'q')
input_query.send_keys('Croatia')


first_hint = wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@role="listbox"]/li[1]')))
first_hint.click()
wiki_link = driver.find_element(By.XPATH, "(//a[@role='presentation'])[1]")  # locator differ from web version
wiki_link.click()

time.sleep(1)
driver.quit()
