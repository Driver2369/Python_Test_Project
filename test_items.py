from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_should_be_available(browser):

    browser.get(link)
    wait = WebDriverWait(browser, 5)
    add_to_cart_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#add_to_basket_form button')))

    assert add_to_cart_button.is_displayed()

    # for debugging purposes
    time.sleep(5)
