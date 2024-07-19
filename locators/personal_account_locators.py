from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    # кнопка "История заказов"
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")
    # карточка первого сделанного заказа
    FIRST_CREATED_BURGER = (By.XPATH, "//li[contains(@class,'OrderHistory_listItem')][1]")
    # карточка последнего сделанного заказа
    LAST_CREATED_BURGER = (By.XPATH, "//main//ul/li[last()]//p[@class='text text_type_digits-default']")
    # поле "Логин" профиля в ЛК
    PROFILE_LOGIN_INPUT = (By.XPATH, "//label[text()= 'Логин']/following-sibling::input")
    # кнопка "История заказов" в активном состоянии
    ACTIVE_ORDER_HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов' and contains(@class, 'link_active')]")
    # кнопка "Выйти"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()= 'Выход']")