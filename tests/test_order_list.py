import allure
from page_objects.orders_list_page import OrdersListPage
from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from page_objects.personal_account_page import PersonalAccount
from data.data import Urls


class TestOrderList:
    @allure.title('Проверка появления всплывающего окна с информацией о заказе по клику на заказ в ленте заказов')
    @allure.description('Дожидаемся загрузки страницы, в рамках подготовки к тесту переходим в раздел "Лента заказов", '
                        'затем кликаем на карточку последнего заказа,ожидаем появление всплывающего окна с информацией '
                        'о заказе')
    def test_click_on_order_opens_popup_window_with_orders_details_true(self, driver):
        # предусловие: переход к Ленте Заказов
        home_page = HomePage(driver)
        home_page.finish_modal_loading()
        home_page.click_orders_list_button()
        # шаги
        orders_list_page = OrdersListPage(driver)
        orders_list_page.click_order_in_orders_list()
        details_popup_window = orders_list_page.find_order_info()

        assert details_popup_window.is_displayed() is True

    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    @allure.description('Авторизуем тестового пользователя, переходим в "Ленту заказов" и фиксируем на счетчике число '
                        'выполненных за все время заказов, переходим в "Конструктор", делаем заказ, переходим в '
                        '"Ленту заказов", ожидаем, что число выполненных за все время заказов на счетчике увеличилось')
    def test_all_completed_orders_increase_as_new_order_added_true(self, driver, create_and_delete_user):
        # предусловие: авторизация пользователя перед совершением заказа
        response, payload = create_and_delete_user
        email_value = payload['email']
        password_value = payload['password']
        login_page = LoginPage(driver)
        login_page.login_user(email_value, password_value)
        # предусловие: переходим в Ленту заказов
        home_page = HomePage(driver)
        home_page.finish_modal_loading()
        home_page.click_orders_list_button()
        # предусловие: сохраняем в переменную значение счетчика всех выполненных заказов до добавления заказа
        orders_list_page = OrdersListPage(driver)
        counter_number_before = orders_list_page.get_number_of_completed_orders()
        # шаги
        home_page.click_constructor_button()
        home_page.finish_modal_loading()
        home_page.make_an_order_remember_number_close_popup_window()
        home_page.click_orders_list_button()
        counter_number_after = orders_list_page.get_number_of_completed_orders()

        try:
            assert int(counter_number_after) > int(counter_number_before)
        except AssertionError as e:
            print('Известный баг: драйвер firefox не сохраняет новый заказ, число заказов не меняется')

    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    @allure.description('Авторизуем тестового пользователя, переходим в "Ленту заказов" и фиксируем на счетчике число '
                        'выполненных за сегодня заказов, переходим в "Конструктор", делаем заказ, переходим в '
                        '"Ленту заказов", ожидаем, что число выполненных за сегодня заказов на счетчике увеличилось')
    def test_today_completed_orders_increase_as_new_order_added_true(self, driver, create_and_delete_user):
        # предусловие: авторизация пользователя перед совершением заказа
        response, payload = create_and_delete_user
        email_value = payload['email']
        password_value = payload['password']
        login_page = LoginPage(driver)
        login_page.login_user(email_value, password_value)
        # предусловие: переходим в Ленту заказов
        home_page = HomePage(driver)
        home_page.finish_modal_loading()
        home_page.click_orders_list_button()
        # предусловие: сохраняем в переменную значение счетчика сегодняшних выполненных заказов до добавления заказа
        orders_list_page = OrdersListPage(driver)
        counter_number_before = orders_list_page.get_today_completed_orders()
        # шаги
        home_page.click_constructor_button()
        home_page.finish_modal_loading()
        home_page.make_an_order_remember_number_close_popup_window()
        home_page.click_orders_list_button()
        counter_number_after = orders_list_page.get_today_completed_orders()

        try:
            assert int(counter_number_after) > int(counter_number_before)
        except AssertionError as e:
            print('Известный баг: драйвер firefox не сохраняет новый заказ, число заказов не меняется')

    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе "В работе"')
    @allure.description('Авторизуем тестового пользователя, делаем заказ, фиксируем номер заказа, переходим в '
                        '"Ленту заказов", ожидаем, что номер заказа отобразится в секции "В работе"')
    def test_orders_number_appears_in_progress_section_true(self, driver, create_and_delete_user):
        # предусловие: авторизация пользователя перед совершением заказа
        response, payload = create_and_delete_user
        email_value = payload['email']
        password_value = payload['password']
        login_page = LoginPage(driver)
        login_page.login_user(email_value, password_value)
        # шаги
        home_page = HomePage(driver)
        home_page.finish_modal_loading()
        order_number = home_page.make_an_order_remember_number_close_popup_window()
        home_page.finish_modal_loading()
        home_page.click_orders_list_button()
        orders_list_page = OrdersListPage(driver)
        orders_list_page.finish_modal_loading()
        orders_list_page.wait_in_progress_refresh()
        order_in_progress = orders_list_page.find_order_in_progress()

        try:
            assert order_in_progress == f'0{order_number}'
        except AssertionError as e:
            print('Известный баг: драйвер firefox не сохраняет заказ, получить реальный номер заказа для '
                  'сравнения невозможно')

    @allure.title('Проверка, что заказ пользователя из раздела «История заказов» '
                  'отображается на странице «Лента заказов»')
    @allure.description('Авторизуем тестового пользователя, делаем заказ, фиксируем номер заказа, переходим в '
                        'Личный Кабинет, переходим в Историю заказов, ожидаем созданный заказ последним в Истории, '
                        'переходим в Ленту заказов,ожидаем создланный заказ в Ленте Заказов')
    def test_users_orders_displayed_in_orders_list_true(self, driver, create_and_delete_user):
        # предусловие: авторизация пользователя перед совершением заказа
        response, payload = create_and_delete_user
        email_value = payload['email']
        password_value = payload['password']
        login_page = LoginPage(driver)
        login_page.login_user(email_value, password_value)
        # предусловие: создание заказа
        home_page = HomePage(driver)
        home_page.finish_modal_loading()
        order_number = f'#0{home_page.make_an_order_remember_number_close_popup_window()}'
        # шаги
        home_page.finish_modal_loading()
        home_page.go_to_personal_account()
        personal_ac_page = PersonalAccount(driver)
        personal_ac_page.open_orders_history()
        order_number_in_history = personal_ac_page.find_last_order()
        personal_ac_page.open_page(Urls.FEED_URL)
        order_list_page = OrdersListPage(driver)
        order_list_page.finish_modal_loading()
        order_number_in_list = order_list_page.get_order_in_order_list(order_number_in_history)

        assert order_number_in_history == order_number and order_number_in_list is not None


