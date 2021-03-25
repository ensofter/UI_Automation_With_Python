from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS), \
            "Items in basket is presented, but should not be"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS), \
            "Items in basket is presented, but should not be"

    def should_be_message_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Message is not presented"

    def get_message_that_basket_is_empty(self):
        message_basket_is_empty = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE)
        return message_basket_is_empty.text

    def assert_message_that_basket_is_empty(self):
        empty_message_from_page = self.get_message_that_basket_is_empty()
        assert "empty" in empty_message_from_page, f"Message that basket is empty is nit presented"
