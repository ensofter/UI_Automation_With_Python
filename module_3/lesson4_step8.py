from selenium import webdriver
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test_file.txt')

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options)
browser.get("http://suninjuly.github.io/file_input.html")

f_name = browser.find_element_by_css_selector("input[name='firstname']")
f_name.send_keys("Alex")
l_name = browser.find_element_by_css_selector("input[name='lastname']")
l_name.send_keys("RomF")
email = browser.find_element_by_css_selector("input[name='email']")
email.send_keys('asd@asd.com')

file_input = browser.find_element_by_css_selector("#file")
file_input.send_keys(file_path)

submit_button = browser.find_element_by_tag_name("button")
submit_button.click()
