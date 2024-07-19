import allure
from locators.personal_account_locators import PersonalAccountLocators
from page_objects.base_page import BasePage
from selenium.common.exceptions import TimeoutException


class PersonalAccount(BasePage):
    @allure.step('Открываем историю заказов')
    def open_orders_history(self):
        self.finish_modal_loading()
        self.should_be_visible(PersonalAccountLocators.ORDER_HISTORY_BUTTON)
        self.click_button(PersonalAccountLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Находим номер последнего сделанного заказа')
    def find_last_order(self):
        last_order = self.wait_and_find_element(PersonalAccountLocators.LAST_CREATED_BURGER)
        last_orders_number = last_order.text
        return last_orders_number

    @allure.step('Получаем логин пользователя в "Личном кабинете"')
    def get_login_from_personal_account(self):
        return self.get_attribute_of_element(PersonalAccountLocators.PROFILE_LOGIN_INPUT, 'value')

    @allure.step('Проверяем, что поле "История заказов" активно')
    def check_if_orders_history_active(self):
        try:
            active_orders_history = self.wait_and_find_element(PersonalAccountLocators.ACTIVE_ORDER_HISTORY_BUTTON)
            return active_orders_history
        except TimeoutException as e:
            print('Поле "История заказов" не активно')
            return None

    @allure.step('Кликаем на кнопку "Выйти"')
    def click_logout_button(self):
        self.finish_modal_loading()
        self.should_be_visible(PersonalAccountLocators.LOGOUT_BUTTON)
        self.click_button(PersonalAccountLocators.LOGOUT_BUTTON)
