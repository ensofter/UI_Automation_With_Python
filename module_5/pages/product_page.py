from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_on_page_before_add_to_shopping_cart(self):
        self.should_be_add_to_shopping_cart_button()
        self.should_be_product_name()
        self.should_be_product_coast()

    def should_be_on_page_after_add_to_shopping_cart(self):
        self.should_be_product_name_alert_inner()
        self.should_be_shopping_cart_total_sum_alert_inner()

    def should_be_add_to_shopping_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_SHOPPING_CART_BUTTON)

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME)

    def should_be_product_coast(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_COAST)

    def should_be_product_name_alert_inner(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_ALERT_INNER)

    def should_be_shopping_cart_total_sum_alert_inner(self):
        assert self.is_element_present(*ProductPageLocators.SHOPPING_CART_TOTAL_SUM_ALERT_INNER)

    def add_to_shopping_cart(self):
        add_to_shopping_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_SHOPPING_CART_BUTTON)
        add_to_shopping_cart_button.click()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def get_product_coast(self):
        products_coast = self.browser.find_element(*ProductPageLocators.PRODUCT_COAST)
        return products_coast.text

    def get_product_name_alert_inner(self):
        product_name_alert_inner = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERT_INNER)
        return product_name_alert_inner.text

    def get_shopping_cart_total_coast_alert_inner(self):
        shopping_cart_total_coast_alert_inner = self.browser.find_element(*ProductPageLocators.SHOPPING_CART_TOTAL_SUM_ALERT_INNER)
        return shopping_cart_total_coast_alert_inner.text

    def assert_product_name_and_coast_in_alert_inner(self):
        self.assert_product_name_in_alert_inner()
        self.assert_product_coast_in_alert_inner()

    def assert_product_name_in_alert_inner(self):
        product_name_from_page = self.get_product_name()
        product_name_from_alert_inner = self.get_product_name_alert_inner()
        assert product_name_from_page == product_name_from_alert_inner, f"Expected {product_name_from_page}, but got {product_name_from_alert_inner}"

    def assert_product_coast_in_alert_inner(self):
        product_coast_from_page = self.get_product_coast()
        product_coast_from_alert_inner = self.get_shopping_cart_total_coast_alert_inner()
        assert product_coast_from_page == product_coast_from_alert_inner, f"Expected {product_coast_from_page}, but got {product_coast_from_alert_inner}"

