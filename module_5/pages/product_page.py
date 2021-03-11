from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_on_page_before_add_to_basket(self):
        self.should_be_add_to_basket_button()
        self.should_be_product_name()
        self.should_be_product_coast()
        self.should_not_be_success_message()

    def should_be_on_page_after_add_to_basket(self):
        self.should_be_success_message()
        self.should_be_basket_total_sum_alert_inner()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def should_be_product_coast(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_COAST), "Product coast is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def should_be_basket_total_sum_alert_inner(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_COAST_MESSAGE)

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def get_product_coast(self):
        products_coast = self.browser.find_element(*ProductPageLocators.PRODUCT_COAST)
        return products_coast.text

    def get_success_message(self):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        return success_message.text

    def get_shopping_cart_total_coast_message(self):
        basket_total_coast_alert_inner = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL_COAST_MESSAGE
        )
        return basket_total_coast_alert_inner.text

    def assert_product_name_and_coast_in_alert_inner(self):
        self.assert_product_name_in_success_message()
        self.assert_product_coast_in_coast_message()

    def assert_product_name_in_success_message(self):
        product_name_from_page = self.get_product_name()
        success_message = self.get_success_message()
        assert product_name_from_page in success_message, \
            f"Expected {product_name_from_page}, but got {success_message}"

    def assert_product_coast_in_coast_message(self):
        product_coast_from_page = self.get_product_coast()
        basket_total_coast_message = self.get_shopping_cart_total_coast_message()
        assert product_coast_from_page == basket_total_coast_message, \
            f"Expected {product_coast_from_page}, but got {basket_total_coast_message}"
