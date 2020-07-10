#!/usr/bin/env python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException, \
    StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from subprocess import call
from selenium.webdriver.common.keys import Keys
import datetime
import time


class GenericLocators(object):
    """
        Container for locators that appear on all pages/dialogs/sections in order to be properly grouped.
        All locators that are used on more than one page should be added to generic page locators and properly
        verified and after that updated on any modifications.
    """
    

class BasePage(object):
    """
        Container for base functions and methods to carry over page objects but stored on a single place
    """

    def __init__(self, driver):
        self.driver = driver
        self.generic_locators = GenericLocators

    """
        Global waits
    """

    def wait_for_element_to_appear(self, by, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, locator)))
        self.wait_for(1.5)

    def wait_for_element_to_become_invisible(self, by, locator):
        WebDriverWait(self.driver, 100).until(EC.invisibility_of_element_located((by, locator)))

    def wait_for_element_to_appear_for_specific_time(self, time2wait, by, locator):
        WebDriverWait(self.driver, time2wait).until(EC.visibility_of_element_located((by, locator)))

    def wait_for_element_to_be_clickable(self, by, locator):
        WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((by, locator)))

    def wait_for_element_to_disappear(self, by, locator):
        for x in range(0, 100):
            try:
                visible = self.is_element_visible(by=by, locator=locator)
                if visible:
                    self.wait_for(1)
                elif not visible or visible is None:
                    break
                elif x == 99:
                    raise "Element didn't disappear in given time (100 sec): " + by + " = " + locator
            except NoSuchElementException:
                break
            except StaleElementReferenceException:
                break

    def wait_for_element_to_disappear_for_specific_time(self, time_to_wait,  by, locator):
        for x in range(0, time_to_wait):
            try:
                visible = self.is_element_visible(by=by, locator=locator)
                if visible:
                    self.wait_for(1)
                elif not visible or visible is None:
                    break
                elif x == time_to_wait - 1:
                    raise "Element didn't disappear in given time (100 sec): " + by + " = " + locator
            except NoSuchElementException:
                break
            except StaleElementReferenceException:
                break

    def wait_specific_time_and_verify_element_presence(self, time_to_wait, by, locator):
        try:
            self.wait_for_element_to_appear_for_specific_time(time_to_wait, by, locator)
        except TimeoutException:
            visible = self.is_element_visible(by, locator)
            return visible
        except WebDriverException:
            visible = self.is_element_visible(by, locator)
            return visible

    """
        Element visibility and presence checkers
    """

    def is_element_visible(self, by, locator):
        try:
            element = self.find(by=by, locator=locator)
            try:
                ok = element.is_displayed()
            except StaleElementReferenceException:
                self.wait_for(3)
                try:
                    ok = element.is_displayed()
                except StaleElementReferenceException:
                    ok = False
                except NoSuchElementException:
                    ok = False
        except NoSuchElementException:
            ok = False
        return ok

    def is_element_present_in_dom(self, by, locator):
        ok = True
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            ok = False
        except WebDriverException:
            ok = False
        return ok

    """
        Locating elements with or without waiting for them to appear on page respectively
    """

    def find(self, by, locator):
        if by == By.CSS_SELECTOR:
            return self.driver.find_element_by_css_selector(css_selector=locator)
        elif by == By.XPATH:
            return self.driver.find_element_by_xpath(xpath=locator)
        elif by == By.ID:
            return self.driver.find_element_by_id(id=locator)

    def finds(self, by, locator):
        if by == By.CSS_SELECTOR:
            return self.driver.find_elements_by_css_selector(css_selector=locator)
        elif by == By.XPATH:
            return self.driver.find_elements_by_xpath(xpath=locator)

    def wait_for_element(self, by, locator):
        self.wait_for_element_to_appear(by=by, locator=locator)
        if by == By.CSS_SELECTOR:
            return self.driver.find_element_by_css_selector(css_selector=locator)
        elif by == By.XPATH:
            return self.driver.find_element_by_xpath(xpath=locator)

    def wait_for_elements(self, by, locator):
        self.wait_for_element_to_appear(by=by, locator=locator)
        try:
            if by == By.CSS_SELECTOR:
                return self.driver.find_elements_by_css_selector(css_selector=locator)
            elif by == By.XPATH:
                return self.driver.find_elements_by_xpath(xpath=locator)
        except StaleElementReferenceException:
            self.wait_for(2)
            return self.finds(by=by, locator=locator)

    """
        Interaction with page elements
    """

    def clear_text(self, *locator):
        element = self.wait_for_element(*locator)
        element.clear()

    def fill_input(self, text, *locator):
        element = self.wait_for_element(*locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def fill_input_and_press_enter(self, text, *locator):
        element = self.wait_for_element(*locator)
        element.click()
        element.clear()
        element.send_keys(text)
        self.press_enter(*locator)

    def press_enter(self, *locator):
        element = self.wait_for_element(*locator)
        element.send_keys(Keys.ENTER)

    def click_on_element(self, *locator):
        try:
            element = self.find(*locator)
            element.click()
        except WebDriverException:
            self.wait_for(2)
            element = self.wait_for_element(*locator)
            actions = ActionChains(self.driver)
            actions.move_to_element(to_element=element)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()

    def hover_over(self, *locator):
        element = self.wait_for_element(*locator)
        ActionChains(self.driver).move_to_element(to_element=element).perform()

    def wait_for(self, time_to_wait):
        time.sleep(time_to_wait)

    def switch_to_frame(self, *locator):
        self.wait_for_element_to_appear(*locator)
        self.driver.switch_to.frame(self.find(*locator))

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def go_back_to_previous_page(self):
        self.driver.back()
        self.wait_for_page_load()
        self.wait_for(time_to_wait=3)
