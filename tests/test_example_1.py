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

        # Check that the google page is displayed and the search field is visible
        self.assertTrue(search.is_google_search_field_visible(),
                        "Nor correct page is opened oor the search field is not visible")

        # Enter keyword in the search field and hit enter
        search.enter_keyword_in_search_field("Python")

        # Check that the "Python" keyword is visible on the page
        assert "Python" in driver.page_source, "The 'Python' keyword is not visible on the page!"

    def tearDown(self):
        super(TestExample01, self).tearDown()
