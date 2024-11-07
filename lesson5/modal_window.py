from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
options = Options()
options.binary_location = firefox_binary_path

service = Service(executable_path=r'C:\Geckodriver\geckodriver.exe')
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")

try:
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='modal-footer']/p"))
    )

    close_button.click()
    print("Модальное окно закрыто.")

except TimeoutException:
    print("Время ожидания истекло: кнопка 'Close' не была найдена.")
except NoSuchElementException:
    print("Элемент не найден: модальное окно или кнопка отсутствует на странице.")
except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:

    driver.quit()