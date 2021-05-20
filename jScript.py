from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

element_x = browser.find_element_by_id("input_value")
result = calc(element_x.text)

answerField = browser.find_element_by_id("answer")
answerField.send_keys(result)

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

checkRobot = browser.find_element_by_id("robotCheckbox")
checkRobot.click()

radioRobot = browser.find_element_by_id("robotsRule")
radioRobot.click()

button.click()

