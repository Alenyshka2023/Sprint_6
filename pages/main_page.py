import allure
from conftest import driver
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators, QuestionsMainPageLocators


class MainPage(BasePage):

    @allure.step('Инициализация работы в браузере')
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Дождаться загрузки заголовка "Самокат на пару дней" на главной странице')
    def main_wait_for_load_page_title(self):
        self.base_wait_visibility_of_element_located(MainPageLocators.TITLE_MAIN_PAGE)


    @allure.step('Клик на лого "Яндекс"')
    def click_on_logo_yandex_in_header(self):
        self.base_click_to_element(MainPageLocators.LOGO_YANDEX)


    @allure.step('Клик на кнопку "Заказать" на хедере страницы')
    def main_click_button_order_top(self):
        self.base_click_to_element(MainPageLocators.BUTTON_ORDER_ON_HEADER)


    @allure.step('Клик на кнопку "Заказать" в центре страницы')
    def main_click_button_order_page(self):
        self.base_click_to_element(MainPageLocators.BUTTON_ORDER_ON_CENTER)


class MainPageFAQSection(BasePage):

    @allure.step('Инициализация работы в браузере')
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Скролл страницы до блока "Вопросы о важном"')
    def faq_scroll_to_questions_answers(self):
        self.base_scroll_to_element(QuestionsMainPageLocators.SECTION_QUESTIONS_ABOUT_IMPORTANT)


    @allure.step('Клик на вопрос 1')
    def faq_click_question_id_0(self):
        self.base_click_to_element(QuestionsMainPageLocators.BUTTON_QUESTION_1)


    @allure.step('Получить текст вопроса 1')
    def get_text_question_for_faq_0(self):
        return self.base_get_text_of_element(QuestionsMainPageLocators.BUTTON_QUESTION_1)


    @allure.step('Получить текст ответа на вопрос 1')
    def get_text_answer_for_faq_0(self):
        return self.base_get_text_of_element(QuestionsMainPageLocators.BUTTON_RESPONSE_1)


    @allure.step('Клик на вопрос 2')
    def faq_click_question_id_1(self):
        self.base_click_to_element(QuestionsMainPageLocators.BUTTON_QUESTION_2)


    @allure.step('Получить текст вопроса 2')
    def get_text_question_for_faq_1(self):
        return self.base_get_text_of_element(QuestionsMainPageLocators.BUTTON_QUESTION_2)


    @allure.step('Получить текст ответа на вопрос 2')
    def get_text_answer_for_faq_1(self):
        return self.base_get_text_of_element(QuestionsMainPageLocators.BUTTON_RESPONSE_2)


    @allure.step('Клик на вопрос 3')
    def faq_click_question_id_2(self):
        self.base_click_to_element(QuestionsMainPageLocators.BUTTON_QUESTION_3)


    @allure.step('Получить текст вопроса 3')
    def get_text_question_for_faq_2(self):
        return self.base_get_text_of_element(QuestionsMainPageLocators.BUTTON_QUESTION_3)


    @allure.step('Получить текст ответа на вопрос 3')
    def get_text_answer_for_faq_2(self):
        return self.base_get_text_of_element(QuestionsMainPageLocators.BUTTON_RESPONSE_3)


    @allure.step('Клик на вопрос 4')
    def faq_click_question_id_3(self):
        self.base_click_to_element(QuestionsMainPageLocators.BUTTON_QUESTION_4)


    @allure.step('Получить текст вопроса 4')
    def get_text_question_for_faq_3(self):
        return self.base_get_text_of_element(QuestionsMainPageLocators.BUTTON_QUESTION_4)


    @allure.step('Получить текст ответа на вопрос 4')
    def get_text_answer_for_faq_3(self):
        return self.base_get_text_of_element(QuestionsMainPageLocators.BUTTON_RESPONSE_4)


    @allure.step('Клик на вопрос 5')
    def faq_click_question_id_4(self):
        self.base_click_to_element(QuestionsMainPageLocators.BUTTON_QUESTION_5)


    @allure.step('Получить текст вопроса 5')
    def get_text_question_for_faq_4(self):
        return self.base_get_text_of_element(QuestionsMainPageLocators.BUTTON_QUESTION_5)


    @allure.step('Получить текст ответа на вопрос 5')
    def get_text_answer_for_faq_4(self):
        return self.base_get_text_of_element(QuestionsMainPageLocators.BUTTON_RESPONSE_5)


    @allure.step('Клик на вопрос 6')
    def faq_click_question_id_5(self):
        self.base_click_to_element(QuestionsMainPageLocators.BUTTON_QUESTION_6)


    @allure.step('Получить текст вопроса 6')
    def get_text_question_for_faq_5(self):
        return self.base_get_text_of_element(QuestionsMainPageLocators.BUTTON_QUESTION_6)


    @allure.step('Получить текст ответа на вопрос 6')
    def get_text_answer_for_faq_5(self):
        return self.base_get_text_of_element(QuestionsMainPageLocators.BUTTON_RESPONSE_6)


    @allure.step('Клик на вопрос 7')
    def faq_click_question_id_6(self):
        self.base_click_to_element(QuestionsMainPageLocators.BUTTON_QUESTION_7)


    @allure.step('Получить текст вопроса 7')
    def get_text_question_for_faq_6(self):
        return self.base_get_text_of_element(QuestionsMainPageLocators.BUTTON_QUESTION_7)


    @allure.step('Получить текст ответа на вопрос 7')
    def get_text_answer_for_faq_6(self):
        return self.base_get_text_of_element(QuestionsMainPageLocators.BUTTON_RESPONSE_7)


    @allure.step('Клик на вопрос 8')
    def faq_click_question_id_7(self):
        self.base_click_to_element(QuestionsMainPageLocators.BUTTON_QUESTION_8)


    @allure.step('Получить текст вопроса 8')
    def get_text_question_for_faq_7(self):
        return self.base_get_text_of_element(QuestionsMainPageLocators.BUTTON_QUESTION_8)


    @allure.step('Получить текст ответа на вопрос 8')
    def get_text_answer_for_faq_7(self):
        return self.base_get_text_of_element(QuestionsMainPageLocators.BUTTON_RESPONSE_8)

