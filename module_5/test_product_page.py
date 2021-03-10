from .pages.product_page import ProductPage
import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time


class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                         ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                          pytest.param("offer7", marks=pytest.mark.xfail), "offer8",
                          "offer9"]
                         )
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo="
        product_page = ProductPage(browser, link+promo_offer)
        product_page.open()
        product_page.should_be_on_page_before_add_to_basket()
        product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_on_page_after_add_to_basket()
        product_page.assert_product_name_and_coast_in_alert_inner()

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket()
        product_page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_login_link()
        product_page.go_to_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_basket_button()
        product_page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_items_in_basket()
        basket_page.should_be_message_that_basket_is_empty()
        basket_page.assert_message_that_basket_is_empty()


@pytest.mark.register
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = "QWERTY1488"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.should_be_login_page()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()


    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_on_page_before_add_to_basket()
        product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_on_page_after_add_to_basket()
        product_page.assert_product_name_and_coast_in_alert_inner()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()
