from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REGISTER_REPEAT_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_COAST = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) div")
    BASKET_TOTAL_COAST_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(3) div p strong")


class BasketPageLocators:
    ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
