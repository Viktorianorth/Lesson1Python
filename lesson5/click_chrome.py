from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

button = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')
for _ in range(5):
    button.click()
count_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

print(f'число кнопок:{len(count_buttons)}')

driver.quit()