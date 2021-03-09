from .pages.product_page import ProductPage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo="


@pytest.mark.parametrize('promo_offer',
                         ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", pytest.param("offer7", marks=pytest.mark.xfail), "offer8",
                          "offer9"]
                         )
class TestProductPage:
    def test_guest_can_add_product_to_shopping_cart(self, browser, promo_offer):
        product_page = ProductPage(browser, link+promo_offer)
        product_page.open()
        product_page.should_be_on_page_before_add_to_shopping_cart()
        product_page.add_to_shopping_cart()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_on_page_after_add_to_shopping_cart()
        product_page.assert_product_name_and_coast_in_alert_inner()
