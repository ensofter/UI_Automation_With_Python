from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest


link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.should_be_login_link()
        main_page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.should_be_login_link()


class TestProductInBasket:
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.should_be_basket_button()
        main_page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_items_in_basket()
        basket_page.should_be_message_that_basket_is_empty()
        basket_page.assert_message_that_basket_is_empty()


