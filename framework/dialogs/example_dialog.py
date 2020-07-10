#!/usr/bin/env python
from selenium.webdriver.common.by import By
from framework.base.base_page import GenericLocators
from framework.base.base_dialog import BaseDialog, BaseDialogLocators


class SomeDialogLocators(object):

    SOME_FIELD = (By.XPATH, "The xpath")


class SomeDialog(BaseDialog):

    def __init__(self, driver):
        super(SomeDialog, self).__init__(driver)
        self.driver = driver
        self.generic_locators = GenericLocators
        self.base_dialog_locators = BaseDialogLocators
        self.some_dialog_locators = SomeDialogLocators




