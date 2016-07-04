__author__ = 'jayson_rodrigues'

from selenium.webdriver.common.by import By
import time

class Login(object):
    _email_field_locator = (By.ID, "Email")
    _password_field_locator = (By.ID, "Passwd")
    _submit_button_locator = (By.ID, "signIn")
    _next_button_locator = (By.ID, "next")


    def login(self, driver):
        driver.find_element(*self._email_field_locator).send_keys("roystontestuser3@gmail.com")
        driver.find_element(*self._next_button_locator).click()
        time.sleep(3)
        driver.find_element(*self._password_field_locator).send_keys("rash0207")
        driver.find_element(*self._submit_button_locator).click()