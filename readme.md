# Sprint_5: Тестирование сайта **Stellar Burgers** (https://stellarburgers.nomoreparties.site/) 
в браузере **Google Chrome**

## ПО для тестирования
- Python 3.13
- PyTest
- Selenium
- Google Chrome и chromedriver

## Содержание:
директория tests  - содержит тесты
conftest.py - содержит фикстуры
data.py - содержит данные для регистрации
urls.py - содержит url`s
locators.py - cодержит локаторы 

## Проверка функционала (реализованные тесты)

**Регистрация** (test_registration)
 test_successful_registration- успешная регистрация
 test_invalid_password_registration - неуспешная регистрация (пароль менее 6 символов)


**Вход** (test_login)
test_login_from_main_page - по кнопке «Войти в аккаунт» на главной
test_login_from_personal_account_button - через кнопку «Личный кабинет»
test_login_from_registration_form - через кнопку в форме регистрации
test_login_from_password_restore_page - через кнопку в форме восстановления пароля


**Переход в личный кабинет** (test_transition_personal_acc)
test_transition_to_personal_account - клику на «Личный кабинет»


**Выход из аккаунта** (test_logout)
test_logout - по кнопке «Выйти» в личном кабинете


**Переход из личного кабинета в «Конструктор»**
test_transition_to_constructor_from_personal_account_button - по клику на «Конструктор»
def test_transition_to_constructor_from_personal_account_logo - по клику на логотип Stellar Burgers
 
**Переходы к разделам Конструктор бургеров** (test_construction)
test_transition_to_buns_section - «Булки»
test_transition_to_sauces_section -  «Соусы»
test_transition_to_fillings_section - «Начинки»
