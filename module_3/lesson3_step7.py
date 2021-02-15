from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options)
browser.get("http://suninjuly.github.io/get_attribute.html")

image = browser.find_element_by_css_selector("img")
valuex = image.get_attribute("valuex")
y = calc(valuex)
input_answer = browser.find_element_by_css_selector("#answer")
input_answer.send_keys(y)
check_box_robot = browser.find_element_by_css_selector("#robotCheckbox")
check_box_robot.click()
radio_button_robot = browser.find_element_by_css_selector("#robotsRule")
radio_button_robot.click()
submit_button = browser.find_element_by_css_selector("button[type='submit']")
submit_button.click()

