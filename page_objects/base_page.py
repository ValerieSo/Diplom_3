from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from locators.base_page_locators import BasePageLocators
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_clickable_element(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def should_be_visible(self, locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return element.is_displayed()

    def should_not_be_visible(self, locator):
        return WebDriverWait(self.driver, 10).until_not(expected_conditions.visibility_of_element_located(locator))

    def click_button(self, locator):
        button = self.find_clickable_element(locator)
        button.click()

    def drag_an_element(self, element, target):
        actions = ActionChains(self.driver)
        actions.click_and_hold(element).move_to_element(target).release().perform()

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def get_text_from_element(self, locator):
        return self.wait_and_find_element(locator).text

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def become_invisible(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element_located(locator))

    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Ожидание закрытия модального окна загрузки")
    def finish_modal_loading(self):
        self.should_not_be_visible(BasePageLocators.MODAL_OVERLAY)

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    def get_attribute_of_element(self, locator, attribute):
        element = self.wait_and_find_element(locator)
        value = element.get_attribute(attribute)
        return value
