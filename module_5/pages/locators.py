from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_SHOPPING_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_COAST = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_ALERT_INNER = (By.CSS_SELECTOR, ".alertinner strong")
    SHOPPING_CART_TOTAL_SUM_ALERT_INNER = (By.CSS_SELECTOR, ".alertinner p strong")
