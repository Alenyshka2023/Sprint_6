import pytest
import allure
from pages.base_page import BasePage
from pages.main_page import MainPage, MainPageFAQSection
from locators.main_page_locators import QuestionsMainPageLocators
from data import TestDataFAQ
from conftest import driver


class TestFaqScooterRental:

    @allure.title('Проверка блока "Вопросы о важном" на главной странице')
    @allure.description('Проверить, что клик на каждый вопрос открывает соответствующий ему ответ')
    @pytest.mark.parametrize("test_faq_id, actual_question, actual_answer, expected_question, expected_answer", [
                            (MainPageFAQSection.faq_click_question_id_0,
                                MainPageFAQSection.get_text_question_for_faq_0, MainPageFAQSection.get_text_answer_for_faq_0,
                                    TestDataFAQ.dict_expected_faq[0][0], TestDataFAQ.dict_expected_faq[0][1]),
                            (MainPageFAQSection.faq_click_question_id_1,
                                MainPageFAQSection.get_text_question_for_faq_1, MainPageFAQSection.get_text_answer_for_faq_1,
                                    TestDataFAQ.dict_expected_faq[1][0], TestDataFAQ.dict_expected_faq[1][1]),
                            (MainPageFAQSection.faq_click_question_id_2,
                                MainPageFAQSection.get_text_question_for_faq_2, MainPageFAQSection.get_text_answer_for_faq_2,
                                    TestDataFAQ.dict_expected_faq[2][0], TestDataFAQ.dict_expected_faq[2][1]),
                            (MainPageFAQSection.faq_click_question_id_3,
                                MainPageFAQSection.get_text_question_for_faq_3, MainPageFAQSection.get_text_answer_for_faq_3,
                                    TestDataFAQ.dict_expected_faq[3][0], TestDataFAQ.dict_expected_faq[3][1]),
                            (MainPageFAQSection.faq_click_question_id_4,
                                MainPageFAQSection.get_text_question_for_faq_4, MainPageFAQSection.get_text_answer_for_faq_4,
                                    TestDataFAQ.dict_expected_faq[4][0], TestDataFAQ.dict_expected_faq[4][1]),
                            (MainPageFAQSection.faq_click_question_id_5,
                                MainPageFAQSection.get_text_question_for_faq_5, MainPageFAQSection.get_text_answer_for_faq_5,
                                    TestDataFAQ.dict_expected_faq[5][0], TestDataFAQ.dict_expected_faq[5][1]),
                            (MainPageFAQSection.faq_click_question_id_6,
                                MainPageFAQSection.get_text_question_for_faq_6, MainPageFAQSection.get_text_answer_for_faq_6,
                                    TestDataFAQ.dict_expected_faq[6][0], TestDataFAQ.dict_expected_faq[6][1]),
                            (MainPageFAQSection.faq_click_question_id_7,
                                MainPageFAQSection.get_text_question_for_faq_7, MainPageFAQSection.get_text_answer_for_faq_7,
                                    TestDataFAQ.dict_expected_faq[7][0], TestDataFAQ.dict_expected_faq[7][1])
                            ])
    def test_click_on_questions_to_response(self, driver, test_faq_id, actual_question, actual_answer, expected_question, expected_answer):
        test_page = MainPageFAQSection(driver)
        test_page.base_to_accept_cookies()
        test_page.faq_scroll_to_questions_answers()
        test_faq_id(test_page)
        text_actual_question = actual_question(test_page)
        text_actual_answer = actual_answer(test_page)
        assert text_actual_question == expected_question
        assert text_actual_answer == expected_answer

