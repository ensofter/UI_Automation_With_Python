from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), '100'))
book_button = browser.find_element_by_tag_name("button")
book_button.click()

x = browser.find_element_by_css_selector("#input_value").text
res = calc(int(x))

input_field = browser.find_element_by_css_selector("#answer")
input_field.send_keys(res)

button = browser.find_element_by_css_selector("#solve")
button.click()
