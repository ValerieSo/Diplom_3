import allure
from page_objects.personal_account_page import PersonalAccount
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from data.data import TestAuthorizationData, Urls


class TestPersonalAccount:
    @allure.title('Проверяем переход авторизованного пользователя по клику на кнопку "Личный кабинет"'
                  ' в хэдере приложения')
    @allure.description('Авторизуем тестового пользователя, кликаем по кнопке "Личный кабинет" в хэдере приложения, '
                        'ожидаем переход в "Личный кабинет" тестового пользователя')
    def test_auth_user_clicking_personal_account_button_opened_personal_account_page(self, driver, create_and_delete_user):
        # предусловие: авторизация тестового пользователя
        response, payload = create_and_delete_user
        email_value = payload['email']
        password_value = payload['password']
        login_page = LoginPage(driver)
        login_page.login_user(email_value, password_value)
        # шаги
        home_page = HomePage(driver)
        home_page.finish_modal_loading()
        home_page.go_to_personal_account()
        personal_ac_page = PersonalAccount(driver)
        personal_ac_page.finish_modal_loading()
        login_input_value = personal_ac_page.get_login_from_personal_account()
        current_url = personal_ac_page.get_current_url()

        assert current_url == Urls.PERSONAL_ACCOUNT_URL and login_input_value == email_value

    @allure.title('Проверяем переход неавторизованного пользователя по клику на кнопку "Личный кабинет" '
                  'в хэдере приложения')
    @allure.description('дожидаемся загрузки страницы, кликаем по кнопке "Личный кабинет" в хэдере приложения, '
                        'ожидаем переход на страницу авторизации ')
    def test_unauth_user_clicking_personal_account_button_opens_authorization_page(self, driver):
        home_page = HomePage(driver)
        home_page.finish_modal_loading()
        home_page.go_to_personal_account()
        login_page = LoginPage(driver)
        current_url = login_page.get_current_url()
        login_input = login_page.find_login_input()

        assert current_url == Urls.LOGIN_URL and login_input.is_displayed()

    @allure.title('Проверяем, переход в раздел «История заказов»')
    @allure.description('Авторизуем тестового пользователя, кликаем по кнопке "Личный кабинет" в хэдере приложения, '
                        'кликаем по кнопке "История заказов", ожидаем переход к истории заказов и переход кнопки '
                        '"История заказов" в активное состояние')
    def test_auth_user_clicking_order_history_button(self, driver, create_and_delete_user):
        # предусловие: авторизация тестового пользователя
        response, payload = create_and_delete_user
        email_value = payload['email']
        password_value = payload['password']
        login_page = LoginPage(driver)
        login_page.login_user(email_value, password_value)
        # предусловие: переход в личный кабинет
        home_page = HomePage(driver)
        home_page.finish_modal_loading()
        home_page.go_to_personal_account()
        # шаги
        personal_ac_page = PersonalAccount(driver)
        personal_ac_page.finish_modal_loading()
        personal_ac_page.open_orders_history()
        personal_ac_page.finish_modal_loading()
        check_orders_history = personal_ac_page.check_if_orders_history_active()
        current_url = personal_ac_page.get_current_url()

        assert current_url == Urls.ORDERS_HISTORY_URL and check_orders_history is not None

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Авторизуем тестового пользователя, кликаем по кнопке "Личный кабинет" в хэдере приложения, '
                        'кликаем по кнопке "Выход", ожидаем переход на страницу авторизации')
    def test_logout_by_clicking_logout_button(self, driver, create_and_delete_user):
        # предусловие: авторизация тестового пользователя
        response, payload = create_and_delete_user
        email_value = payload['email']
        password_value = payload['password']
        login_page = LoginPage(driver)
        login_page.login_user(email_value, password_value)
        # предусловие: переход в личный кабинет
        home_page = HomePage(driver)
        home_page.finish_modal_loading()
        home_page.go_to_personal_account()
        # шаги
        personal_ac_page = PersonalAccount(driver)
        personal_ac_page.finish_modal_loading()
        personal_ac_page.click_logout_button()
        login_page = LoginPage(driver)
        login_input = login_page.find_login_input()
        current_url = login_page.get_current_url()

        assert current_url == Urls.LOGIN_URL and login_input.is_displayed()
