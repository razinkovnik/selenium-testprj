from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")
    SHOW_BASKET_LINK = (By.CSS_SELECTOR, "header.header span>a.btn-default")
    USER_ICON = (By.CLASS_NAME, "icon-user")

class LoginPageLocators:
    LOGIN_USERNAME = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators:
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_ADDED_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_page h1")
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    BASKET_EMPTY_MESSAGE = (By.ID, "content_inner")
