from .base_page import BasePage
from .locators import ProductPageLocators
import time
import math
from selenium.common.exceptions import NoAlertPresentException

def solve_quiz_and_get_code(self):
    alert = self.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")

class ProductPage(BasePage):
    def should_be_add_product_to_basket(self):
        self.should_be_click_button()
        self.solve_quiz_and_get_code()
        self.should_be_show_add_text()
        self.should_be_right_price()

    def should_be_click_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "add_button is not presented"
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()
    
    def should_be_show_add_text(self):
        assert self.is_element_present(*ProductPageLocators.TEXT_PRODUCT_ADDED), "text_added is not presented"
        text_added = self.browser.find_element(*ProductPageLocators.TEXT_PRODUCT_ADDED)
        assert "был добавлен в вашу корзину" in text_added.text, "product is not in basket"
    
    def should_be_right_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), "price is not presented"
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), "basket_price is not presented"
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert price == basket_price, f"product {price} is not equal {basket_price}"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
