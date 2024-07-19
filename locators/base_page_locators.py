from selenium.webdriver.common.by import By

class BasePageLocators:
    # окно загрузки
    MODAL_OVERLAY = (By.XPATH, "//img[@alt='loading animation']")
