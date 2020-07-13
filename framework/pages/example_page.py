#!/usr/bin/env python
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from framework.base.base_page import BasePage, GenericLocators


class ExamplePageLocators(object):

    EXAMPLE_PAGE_LOCATOR = (By.CSS_SELECTOR, ".lst")


class ExamplePage(BasePage):

    def __init__(self, driver):
        super(ExamplePage, self).__init__(driver)
        self.driver = driver
        self.generic_locators = GenericLocators
        self.example_page_locators = ExamplePageLocators

    def is_google_search_field_visible(self):
        self.wait_for_element_to_appear(*self.example_page_locators.EXAMPLE_PAGE_LOCATOR)
        visible = self.is_element_visible(*self.example_page_locators.EXAMPLE_PAGE_LOCATOR)
        return visible

    def enter_keyword_in_search_field(self, keyword):
        self.find(*self.example_page_locators.EXAMPLE_PAGE_LOCATOR).send_keys(keyword)
        self.find(*self.example_page_locators.EXAMPLE_PAGE_LOCATOR).send_keys(Keys.ENTER)

