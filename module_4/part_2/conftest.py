import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    print(f"\nstart chrome browser for test")
    yield browser
    print("\nquit browser")
    browser.quit()
