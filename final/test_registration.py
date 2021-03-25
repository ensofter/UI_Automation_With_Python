import pytest
from .pages.login_page import LoginPage
import time


@pytest.mark.personal_tests
class TestUserRegistration:

    def test_user_can_register(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = "QWERTY1488"

        # Arrange
        login_page = LoginPage(browser, link)
        login_page.open()

        # Act
        login_page.should_be_login_page()
        login_page.register_new_user(email, password)

        # Assert
        login_page.assert_success_message_after_registration(browser.language)

    def test_user_cant_use_already_used_email_for_another_registration(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        email = "test@test.ru"
        password = "QWERTY1488"

        # Arrange
        login_page = LoginPage(browser, link)
        login_page.open()

        # Act
        login_page.should_be_login_page()
        login_page.register_new_user(email, password)

        # Assert
        login_page.assert_danger_message_for_already_used_email(browser.language)
