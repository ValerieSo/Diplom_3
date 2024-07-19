import allure
from locators.home_page_locators import HomePageLocators
from page_objects.base_page import BasePage
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.click_button(HomePageLocators.BUTTON_CONSTRUCTOR)
        self.should_be_visible(HomePageLocators.LABEL_ASSEMBLE_BURGER)

    @allure.step('Находим заголовок секции "Конструктор"')
    def find_constructor_header(self):
        return self.wait_and_find_element(HomePageLocators.LABEL_ASSEMBLE_BURGER)

    @allure.step('Кликаем по кнопке "Лента заказов"')
    def click_orders_list_button(self):
        self.click_button(HomePageLocators.BUTTON_ORDER_LIST)
        self.should_be_visible(HomePageLocators.LABEL_ORDER_LIST)

    @allure.step('Находим заголовок секции "Лента заказов"')
    def find_orders_list_header(self):
        return self.wait_and_find_element(HomePageLocators.LABEL_ORDER_LIST)

    @allure.step('Кликаем на ингридиент в Конструкторе')
    # ингридиенты представлены набором, для тестовых данных выберем ингредиент до котрого необходимо скроллить
    def click_ingredient(self):
        self.scroll_to_element(HomePageLocators.TEST_INGREDIENT)
        self.click_button(HomePageLocators.TEST_INGREDIENT)
        self.should_be_visible(HomePageLocators.INGREDIENT_POPUP_WINDOW_TITLE)

    @allure.step('Находим всплывающее окно информации об ингредиенте')
    def find_popup_window(self):
        return self.wait_and_find_element(HomePageLocators.INGREDIENT_POPUP_WINDOW_TITLE)

    @allure.step('Получаем информацию из всплывающего окна информации об ингредиенте')
    def get_ingredient_info(self):
        self.should_be_visible(HomePageLocators.INGREDIENT_POPUP_WINDOW_TITLE)
        window_title = self.wait_and_find_element(HomePageLocators.INGREDIENT_POPUP_WINDOW_TITLE).text
        ingredient_name = self.wait_and_find_element(HomePageLocators.INGREDIENT_POPUP_WINDOW_INGR_NAME).text
        return window_title, ingredient_name

    @allure.step('Закрываем всплывающее окно информации об ингредиенте кликом по крестику')
    def close_popup_window(self):
        self.click_button(HomePageLocators.CLOSE_POPUP_WINDOW_BUTTON)
        self.should_not_be_visible(HomePageLocators.INGREDIENT_POPUP_WINDOW_TITLE)

    @allure.step('Перетаскиваем тестовый ингредиент в область формирования бургера')
    def add_ingredient_to_burger(self):
        self.scroll_to_element(HomePageLocators.TEST_INGREDIENT)
        element = self.find_clickable_element(HomePageLocators.TEST_INGREDIENT)
        target = self.wait_and_find_element(HomePageLocators.BURGER_TARGET)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    @allure.step('Перетаскиваем тестовую булочку в область формирования бургера')
    def add_buns_to_burger(self):
        element = self.find_clickable_element(HomePageLocators.TEST_BUN)
        target = self.wait_and_find_element(HomePageLocators.BUN_TARGET)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    @allure.step('Получаем значение счетчика тестового ингредиента')
    def get_ingredient_counter(self):
        try:
            self.should_be_visible(HomePageLocators.TEST_INGREDIENT)
        except ElementNotVisibleException:
            self.scroll_to_element(HomePageLocators.TEST_INGREDIENT)
        value = self.wait_and_find_element(HomePageLocators.INGREDIENT_COUNTER).text
        return value

    @allure.step('Закрываем всплывающее окно с информацией о заказе')
    def close_order_popup_window(self):
        self.click_button(HomePageLocators.CLOSE_POPUP_WINDOW_BUTTON)
        self.should_not_be_visible(HomePageLocators.CLOSE_POPUP_WINDOW_BUTTON)

    @allure.step('Делаем заказ')
    def make_an_order(self):
        self.find_constructor_header()
        self.add_buns_to_burger()
        self.add_ingredient_to_burger()
        self.click_button(HomePageLocators.BUTTON_MAKE_ORDER)

    @allure.step('Находим номер заказа в высплывающем окне')
    def find_order_number(self):
        try:
            self.should_not_be_visible(HomePageLocators.DAFAULT_ORDER_NUMBER)
            return self.wait_and_find_element(HomePageLocators.ORDER_NUMBER)
        except TimeoutException as e:
            print('Известный баг: драйвер firefox не сохраняет новый заказ, сохраняется дефолтный номер заказа, который не найти')
            return self.wait_and_find_element(HomePageLocators.DAFAULT_ORDER_NUMBER)

    @allure.step('Делаем заказ, запоминаем номер заказа и закрываем всплывающее окно')
    def make_an_order_remember_number_close_popup_window(self):
        self.make_an_order()
        self.finish_modal_loading()
        order_number = self.find_order_number().text
        self.finish_modal_loading()
        self.close_order_popup_window()
        return order_number

    @allure.step('Переходим в личный кабинет по кнопке в хэдере')
    def go_to_personal_account(self):
        self.should_be_visible(HomePageLocators.PERSONAL_ACCOUNT)
        self.click_button(HomePageLocators.PERSONAL_ACCOUNT)
        self.finish_modal_loading()
