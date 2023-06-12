import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


path = r'/home/olytvynov/Projects/HL/drivers/chromedriver_linux64_111.0.5563.64'
driver = Chrome(service=Service(path))
driver.maximize_window()
driver.implicitly_wait(5)

# Single selection

# driver.get('https://demo.guru99.com/test/newtours/register.php')
# countries_dropdown_element = driver.find_element(By.NAME, 'country')
# countries_dropdown = Select(countries_dropdown_element)
# #print(countries_dropdown.is_multiple)
# # for option in countries_dropdown.options:
# #     print(option.text)
# #countries_dropdown.select_by_visible_text("ANTARCTICA")
# #countries_dropdown.select_by_index(3)
# ##countries_dropdown.select_by_value()
# print(countries_dropdown.all_selected_options[0].text)


# Multiple selection

driver.get('https://output.jsbin.com/osebed/2')
fruits_element = driver.find_element(By.ID, 'fruits')
fruits = Select(fruits_element)
print(fruits.is_multiple)

for option in fruits.all_selected_options:
    print(option.text)
print()

fruits.select_by_value('banana')
fruits.select_by_value('apple')
fruits.select_by_value('grape')

for option in fruits.all_selected_options:
    print(option.text)

time.sleep(0.6)
fruits.deselect_by_value('apple')


time.sleep(2)
driver.quit()
