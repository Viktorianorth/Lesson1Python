from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException

service = Service(executable_path=r'C:\Users\vikto\Downloads\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

try:

    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-primary')]"))
    )
    button.click()
    print("Кнопка успешно нажата.")
except TimeoutException:
    print("Время ожидания истекло: кнопка не была найдена или не стала доступной для клика.")
except NoSuchElementException:
    print("Элемент не найден: кнопка с заданным XPATH отсутствует на странице.")
except ElementClickInterceptedException:
    print("Не удалось кликнуть по элементу: кнопка перекрыта другим элементом.")
except Exception as e:
    print(f"Произошла ошибка: {e}")