from .base_page import BasePage
from .locators import CatalogPageLocators


class CatalogPage(BasePage):

    def should_be_on_page(self):
        self.should_be_login_url()
        self.should_be_total_results()
        self.should_be_nex_page_button()
        self.should_be_product_card()
        self.should_be_product_header()
        self.should_be_product_price()
        self.should_be_product_availability()
        self.should_be_add_to_cart_button()

    def should_be_login_url(self):
        assert "catalogue" in self.browser.current_url, "Current url doesn't have 'catalogue' in url"

    def should_be_total_results(self):
        assert self.is_element_present(*CatalogPageLocators.TOTAL_RESULTS), "Total Results isn't displayed"

    def should_be_nex_page_button(self):
        assert self.is_element_present(*CatalogPageLocators.NEXT_PAGE_BUTTON), "Next Page Button isn't displayed"

    def should_be_product_card(self):
        assert self.is_element_present(*CatalogPageLocators.PRODUCT_CARD), "Product Card isn't presented"

    def should_be_product_header(self):
        assert self.is_element_present(*CatalogPageLocators.PRODUCT_HEADER), "Product Header isn't presented"

    def should_be_product_price(self):
        assert self.is_element_present(*CatalogPageLocators.PRODUCT_PRICE), "Product Price isn't presented"

    def should_be_product_availability(self):
        assert self.is_element_present(*CatalogPageLocators.PRODUCT_AVAILABILITY), "Product Availability isn't presented"

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*CatalogPageLocators.ADD_TO_CART_BUTTON), "Add to cart button isn't presented"

    def get_product_header(self):
        product_header = self.browser.find_element(*CatalogPageLocators.PRODUCT_HEADER)
        return product_header.text

    def get_product_price(self):
        product_price = self.browser.find_element(*CatalogPageLocators.PRODUCT_PRICE)
        return product_price.text

    def get_product_data(self):
        return [self.get_product_header(), self.get_product_price()]

    def get_total_products_on_first_page(self):
        products_on_page = self.browser.find_elements(*CatalogPageLocators.PRODUCT_CARDS)
        return products_on_page

    def get_total_results_on_page(self):
        total_results_on_page = self.browser.find_element(*CatalogPageLocators.TOTAL_RESULTS)
        return total_results_on_page.text

    def go_to_product_page(self):
        product_header = self.browser.find_element(*CatalogPageLocators.PRODUCT_HEADER).click()

    def go_to_next_page(self):
        self.browser.find_element(*CatalogPageLocators.NEXT_PAGE_BUTTON).click()

    def go_to_previous_page(self):
        self.browser.find_element(*CatalogPageLocators.PREVIOUS_PAGE_BUTTON).click()

    def assert_20_products_per_page(self):
        total_product_on_page = self.get_total_products_on_first_page()
        assert len(total_product_on_page) == 20, "Products less then 20"

    def assert_total_results(self):
        total_results = self.get_total_results_on_page()
        assert int(total_results) == 201, "Total products not 201"

    def assert_next_page_url_has_page_number_2(self):
        assert "?page=2" in self.browser.current_url, "Current url doesn't have '?page=2' in url"


