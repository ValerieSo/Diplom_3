import allure
from page_objects.login_page import LoginPage
from page_objects.password_recovery_page import PasswordRecoveryPage
from data.data import Urls


class TestPasswordRecoveryPage:
    @allure.title('Проверка перехода на страницу восстановления пароля по клику по кнопке «Восстановить пароль»')
    @allure.description('Переходим на страницу авторизации, кликаем на кнопку "Восстановить пароль", '
                        'ожидаем открытие страницы восстановления пароля')
    def test_clicking_password_recovery_button_opened_password_recovery_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.LOGIN_URL)
        login_page.finish_modal_loading()
        login_page.click_password_recovery_button()
        pwd_recovery_page = PasswordRecoveryPage(driver)
        pwd_recovery_label = pwd_recovery_page.find_password_recovery_label()
        current_url = pwd_recovery_page.get_current_url()

        assert current_url == Urls.PWD_RECOVERY_URL and pwd_recovery_label.is_displayed()

    @allure.title('Проверка ввода почты и клика по кнопке «Восстановить»')
    @allure.description('Переходим на страницу авторизации, кликаем на кнопку "Восстановить пароль", в поле "email" '
                        'вводим тестовый email, кликаем по кнопке "Восстановить", ожидаем открытия страницы ввода '
                        'нового пароля')
    def test_password_recovery_email_submission(self, driver):
        # предусловие: переход к форме восстановленя пароля
        login_page = LoginPage(driver)
        login_page.open_page(Urls.LOGIN_URL)
        login_page.finish_modal_loading()
        login_page.click_password_recovery_button()
        # шаги
        pwd_recovery_page = PasswordRecoveryPage(driver)
        pwd_recovery_page.set_email_in_recovery_from()
        pwd_recovery_page.click_recover_button()
        recovery_password_input = pwd_recovery_page.find_password_input_in_restoration_password_form()
        current_url = pwd_recovery_page.get_current_url()

        assert current_url == Urls.RESET_PWD_URL and recovery_password_input.is_displayed()

    @allure.title('Проверка, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description('Переходим на страницу авторизации, кликаем на кнопку "Восстановить пароль", в поле "email" '
                        'вводим тестовый email, кликаем по кнопке "Восстановить", кликаем по кнопке '
                        '"Показать/скрыть пароль", ожидаем, что поле ввода подсвечивается синим')
    def test_show_activates_password_field(self, driver):
        # предусловие: переход к форме восстановленя пароля
        login_page = LoginPage(driver)
        login_page.open_page(Urls.LOGIN_URL)
        login_page.finish_modal_loading()
        login_page.click_password_recovery_button()
        # предусловие: переход к форме обновления пароля
        pwd_recovery_page = PasswordRecoveryPage(driver)
        pwd_recovery_page.go_to_password_reset_form()
        # шаги
        pwd_recovery_page.finish_modal_loading()
        pwd_recovery_page.click_show_hide_button()
        active_pwd_input = pwd_recovery_page.find_active_input_new_password()

        assert active_pwd_input.is_displayed()
