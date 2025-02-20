from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, './/label[text()="Email"]/parent::div/input') # поле ввода e-mail
    PASSWORD_INPUT = (By.NAME, 'Пароль') # поле ввода пароль
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]') # кнопка входа
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']") # гиперссылка "Зарегистрироваться"
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']") # гиперссылка "Восстановить пароль"
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']") # Заголовок формы входа "Вход"

class RegisterPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']") # гиперссылка "Войти"
    NAME_INPUT = (By.XPATH, './/label[text()="Имя"]/parent::div/input') # поле ввода имени
    EMAIL_INPUT = (By.XPATH, './/label[text()="Email"]/parent::div/input') # поле ввода e-mail
    PASSWORD_INPUT = (By.NAME, 'Пароль') # поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]') # кнопка "Зарегистрироваться"
    INCORRECT_PASSWORD_ERROR = (By.XPATH, '//p[@class="input__error text_type_main-default" and text()="Некорректный пароль"]') # Ошибка при некорректном пароле

class MainPageLocators: #Конструктор
    PERSONAL_ACCOUNT_LINK = (By.LINK_TEXT, 'Личный Кабинет') # Кнопка "Личный кабинет"
    LOG_IN_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']") # Кнопка входа с главной
    ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]') # Кнопка "оформить заказ"
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']") # кнопка для перехода к разделу "Соусы"
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']") # кнопка для перехода к разделу "Булочки"
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']") # кнопка для перехода к разделу "Начинки"
    FILLINGS_HEADER = ((By.XPATH, "//h2[text()='Начинки']")) # Заголовок "Начинки"
    ACTIVE_BUNS = (By.XPATH, "//span[text()='Булки']/parent::div") # активное состояние кнопки "Булочки"
    ACTIVE_SAUCES = (By.XPATH, "//span[text()='Соусы']/parent::div") # активное состояние кнопки "Соусы"
    ACTIVE_FILLINGS = (By.XPATH, "//span[text()='Начинки']/parent::div") # активное состояние кнопки "Соусы"

class ProfilePageLocators:
    ORDER_HISTORY_LINK = (By.LINK_TEXT, 'История заказов') # личный кабинет "История заказов"
    CONSTRUCTOR_LINK = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Конструктор"]') # Гиперссылка "Конструктор"
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # Логотип "Stellar Burgers"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") # личный кабинет кнопка выхода

class PasswordRestorePage:
    LOGIN_LINK = (By.CSS_SELECTOR, "a.Auth_link__1fOlj") # Ссылка "Войти" на странице восстановления пароля
