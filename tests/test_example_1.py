#!/usr/bin/env python
from framework.base.base_tc import BaseTestCase
from framework.pages.example_page import ExamplePage
import time


class TestExample01(BaseTestCase):

    def setUp(self):
        super(TestExample01, self).setUp()

    def test_example_1(self):
        driver = self.driver
        search = ExamplePage(driver)
        time.sleep(3)
        search.enter_keyword_in_search_field("Python")
        time.sleep(3)

        assert "Python" in driver.page_source, "The 'Python' keyword is not visible on the page!"

    def tearDown(self):
        super(TestExample01, self).tearDown()
