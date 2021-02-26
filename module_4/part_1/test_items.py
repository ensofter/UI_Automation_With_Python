# Data
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
expected_result = {
    'ru': 'Добавить в корзину',
    'en-gb': 'Add to basket',
    'es': 'Añadir al carrito',
    'fr': 'Ajouter au panier'
}

ADD_TO_CART_BUTTON_LOCATOR = ".btn-add-to-basket"


def test_language_on_add_to_cart_button(browser):
    # Arrange
    browser.get(link)

    # Act
    text_on_button = browser.find_element_by_css_selector(ADD_TO_CART_BUTTON_LOCATOR).text

    # Assert
    assert text_on_button == expected_result[browser.language], f"Expected text {expected_result[browser.language]}, but got {text_on_button}"
