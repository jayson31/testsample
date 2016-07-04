__author__ = 'jayson_rodrigues'

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from random import randint
from selenium.webdriver.common.keys import Keys
import time

class Register(object):
    _first_name_field_locator = (By.ID, "FirstName")
    _last_name_field_locator = (By.ID, "LastName")
    _username_field_locator = (By.ID, "GmailAddress")
    _password_field_locator = (By.ID, "Passwd")
    _confirm_password_field_locator = (By.ID, "PasswdAgain")
    _month_dropdown_locator = (By.ID, "BirthMonth")
    _month_locator = (By.ID, ":5")
    _day_field_locator = (By.ID, "BirthDay")
    _year_field_locator = (By.ID, "BirthYear")
    _gender_dropdown_locator = (By.ID, "Gender")
    _gender_selector_locator = (By.ID, ":f")
    _next_button_locator = (By.ID, "submitbutton")
    _popup_locator = (By.CLASS_NAME, "tos-scroll")
    _agree_button_locator = (By.ID, "iagreebutton")

    def generate_username(self):
        random = randint(1, 1000000000)
        return random

    def register(self, driver):
        driver.find_element(*self._first_name_field_locator).send_keys("Test")
        driver.find_element(*self._last_name_field_locator).send_keys("Test")
        random = self.generate_username()
        username = "Test" + str(random)
        driver.find_element(*self._username_field_locator).send_keys(username)
        driver.find_element(*self._password_field_locator).send_keys("QwErTy13579")
        driver.find_element(*self._confirm_password_field_locator).send_keys("QwErTy13579")
        driver.find_element(*self._month_dropdown_locator).click()
        driver.find_element(*self._month_locator).click()
        driver.find_element(*self._day_field_locator).send_keys("01")
        driver.find_element(*self._year_field_locator).send_keys("1989")
        driver.find_element(*self._gender_dropdown_locator).click()
        driver.find_element(*self._gender_selector_locator).click()
        driver.find_element(*self._next_button_locator).click()
        text = driver.find_element(By.XPATH, "//div[@id='tos-text']/div[4]/div").text
        act = ActionChains(driver)
        act.move_to_element(driver.find_element(By.XPATH, "//div[@id='tos-text']/div[5]")).perform()
        driver.find_element(*self._agree_button_locator).click()
