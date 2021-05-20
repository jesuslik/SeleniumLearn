from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)


    firstName = browser.find_element_by_name("firstname")
    firstName.send_keys("Artemy")

    lastName = browser.find_element_by_name("lastname")
    lastName.send_keys("Vetts")

    eMail = browser.find_element_by_name("email")
    eMail.send_keys("artemy@email.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
    elementUpload = browser.find_element_by_id("file")
    elementUpload.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
