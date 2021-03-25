import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--language', action='store',
        default='en-GB',
        help="Choose language: ru is default"
    )
    parser.addoption(
        '--browser_name',
        action='store',
        default=None,
        help="Choose browser: chrome or firefox"
    )


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language").lower()
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print(f"\nstart chrome browser for test with default language - {user_language}..")
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(10)
        browser.language = user_language
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print(f"\nstart firefox browser for test with default language - {user_language}..")
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.maximize_window()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
