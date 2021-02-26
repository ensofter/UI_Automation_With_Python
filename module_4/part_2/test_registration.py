# Data
link = "http://selenium1py.pythonanywhere.com"
test_email = "aewwwksey_raa@gmail.com"
test_password = "password"
expected_thx_text = 'Thanks for registering!'

LOGIN_LNK_LOCATOR = "#login_link"
EMAIL_FIELD_LOCATOR = "#id_registration-email"
PASSWORD_FIELD_LOCATOR = "#id_registration-password1"
REPEAT_PASSWORD_FIELD_LOCATOR = "#id_registration-password2"
SUBMIT_BUTTON_LOCATOR = "button[name='registration_submit']"
ALERT_THX_TEXT_LOCATOR = ".alertinner.wicon"


def test_registration_new_user(browser):
    # Arrange
    browser.get(link)

    # Act
    browser.find_element_by_css_selector(LOGIN_LNK_LOCATOR).click()
    email_field = browser.find_element_by_css_selector(EMAIL_FIELD_LOCATOR)
    email_field.send_keys(test_email)
    password_field = browser.find_element_by_css_selector(PASSWORD_FIELD_LOCATOR)
    password_field.send_keys(test_password)
    repeat_password_field = browser.find_element_by_css_selector(REPEAT_PASSWORD_FIELD_LOCATOR)
    repeat_password_field.send_keys(test_password)
    browser.find_element_by_css_selector(SUBMIT_BUTTON_LOCATOR).click()
    thx_text_from_page = browser.find_element_by_css_selector(ALERT_THX_TEXT_LOCATOR).text

    # Assert
    assert thx_text_from_page == expected_thx_text, f"Expected text - {expected_thx_text}, but got {thx_text_from_page}"
