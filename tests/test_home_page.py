import allure
from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage

class TestHomePage:
    @allure.title('Проверка перехода в конструктор по клику на кнопку «Конструктор»')
    @allure.description('Дожидаемся загрузки страницы, в рамках подготовки к тесту переходим в раздел "Лента заказов" '
                        'т.к. "Конструктор" загружается с стартовой страницей, затем кликаем на кнопку "Конструктор",'
                        ' ожидаем появление раздела "Собери бургер"')
    def test_open_constructor_section_by_clicking_on_constructor_button_success(self, driver):
        home_page = HomePage(driver)
        # предусловие: переходим в секцию "Лента заказов"
        home_page.finish_modal_loading()
        home_page.click_orders_list_button()
        # шаги
        home_page.click_constructor_button()
        section_header = home_page.find_constructor_header()

        assert section_header.is_displayed()

    @allure.title('Проверка перехода к ленте заказов по клику на кнопку «Лента заказов»')
    @allure.description('Дожидаемся загрузки страницы, затем кликаем на кнопку "Лента заказов", ожидаем появление '
                        'раздела "Лента заказов"')
    def test_open_order_list_section_by_clicking_on_order_list_button_success(self, driver):
        home_page = HomePage(driver)
        home_page.finish_modal_loading()
        home_page.click_orders_list_button()
        section_header = home_page.find_orders_list_header()

        assert section_header.is_displayed() is True

    @allure.title('Проверка открытия по клику на ингридиент всплывающего окна с деталями об ингридиенте')
    @allure.description('Дожидаемся загрузки страницы, скроллим конструктор до тестового ингредиента, кликаем '
                        'по карточке тестового ингредиента, ожидаем появление всплывающего окна с информацией '
                        'об ингредиенте')
    def test_open_ingredients_popup_window_by_clicking_on_ingredient_success(self, driver):
        home_page = HomePage(driver)
        home_page.finish_modal_loading()
        home_page.click_ingredient()
        window_title, ingredient_name = home_page.get_ingredient_info()

        assert window_title == 'Детали ингредиента' and ingredient_name == 'Биокотлета из марсианской Магнолии'

    @allure.title('Проверка закрытия всплывающего окна с деталями об ингредиенте по клику на крестик в окне')
    @allure.description('Дожидаемся загрузки страницы, скроллим конструктор до тестового ингредиента, кликаем '
                        'по карточке тестового ингредиента, ожидаем появление всплывающего окна с информацией '
                        'об ингредиенте, кликаем на крестик в правом верхнем углу окна, ожидаем закрытие окна')
    def test_close_ingredients_popup_window_by_clicking_on_close_button_success(self, driver):
        home_page = HomePage(driver)
        home_page.finish_modal_loading()
        home_page.click_ingredient()
        popup_window = home_page.find_popup_window()
        home_page.close_popup_window()

        assert popup_window.is_displayed() is False

    @allure.title('Проверка, что при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    @allure.description('Дожидаемся загрузки страницы, скроллим конструктор до тестового ингредиента, перетягиваем '
                        'тестовый ингредиент в зону формирования бургера, ожидаем увеличение счетчика ингредиента до 1')
    def test_ingredient_counter_groves_when_add_ingredient_true(self, driver):
        home_page = HomePage(driver)
        home_page.finish_modal_loading()
        home_page.add_ingredient_to_burger()
        counter_value = home_page.get_ingredient_counter()

        assert counter_value == '1'

    @allure.title('Залогиненный пользователь может оформить заказ')
    @allure.description('Дожидаемся загрузки страницы, в рамках подготовки тестового окружения кликаем по кнопке '
                        '"Войти в аккаунт", авторизуем тестового кользователя, дожидаемся перенаправления на страницу '
                        'Конструктора, создаем заказ и нажимаем кнопку "Оформить", ожидаем появления всплывающего окна '
                        'с номером заказа')
    def test_auth_user_create_order_success(self, driver, create_and_delete_user):
        # предусловие: логин пользователя
        response, payload = create_and_delete_user
        email_value = payload['email']
        password_value = payload['password']
        login_page = LoginPage(driver)
        login_page.login_user(email_value, password_value)
        # шаги
        home_page = HomePage(driver)
        home_page.finish_modal_loading()
        home_page.make_an_order()
        order_number = home_page.find_order_number()

        assert order_number.is_displayed() and order_number.text is not '9999'


