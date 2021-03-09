import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--language', action='store',
        default='en-gb',
        help="Choose language: ru is default"
    )


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language").lower()
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    browser.language = user_language
    print(f"\nstart chrome browser for test with default language - {user_language}..")
    yield browser
    print("\nquit browser..")
    browser.quit()
