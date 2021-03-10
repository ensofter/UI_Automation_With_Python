from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.should_be_register_email()
        self.should_be_register_password()
        self.should_be_register_repeat_password()
        self.should_be_register_button()

    def should_be_login_url(self):
        print('!!!!!!!!!!!!!!!!!!!!!!!', self.browser.current_url)
        assert "login" in self.browser.current_url, "Current url doesn't have 'login' in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form isn't displayed"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form isn't displayed"

    def should_be_register_email(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Registration email field isn't displayed"

    def should_be_register_password(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), \
            "Registration password field isn't displayed"

    def should_be_register_repeat_password(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_REPEAT_PASSWORD), \
            "Registration repeat password field isn't displayed"

    def should_be_register_button(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), \
            "Registration button isn't displayed"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_field.send_keys(password)
        repeat_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_REPEAT_PASSWORD)
        repeat_password_field.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
