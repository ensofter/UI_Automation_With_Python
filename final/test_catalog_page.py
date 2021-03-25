import pytest
from .pages.catalog_page import CatalogPage
from .pages.product_page import ProductPage
import time

# Data
link = "http://selenium1py.pythonanywhere.com/catalogue/"


@pytest.mark.personal_tests
class TestCatalogPage:

    def test_user_can_go_to_product_page(self, browser):
        # Arrange
        catalog_page = CatalogPage(browser, link)
        catalog_page.open()

        # Act
        catalog_page.should_be_on_page()
        product_data = catalog_page.get_product_data()
        catalog_page.go_to_product_page()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_be_on_page_before_add_to_basket()

        # Assert
        product_page.assert_product_name_product_price_with_data_from_catalog_page(product_data)

    def test_user_can_go_to_next_page(self, browser):
        # Arrange
        catalog_page = CatalogPage(browser, link)
        catalog_page.open()

        # Act
        catalog_page.should_be_on_page()
        catalog_page.go_to_next_page()

        # Assert
        catalog_page.assert_20_products_per_page()
        catalog_page.assert_total_results()
        catalog_page.assert_next_page_url_has_page_number_2()

    def test_user_can_go_to_previous_page(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/?page=3"

        # Arrange
        catalog_page = CatalogPage(browser, link)
        catalog_page.open()

        # Act
        catalog_page.should_be_on_page()
        catalog_page.go_to_previous_page()

        # Assert
        catalog_page.assert_20_products_per_page()
        catalog_page.assert_total_results()
        catalog_page.assert_next_page_url_has_page_number_2()

