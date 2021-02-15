from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options)
browser.get("http://suninjuly.github.io/alert_accept.html")

button = browser.find_element_by_tag_name("button")
button.click()
alert = browser.switch_to.alert
alert.accept()

x = browser.find_element_by_css_selector("#input_value").text
res = calc(int(x))

input_field = browser.find_element_by_css_selector("#answer")
input_field.send_keys(res)

button = browser.find_element_by_tag_name("button")
button.click()
