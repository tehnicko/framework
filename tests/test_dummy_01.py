#!/usr/bin/env python
from framework.base.base_tc import BaseTestCase
from framework.pages.login_page import LoginPage
import time


class TestDummy01(BaseTestCase):

    def setUp(self):
        super(TestDummy01, self).setUp()

    def test_dummy1(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username("TestDummy01")
        time.sleep(3)

    def tearDown(self):
        super(TestDummy01, self).tearDown()
