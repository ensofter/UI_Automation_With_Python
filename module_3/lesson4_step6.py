from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options)
browser.get("http://suninjuly.github.io/execute_script.html")

x = browser.find_element_by_css_selector("#input_value").text
res = calc(int(x))

answer_filed = browser.find_element_by_css_selector("#answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", answer_filed)
answer_filed.send_keys(res)

robot_check_box = browser.find_element_by_css_selector("#robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", robot_check_box)
robot_check_box.click()

robot_radio = browser.find_element_by_css_selector("#robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radio)
robot_radio.click()

submit_button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
submit_button.click()

browser.quit()
