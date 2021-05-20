import math
import time

from selenium import webdriver

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    sum = int(x) + int(y)

    resultSelect = "[value='" + str(sum) + "']"

    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector(resultSelect).click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
