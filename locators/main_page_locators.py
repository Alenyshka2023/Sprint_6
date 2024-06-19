from selenium.webdriver.common.by import By


class MainPageLocators:
    # заголовок "Самокат на пару дней"
    TITLE_MAIN_PAGE = [By.XPATH, "//div[contains(@class, 'Home_Header')]"]
    # лого "Яндекс"
    LOGO_YANDEX = By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]"
    # лого "Самокат"
    LOGO_SCOOTER = By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]"
    # кнопка Принять куки "да все привыкли"
    BUTTON_COOKIE = By.ID, "rcc-confirm-button"
    # кнопка "Заказать" на хедере страницы
    BUTTON_ORDER_ON_HEADER = By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"
    # кнопка Заказать в центре страницы
    BUTTON_ORDER_ON_CENTER = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"



class QuestionsMainPageLocators:
    # заголовок блока "Вопросы о важном"
    SECTION_QUESTIONS_ABOUT_IMPORTANT = By.XPATH, "//div[text()='Вопросы о важном']"
    # вопрос - ответ
    BUTTON_QUESTION_1 = (By.XPATH, "//div[@id = 'accordion__heading-0']")
    BUTTON_RESPONSE_1 = By.XPATH, '//div[@id="accordion__panel-0"]/p'
    BUTTON_QUESTION_2 = By.XPATH, "//div[@id = 'accordion__heading-1']"
    BUTTON_RESPONSE_2 = By.XPATH, '//div[@id="accordion__panel-1"]/p'
    BUTTON_QUESTION_3 = By.XPATH, "//div[@id = 'accordion__heading-2']"
    BUTTON_RESPONSE_3 = By.XPATH, '//div[@id="accordion__panel-2"]/p'
    BUTTON_QUESTION_4 = By.XPATH, "//div[@id = 'accordion__heading-3']"
    BUTTON_RESPONSE_4 = By.XPATH, '//div[@id="accordion__panel-3"]/p'
    BUTTON_QUESTION_5 = By.XPATH, "//div[@id = 'accordion__heading-4']"
    BUTTON_RESPONSE_5 = By.XPATH, '//div[@id="accordion__panel-4"]/p'
    BUTTON_QUESTION_6 = By.XPATH, "//div[@id = 'accordion__heading-5']"
    BUTTON_RESPONSE_6 = By.XPATH, '//div[@id="accordion__panel-5"]/p'
    BUTTON_QUESTION_7 = By.XPATH, "//div[@id = 'accordion__heading-6']"
    BUTTON_RESPONSE_7 = By.XPATH, '//div[@id="accordion__panel-6"]/p'
    BUTTON_QUESTION_8 = By.XPATH, "//div[@id = 'accordion__heading-7']"
    BUTTON_RESPONSE_8 = By.XPATH, '//div[@id="accordion__panel-7"]/p'
