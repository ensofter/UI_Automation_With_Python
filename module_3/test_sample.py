from selenium import webdriver

# Data
CATALOG_PAGE = "http://selenium1py.pythonanywhere.com/ru/catalogue/"

PRODUCT_LINK_LOCATOR = 'a[title="The shellcoder\'s handbook"]'
PRODUCT_H1_HEADER = "article h1"
PRODUCT_H1_HEADER_FOR_ASSERT = "The shellcoder's handbook"


def test_go_to_product_page_from_catalog_page():
    try:
        # Arrange
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        browser = webdriver.Chrome(chrome_options=options)
        browser.implicitly_wait(5)
        browser.get(CATALOG_PAGE)

        # Act
        browser.find_element_by_css_selector(PRODUCT_LINK_LOCATOR).click()

        # Assert
        product_h1_header_from_page = browser.find_element_by_css_selector(PRODUCT_H1_HEADER)
        assert PRODUCT_H1_HEADER_FOR_ASSERT in product_h1_header_from_page.text, \
            f"Expected '{PRODUCT_H1_HEADER_FOR_ASSERT}' H1 header, but got '{product_h1_header_from_page.text}'"

    finally:
        browser.quit()


test_go_to_product_page_from_catalog_page()
