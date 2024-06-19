from selenium.webdriver.common.by import By


class OrderPageLocators:

    # Форма "Для кого самокат"
    # поле ввода "Имя"
    INPUT_NAME = By.XPATH, "//input[@placeholder='* Имя']"
    # поле ввода "Фамилия"
    INPUT_SURNAME = By.XPATH, "//input[@placeholder='* Фамилия']"
    # поле ввода "Адрес: куда привезти заказ"
    INPUT_ADDRESS = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    # поле ввода "Станция метро"
    INPUT_METRO = By.CSS_SELECTOR, "input[placeholder='* Станция метро']"
    # список "Станция метро"
    LIST_METRO = (By.XPATH, ".//li[@class='select-search__row']")
    # поле ввода "Телефон: на него позвонит курьер"
    INPUT_PHONE = By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"
    # кнопка "Далее"
    BUTTON_NEXT = By.XPATH, "//button[text()='Далее']"

    # Форма_2. "Про аренду"
    # поле ввода "Когда привезти самокат"
    INPUT_DATE = By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']"
    # окно выбора даты - текущая дата
    CHOOSE_DATE_TODAY = By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]"
    # окно выбора даты - 21.06
    CHOOSE_DATE_ANY = By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--026']"
    # поле "Срок аренды"
    INPUT_PERIOD_RENT = By.XPATH, "//div[text()='* Срок аренды']"
    # окно выбора срока аренды - сутки
    CHOOSE_PERIOD_RENT_DAY = By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']"
    # окно выбора срока аренды - трое суток
    CHOOSE_PERIOD_RENT_3_DAY = By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']"
    # выбор цвета "чёрный жемчуг"
    CHECKBOX_COLOR_BLACK = By.ID, "black"
    # выбор цвета "серая безысходность"
    CHECKBOX_COLOR_GREY = By.ID, "grey"
    # поле ввода "Комментарий для курьера"
    INPUT_COMMENT = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    # кнопка "Заказать"
    BUTTON_ORDER = By.XPATH, '//*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]'
    # кнопка подтверждения заказа "Да"
    BUTTON_CONFIRM_ORDER = By.XPATH, "//button[text()='Да']"

    # окно с информацией об успешном оформлении заказа
    INFORMATION_SUCCESS_ORDER = By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']"
    # кнопка "Посмотреть статус"
    BUTTON_STATUS_ORDER = By.XPATH, "//button[contains(@class,'Button_Button_') and text()='Посмотреть статус']"
