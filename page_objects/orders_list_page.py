import allure
from locators.orders_list_locators import OrdersListLocators
from page_objects.base_page import BasePage
from selenium.common.exceptions import TimeoutException



class OrdersListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем на заказ в ленте заказов')
    def click_order_in_orders_list(self):
        self.click_button(OrdersListLocators.LAST_ORDER)

    @allure.step('Находим текст во всплывающем окне с информацией о заказе')
    def find_order_info(self):
        return self.wait_and_find_element(OrdersListLocators.ORDER_POPUP_WINDOW_COMPOSITION)

    @allure.step('Получаем число заказов, выполненных за все время')
    def get_number_of_completed_orders(self):
        all_completed_orders = self.wait_and_find_element(OrdersListLocators.ALL_COMPLETED_ORDERS)
        number = all_completed_orders.text
        return number

    @allure.step('Получаем число заказов, выполненных за сегодня')
    def get_today_completed_orders(self):
        today_completed_orders = self.wait_and_find_element(OrdersListLocators.TODAY_COMPLETED_ORDERS)
        number = today_completed_orders.text
        return number

    @allure.step('Ждем, пока обновится лента "В работе"')
    def wait_in_progress_refresh(self):
        try:
            self.should_not_be_visible(OrdersListLocators.DEFAULT_IN_PROGRESS)
        except TimeoutException as e:
            print('Известный баг: драйвер firefox не сохраняет новый заказ, сохраняется дефолтная фраза')


    @allure.step('Находим номер заказа в секции "В работе"')
    def find_order_in_progress(self):
        last_order_in_progress = self.wait_and_find_element(OrdersListLocators.ORDER_IN_PROGRESS)
        number = last_order_in_progress.text
        return number

    @allure.step('Ищем нужный номер заказа в списке заказов')
    def get_order_in_order_list(self, order_number):
        locator = self.format_locators(OrdersListLocators.ORDER_NUMBER_IN_LIST, order_number)
        order = self.wait_and_find_element(locator)
        return order
