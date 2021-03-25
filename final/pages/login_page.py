from .base_page import BasePage
from .locators import LoginPageLocators

success_message_after_registration = {
    'ru': 'Спасибо за регистрацию!',
    'en-gb': 'Thanks for registering!',
    'es': 'Gracias por registrarse!',
    'fr': 'Merci de vous être enregistré !'
}

danger_message_for_already_used_email = {
    'ru': 'Опаньки! Мы нашли какие-то ошибки',
    'en-gb': 'Oops! We found some errors',
    'es': 'Oops! Encontramos algunos errores',
    'fr': 'Oups ! Nous avons trouvé des erreurs'
}


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

    def should_be_icon_about_success_registration(self):
        assert self.is_element_present(*LoginPageLocators.SUCCESS_ICON_AFTER_REGISTRATION)

    def should_be_danger_message_for_already_used_email(self):
        assert self.is_element_present(*LoginPageLocators.DANGER_MESSAGE_FOR_ALREADY_USED_EMAIL)

    def get_message_about_success_registration(self):
        success_message = self.browser.find_element(*LoginPageLocators.SUCCESS_MESSAGE_AFTER_REGISTRATION)
        return success_message.text

    def get_danger_message_for_already_used_email(self):
        danger_message = self.browser.find_element(*LoginPageLocators.DANGER_MESSAGE_FOR_ALREADY_USED_EMAIL)
        return danger_message.text

    def assert_success_message_after_registration(self, language):
        self.should_be_icon_about_success_registration()
        success_message_from_page = self.get_message_about_success_registration()
        assert success_message_from_page == success_message_after_registration[language],\
            f"Expected text {success_message_after_registration[language]}, but got {success_message_from_page}"

    def assert_danger_message_for_already_used_email(self, language):
        self.should_be_danger_message_for_already_used_email()
        danger_message_from_page = self.get_danger_message_for_already_used_email()
        assert danger_message_from_page == danger_message_for_already_used_email[language],\
            f"Expected text {danger_message_for_already_used_email[language]}, but got {danger_message_from_page}"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_field.send_keys(password)
        repeat_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_REPEAT_PASSWORD)
        repeat_password_field.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
