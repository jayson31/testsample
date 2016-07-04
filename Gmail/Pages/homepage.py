__author__ = 'jayson_rodrigues'
from selenium.webdriver.common.by import By


class Homepage(object):
    _create_account_link = (By.XPATH, "//span[@id='link-signup']/a")

    def click_on_create_account(self, driver):
        driver.find_element(*self._create_account_link).click()