import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_css_selector("span#input_value")
    x = x_element.text
    y = calc(x)
    inputField = browser.find_element_by_id("answer")
    inputField.send_keys(y)
    inputCheck = browser.find_element_by_css_selector("[for='robotCheckbox']")
    inputCheck.click()
    inputRadio = browser.find_element_by_css_selector("[for='robotsRule']")
    inputRadio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
