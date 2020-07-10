#!/usr/bin/env python
from selenium.webdriver.common.by import By

from framework.base.base_page import BasePage, GenericLocators


class SomePageLocators(object):

    SOME_PAGE_LOCATOR = (By.XPATH, "here put xpath")


class SomePage(BasePage):

    def __init__(self, driver):
        super(SomePage, self).__init__(driver)
        self.driver = driver
        self.generic_locators = GenericLocators
        self.article_locators = SomePageLocators
