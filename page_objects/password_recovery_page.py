import allure
from locators.password_recovery_locators import PasswordRecoveryLocators
from page_objects.base_page import BasePage
from data.data import TestAuthorizationData


class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Находим заголовок "Восстановление пароля"')
    def find_password_recovery_label(self):
        self.finish_modal_loading()
        return self.wait_and_find_element(PasswordRecoveryLocators.PASSWORD_RECOVERY_LABEL)

    @allure.step('Вводим email в поле восстановления пароля')
    def set_email_in_recovery_from(self):
        self.should_be_visible(PasswordRecoveryLocators.RECOVERY_EMAIL_INPUT)
        recovery_email_input = self.wait_and_find_element(PasswordRecoveryLocators.RECOVERY_EMAIL_INPUT)
        recovery_email_input.send_keys(TestAuthorizationData.test_login)

    @allure.step('Нажимаем кнопку "Восстановить"')
    def click_recover_button(self):
        self.click_button(PasswordRecoveryLocators.RECOVER_BUTTON)
        self.should_be_visible(PasswordRecoveryLocators.RECOVERY_PWD_INPUT)

    @allure.step('Находим поле ввода пароля в форме восстановления пароля')
    def find_password_input_in_restoration_password_form(self):
        return self.wait_and_find_element(PasswordRecoveryLocators.RECOVERY_PWD_INPUT)

    @allure.step('Переходим к форме обновления пароля')
    def go_to_password_reset_form(self):
        self.set_email_in_recovery_from()
        self.click_recover_button()

    @allure.step('Кликаем на кнопку "Показать/скрыть пароль"')
    def click_show_hide_button(self):
        self.should_be_visible(PasswordRecoveryLocators.SHOW_HIDE_BUTTON)
        self.click_button(PasswordRecoveryLocators.SHOW_HIDE_BUTTON)

    @allure.step('Находим поле ввода значения password в форме восстановления пароля в активном состоянии')
    def find_active_input_new_password(self):
        return self.wait_and_find_element(PasswordRecoveryLocators.ACTIVE_RECOVERY_PWD_INPUT)
