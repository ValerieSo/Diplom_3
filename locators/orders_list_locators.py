from selenium.webdriver.common.by import By


class OrdersListLocators:
    # последняя созданная карточка в Ленте заказов
    LAST_ORDER = (By.XPATH, "//li[contains (@class, 'OrderHistory_listItem')]")
    # заголовок "Состав" во всплывающем окне с информацией о заказе
    ORDER_POPUP_WINDOW_COMPOSITION = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']")
    # счетчик заказов, выполненных за все время
    ALL_COMPLETED_ORDERS = (By.XPATH, "//P[@class='text text_type_main-medium'][text()='Выполнено за все время:']/following-sibling::P")
    # счетчик заказов, выполненных за сегодня
    TODAY_COMPLETED_ORDERS = (By.XPATH, "//P[@class='text text_type_main-medium'][text()='Выполнено за сегодня:']/following-sibling::P")
    # номер заказа в секции "В работе"
    ORDER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class,'orderListReady')]/li[1]")
    # надпись "Все текущие заказы готовы!"
    DEFAULT_IN_PROGRESS = (By.XPATH, "//li[text()='Все текущие заказы готовы!']")
    # номера заказов
    ORDER_NUMBER_IN_LIST = (By.XPATH, "//p[text()='{}']")
