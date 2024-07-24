from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    # заголовок формы восстановления пароля
    PASSWORD_RECOVERY_LABEL = (By.XPATH, "//h2[text()='Восстановление пароля']")
    # поле ввода значения email  в форме восстановления пароля
    RECOVERY_EMAIL_INPUT = (By.CSS_SELECTOR, 'input.text')
    # кнопка "Восстановить"
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    # поле ввода значения password в форме восстановления пароля
    RECOVERY_PWD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    # кнопка показать/скрыть пароль в форме обновления пароля
    SHOW_HIDE_BUTTON = (By.CSS_SELECTOR, '.input__icon')
    # поле ввода значения password в форме восстановления пароля в активном состоянии
    ACTIVE_RECOVERY_PWD_INPUT = (By.CSS_SELECTOR, 'div.input_status_active')

