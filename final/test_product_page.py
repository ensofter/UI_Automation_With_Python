from .pages.product_page import ProductPage
import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time


class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                             ["offer1", "offer8"]
                             )
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo="

        # Arrange
        product_page = ProductPage(browser, link + promo_offer)
        product_page.open()

        # Act
        product_page.should_be_on_page_before_add_to_basket()
        product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_on_page_after_add_to_basket()

        # Assert
        product_page.assert_product_name_and_coast_in_alert_inner()


    def test_guest_cant_see_success_message(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

        # Arrange
        product_page = ProductPage(browser, link)
        product_page.open()

        # Act
        product_page.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

        # Arrange
        product_page = ProductPage(browser, link)
        product_page.open()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

        # Arrange
        product_page = ProductPage(browser, link)
        product_page.open()

        # Act
        product_page.should_be_login_link()
