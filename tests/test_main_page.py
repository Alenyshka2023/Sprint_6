import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import TestUrls
from conftest import driver


class TestMainPage:

    @allure.title('Проверка перехода на главную страницу "Яндекс Самокат" по клику на лого "Самокат"')
    @allure.description('Проверить, что клик на лого "Самокат" осуществляет переход на главную страницу Яндекс Самоката')
    def test_click_logo_scooter_direct_main_page(self, driver):
        test_order_page = OrderPage(driver)
        test_main_page = MainPage(driver)
        test_order_page.open_order_page_scooter()
        test_order_page.click_on_logo_scooter_in_header()
        test_main_page.main_wait_for_load_page_title()
        test_expected_url = TestUrls.SCOOTER_MAIN_PAGE
        test_actual_url = test_main_page.base_get_current_url()
        assert test_actual_url == test_expected_url

    @allure.title('Проверка перехода на главную страницу "Дзен" по клику на лого "Яндекс"')
    @allure.description('Проверить, что клик на лого "Яндекс" открывает новое окно с главной страницей "Дзен"')
    def test_click_logo_yandex_open_main_page_dzen(self, driver):
        test_main_page = MainPage(driver)
        test_main_page.base_open_url(TestUrls.SCOOTER_MAIN_PAGE)
        test_main_page.click_on_logo_yandex_in_header()
        test_main_page.base_switch_to_new_tab()
        test_main_page.base_wait_for_open_page(TestUrls.DZEN_MAIN_PAGE)
        test_expected_url = TestUrls.DZEN_MAIN_PAGE
        test_actual_url = test_main_page.base_get_current_url()
        assert test_actual_url == test_expected_url
