from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options)
browser.get("http://suninjuly.github.io/math.html")

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)
input_answer = browser.find_element_by_css_selector("#answer")
input_answer.send_keys(y)
check_box_robot = browser.find_element_by_css_selector("label[for='robotCheckbox']")
check_box_robot.click()
radio_button_robot = browser.find_element_by_css_selector("label[for='robotsRule']")
radio_button_robot.click()
submit_button = browser.find_element_by_css_selector("button[type='submit']")
submit_button.click()

