import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


path = r'/home/olytvynov/Projects/HL/drivers/chromedriver_linux64_111.0.5563.64'
driver = Chrome(service=Service(path))
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://demo.guru99.com/popup.php")



print(driver.current_window_handle)
print(driver.window_handles)
click_here = driver.find_element(By.LINK_TEXT, 'Click Here')
click_here.click()
print()
print(driver.current_window_handle)
print(driver.window_handles)

driver.switch_to.window(driver.window_handles[1])

submit_button = driver.find_element(By.XPATH, "//input[@name='btnLogin']")
print(submit_button.is_displayed())

time.sleep(0.6)
driver.close()

time.sleep(1)
driver.quit()
