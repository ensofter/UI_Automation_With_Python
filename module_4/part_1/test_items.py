link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


ADD_TO_CART_BUTTON_LOCATOR = ".btn-add-to-basket"

expected_result = {
    'ru': 'Добавить в корзину',
    'en-gb': 'Add to basket',
    'es': 'Añadir al carrito',
    'fr': 'Ajouter au panier'
}


def test_language_on_add_to_cart_button(browser, request):
    chosen_language = request.config.getoption("language").lower()
    browser.get(link)
    text_on_button = browser.find_element_by_css_selector(ADD_TO_CART_BUTTON_LOCATOR).text
    assert text_on_button == expected_result[chosen_language], f"Expected text {expected_result[chosen_language]}, but got {text_on_button}"

