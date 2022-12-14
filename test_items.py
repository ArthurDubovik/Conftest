from pydantic import NoneIsAllowedError
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_search(browser):
    browser.get(link)
    #time.sleep(30)
    browser.implicitly_wait(5)
    try:
        cart_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    except:
        cart_button = None
    assert cart_button != None, 'Button Add_to_basket not found'
    