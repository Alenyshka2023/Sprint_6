import pytest
import allure
from pages.base_page import BasePage
from pages.order_page import OrderPage
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from data import TestDataSetOrder
from conftest import driver


class TestOrderPageScooter:

    @allure.title('Проверка оформления заказа через кнопки "Заказать"')
    @allure.description('Проверить, что заказ успешно оформляется через 2 кнопки "Заказать" на главной странице')
    @pytest.mark.parametrize('entry_point, order_dataset', [(MainPageLocators.BUTTON_ORDER_ON_CENTER, TestDataSetOrder.order_dataset_const_1),
                                                        (MainPageLocators.BUTTON_ORDER_ON_HEADER, TestDataSetOrder.order_dataset_const_2)
                                                            ])
    def test_create_order_success(self, driver, entry_point, order_dataset):
        test_order_page = OrderPage(driver)
        test_order_page.base_to_accept_cookies()
        test_order_page.base_scroll_to_element(entry_point)
        test_order_page.base_click_to_element(entry_point)
        test_order_page.set_data_about_user(order_dataset)
        test_order_page.set_data_about_rental_period(order_dataset)
        test_order_page.set_confirm_order()
        test_result_text = test_order_page.check_order_has_been_placed()
        test_status_view = test_order_page.check_button_status_view_availability()
        assert "Заказ оформлен" in test_result_text and test_status_view == True
