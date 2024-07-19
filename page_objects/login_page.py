import allure
from locators.login_page_locators import LoginPageLocators
from page_objects.base_page import BasePage
from data.data import TestAuthorizationData, Urls


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Находим поле ввода логина')
    def find_login_input(self):
        return self.wait_and_find_element(LoginPageLocators.LOGIN_INPUT_EMAIL)

    @allure.step('Вводим логин')
    def set_login(self, email_value):
        email = self.wait_and_find_element(LoginPageLocators.LOGIN_INPUT_EMAIL)
        email.send_keys(email_value)

    @allure.step('Вводим пароль')
    def set_password(self, password_value):
        pwd = self.wait_and_find_element(LoginPageLocators.LOGIN_INPUT_PWD)
        pwd.send_keys(password_value)

    @allure.step('Авторизация пользователя')
    def login_user(self, email_value, password_value):
        self.open_page(Urls.LOGIN_URL)
        self.finish_modal_loading()
        self.set_login(email_value)
        self.set_password(password_value)
        self.click_button(LoginPageLocators.BUTTON_LOGIN)

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_password_recovery_button(self):
        self.should_be_visible(LoginPageLocators.PASSWORD_RECOVERY_BUTTON)
        self.click_button(LoginPageLocators.PASSWORD_RECOVERY_BUTTON)
        self.finish_modal_loading()
