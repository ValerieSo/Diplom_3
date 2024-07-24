from selenium.webdriver.common.by import By


class LoginPageLocators:
    # поле ввода "Email" на странице авторизации
    LOGIN_INPUT_EMAIL = (By.XPATH, "//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    # поле ввода "Пароль" на странице авторизации
    LOGIN_INPUT_PWD = (By.XPATH, "//input[@type = 'password']")
    # кнопка "Войти" на странице авторизации
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")
    # кнопка "Восстановить пароль"
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")
