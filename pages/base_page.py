import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    @allure.step('Открыть страницу')
    def base_open_url(self, URL):
        self.driver.get(URL)


    @allure.step('Получить текущий URL')
    def base_get_current_url(self):
        return self.driver.current_url


    @allure.step('Проверить отображение элемента')
    def base_check_display_of_element(self, LOCATOR):
        return self.driver.find_element(*LOCATOR).is_displayed()


    @allure.step('Дождаться загрузки элемента')
    def base_wait_visibility_of_element_located(self, LOCATOR, timeout = 5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(LOCATOR))


    @allure.step('Дождаться доступности элемента для клика')
    def base_wait_until_element_is_clickable(self, LOCATOR, timeout = 5):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(LOCATOR))


    @allure.step('Клик по выбранному элементу')
    def base_click_to_element(self, LOCATOR):
        self.base_wait_until_element_is_clickable(LOCATOR)
        self.driver.find_element(*LOCATOR).click()


    @allure.step('Проскроллить страницу до выбранного элемента')
    def base_scroll_to_element(self, LOCATOR):
        scroll_to_element = self.driver.find_element(*LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_to_element)


    @allure.step('Получить текст элемента')
    def base_get_text_of_element(self, LOCATOR):
        self.base_wait_visibility_of_element_located(LOCATOR)
        return self.driver.find_element(*LOCATOR).text


    @allure.step('Ввести значение в поле ввода')
    def base_input_text_to_field(self, LOCATOR, text):
        self.driver.find_element(*LOCATOR).send_keys(text)


    @allure.step('Принять cookies')
    def base_to_accept_cookies(self):
        self.base_click_to_element(MainPageLocators.BUTTON_COOKIE)


    @allure.step('Переключиться на новую вкладку')
    def base_switch_to_new_tab(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])


    @allure.step('Дождаться открытия заданной страницы')
    def base_wait_for_open_page(self, page_url):
        return WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(page_url))

