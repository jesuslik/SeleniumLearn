from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    bookButton = browser.find_element_by_id("book")
    bookButton.click()


    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_css_selector("span#input_value")
    x = x_element.text
    y = calc(x)
    inputField = browser.find_element_by_id("answer")
    inputField.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

