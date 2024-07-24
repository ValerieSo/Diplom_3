from selenium.webdriver.common.by import By


class HomePageLocators:
    # кнопка "Конструктор"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    # кнопка "Лента Заказов"
    BUTTON_ORDER_LIST = (By.XPATH, "//p[text()='Лента Заказов']")
    # надпись "Соберите Бургер"
    LABEL_ASSEMBLE_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")
    # надпись "Лента заказов"
    LABEL_ORDER_LIST = (By.XPATH, "//h1[text()='Лента заказов']")
    # карточка ингредиента "Биокотлета из марсианской Магнолии"
    TEST_INGREDIENT = (By.XPATH, "//img[@alt='Биокотлета из марсианской Магнолии']")
    # карточка булочки "Краторная булка N-200i"
    TEST_BUN = (By.XPATH, "//img[@alt='Краторная булка N-200i']")
    # заголовок высплывающего окна карточки ингредиента
    INGREDIENT_POPUP_WINDOW_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    # название ингредиента во всплывающем окне информации об ингредиенте
    INGREDIENT_POPUP_WINDOW_INGR_NAME = (By.XPATH, "//div[contains(@class,'Modal_modal__contentBox')]/p[text()='Биокотлета из марсианской Магнолии']")
    # кнопка "Закрыть"(крестик) во всплывающем окне информации об ингредиенте
    CLOSE_POPUP_WINDOW_BUTTON = (By.XPATH, "//button[contains(@class, 'close')]")
    # область формирования бургера
    BURGER_TARGET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")
    # область для прикрепления булочки
    BUN_TARGET = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (верх)']")
    # счетчик ингредиента
    INGREDIENT_COUNTER = (By.XPATH, "//img[@alt='Биокотлета из марсианской Магнолии']/preceding-sibling::div/p[contains(@class, 'num')]")
    # кнопка "Оформить"  на главной странице
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    # номер заказа
    ORDER_NUMBER = (By.XPATH, "//h2[contains (@class, 'modal__title_shadow')]")
    # дефолтный номер заказа
    DAFAULT_ORDER_NUMBER = (By.XPATH, "//h2[text()='9999']")
    # кнопка "Личный кабинет"
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")

