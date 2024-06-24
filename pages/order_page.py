import random
import allure
from random import choice
from conftest import driver
from pages.base_page import BasePage
from data import TestUrls
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Открыть страницу заказа')
    def open_order_page_scooter(self):
        self.base_open_url(TestUrls.SCOOTER_ORDER_PAGE)



    @allure.step('Ввод имени')
    def set_name_user_in_order(self, name):
        self.base_wait_visibility_of_element_located(OrderPageLocators.INPUT_NAME)
        self.base_click_to_element(OrderPageLocators.INPUT_NAME)
        return self.base_input_text_to_field(OrderPageLocators.INPUT_NAME, name)


    @allure.step('Ввод фамилии')
    def set_last_name_user_in_order(self, last_name):
        self.base_click_to_element(OrderPageLocators.INPUT_SURNAME)
        return self.base_input_text_to_field(OrderPageLocators.INPUT_SURNAME, last_name)


    @allure.step('Ввод адреса')
    def set_address_in_order(self, address):
        self.base_click_to_element(OrderPageLocators.INPUT_ADDRESS)
        return self.base_input_text_to_field(OrderPageLocators.INPUT_ADDRESS, address)


    @allure.step('Выбор станции метро')
    def set_metro_station_in_order(self, metro):
        self.base_click_to_element(OrderPageLocators.INPUT_METRO)
        self.base_input_text_to_field(OrderPageLocators.INPUT_METRO, metro)
        return self.base_click_to_element(OrderPageLocators.LIST_METRO)


    @allure.step('Ввод телефона')
    def set_phone_number_in_order(self, phone):
        self.base_click_to_element(OrderPageLocators.INPUT_PHONE)
        return self.base_input_text_to_field(OrderPageLocators.INPUT_PHONE, phone)


    @allure.step('Клик по кнопке Далее')
    def set_continue_order(self):
        return self.base_click_to_element(OrderPageLocators.BUTTON_NEXT)


    @allure.step('Выбор даты доставки')
    def set_date_start_rent(self):
        date_choise = random.choice([OrderPageLocators.CHOOSE_DATE_TODAY, OrderPageLocators.CHOOSE_DATE_ANY])
        self.base_click_to_element(OrderPageLocators.INPUT_DATE)
        self.base_click_to_element(date_choise)


    @allure.step('Выбор срока аренды')
    def set_rent_time_in_order(self):
        time_choise = random.choice(
            [OrderPageLocators.CHOOSE_PERIOD_RENT_DAY, OrderPageLocators.CHOOSE_PERIOD_RENT_3_DAY])
        self.base_click_to_element(OrderPageLocators.INPUT_PERIOD_RENT)
        self.base_click_to_element(time_choise)


    @allure.step('Выбор цвета самоката')
    def set_color_scooter_in_order(self):
        color_choise = random.choice(
            [OrderPageLocators.CHECKBOX_COLOR_BLACK, OrderPageLocators.CHECKBOX_COLOR_GREY])
        self.base_click_to_element(color_choise)


    @allure.step('Ввод комментария к заказу')
    def set_comment_in_order(self, comment = " "):
        self.base_click_to_element(OrderPageLocators.INPUT_COMMENT)
        return self.base_input_text_to_field(OrderPageLocators.INPUT_COMMENT, comment)


    @allure.step('Завершение заказа')
    def set_complete_order(self):
        self.base_click_to_element(OrderPageLocators.BUTTON_ORDER)


    @allure.step('Заполнение данных о пользователе')
    def set_data_about_user(self, order_dataset):
        self.set_name_user_in_order(order_dataset[0])
        self.set_last_name_user_in_order(order_dataset[1])
        self.set_address_in_order(order_dataset[2])
        self.set_metro_station_in_order(order_dataset[3])
        self.set_phone_number_in_order(order_dataset[4])
        self.set_continue_order()


    @allure.step('Заполнение данных о сроке аренды')
    def set_data_about_rental_period(self, order_dataset):
        self.set_date_start_rent()
        self.set_rent_time_in_order()
        self.set_color_scooter_in_order()
        self.set_comment_in_order(order_dataset[5])
        self.set_complete_order()


    @allure.step('Подтверждение заказа')
    def set_confirm_order(self):
        self.base_click_to_element(OrderPageLocators.BUTTON_CONFIRM_ORDER)


    @allure.step('Отображение сообщения об оформлении заказа')
    def check_order_has_been_placed(self):
        return self.base_get_text_of_element(OrderPageLocators.INFORMATION_SUCCESS_ORDER)


    @allure.step('Проверка кнопки "Посмотреть статус"')
    def check_button_status_view_availability(self):
        self.base_wait_until_element_is_clickable(OrderPageLocators.BUTTON_STATUS_ORDER)
        return self.base_check_display_of_element(OrderPageLocators.BUTTON_STATUS_ORDER)
