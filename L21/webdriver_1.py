from selenium.webdriver import Chrome, Keys
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# By.XPATH, '//ul[@role="listbox"]/li[1]' hint
# By.XPATH, "//div[@id='res']/descendant::a[1]"  - wiki link


driver_path = r'/home/olytvynov/Projects/HL/drivers/chromedriver_linux64_111.0.5563.64'


#driver = Chrome(executable_path=driver_path)  # deprecated
driver = Chrome(service=Service(driver_path))
#driver.implicitly_wait(time_to_wait=3)

wait = WebDriverWait(driver, timeout=3)

driver.maximize_window()

driver.get("https://www.google.com/")

query_field = driver.find_element(By.NAME, 'q')
query_field.send_keys("Croatia")
#time.sleep(1)
# query_field.clear()
# time.sleep(1)
# query_field.send_keys("Ukraine")

# for i in range(3):
#     query_field.send_keys(Keys.BACKSPACE)
#     time.sleep(0.6)

#time.sleep(3)
# wait.until(EC.visibility_of_element_located((By.XPATH, "//ul[@role='listbox']/li[1]")))
# hint = driver.find_element(By.XPATH, "//ul[@role='listbox']/li[1]")

hint = wait.until(EC.visibility_of_element_located((By.XPATH, "//ul[@role='listbox']/li[1]")))

hint.click()
time.sleep(1)

# headers = driver.find_elements(By.TAG_NAME, 'h3')
#
# for header in headers:
#     print(header.text)

# input_field = driver.find_element(By.TAG_NAME, 'textarea')
# print(input_field.get_attribute('value'))
# print(input_field.get_property('value'))
#
# map = driver.find_element(By.XPATH, "//img[@class='lu-fs']")
# print(map.get_attribute('title'))
# print(map.get_property('title'))

wiki_link = driver.find_element(By.XPATH, "//div[@id='res']/descendant::a[1]")
wiki_link.click()
time.sleep(0.5)

# bosnia_and_herzegovina = driver.find_element(By.LINK_TEXT, 'Bosnia and Herzegovina')
# bosnia_and_herzegovina.click()

cro_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Cro')
cro_link.click()


# driver.back()
# time.sleep(0.5)
# driver.refresh()
# time.sleep(0.5)
# driver.forward()

# print(driver.name)
# print(driver.title)
# print(driver.current_url)
# print(driver.page_source[:1000])

# flag = driver.find_element(By.XPATH, "//img[@alt='Flag of Croatia']")
# flag.screenshot('flag.png')
#
# driver.save_screenshot('wiki.png')
#
# screenshot_binary = driver.get_screenshot_as_png()
# with open('scr.png', 'wb') as f:
#     f.write(screenshot_binary)




time.sleep(1)
driver.quit()
