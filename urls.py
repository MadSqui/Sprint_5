class BaseUrls:
    BASE_URL = "https://stellarburgers.nomoreparties.site"

class PageUrls(BaseUrls):
    MAIN_PAGE = f"{BaseUrls.BASE_URL}"
    LOGIN_PAGE = f"{BaseUrls.BASE_URL}/login"
    REGISTRATION_PAGE = f"{BaseUrls.BASE_URL}/register"
    PERSONAL_ACCOUNT_PAGE = f"{BaseUrls.BASE_URL}/account"