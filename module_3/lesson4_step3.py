from selenium import webdriver
from selenium.webdriver.support.ui import Select


def sum_of_two(num1, num2):
    return int(num1) + int(num2)


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options)
browser.get("http://suninjuly.github.io/selects2.html")

num1 = browser.find_element_by_css_selector("#num1").text
num2 = browser.find_element_by_css_selector("#num2").text

res = sum_of_two(num1, num2)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(f"{res}")

submit_button = browser.find_element_by_tag_name("button")
submit_button.click()

browser.quit()

