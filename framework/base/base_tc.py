#!/usr/bin/env python
import sys, unittest, os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Ie
from selenium.webdriver import DesiredCapabilities
from selenium.common.exceptions import WebDriverException, SessionNotCreatedException
# Get configuration
from .config import env_config
# Make Firefox headless to this fixed size
os.environ['MOZ_HEADLESS_WIDTH'] = '1920'
os.environ['MOZ_HEADLESS_HEIGHT'] = '1200'


class BaseTestCase(unittest.TestCase):

    """
        Base Test Case which is inherited through all tests in order to
        provide proper webdriver workflow to set up and
        tear down test case groups.
    """

    # some configuration defaults if the environment is started from Pycharm/Terminal
    BASE_LINK = "https://"

    try:
        BASE_LINK = env_config.get('url')
    except SystemExit:
        pass

    try:
        browser_env = os.environ["BROWSER_ENV"]
    except KeyError:
        # browser_env is empty if not running in terminal, therefore it Chrome is added as default here in code 4 PyChrm
        browser_env = "chrome"

    def get_base_link(self):
        try:
            return env_config.get('url')
        except SystemExit:
            return self.BASE_LINK

    def setUp(self):
        if self.browser_env == 'chrome':
            # this is the setup for working remotely with linux
            # in house just call self.driver = Chrome()
            # Use these commands if you don't want Chrome in headless mode
            options = webdriver.ChromeOptions()
            options.add_argument('--user-agent=piinctest')
            self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)

        # Use these commands for Chrome headless
        elif self.browser_env == 'headless':
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument("--window-size=1920x1080")
            self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)

        elif self.browser_env == 'firefox':
            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override", "piinctest")
            self.driver = Firefox(profile)

        # Use these commands for Firefox headless
        elif self.browser_env == 'firefoxHeadless':
            options = webdriver.FirefoxOptions()
            options.add_argument('-headless')
            options.add_argument("--window-size=1920x1080")
            self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver', options=options)

        elif self.browser_env == "iexplorer":
            caps = DesiredCapabilities.INTERNETEXPLORER.copy()
            caps["ensureCleanSession"] = True
            # This is set as suggested default path, if you have different path, change it /usr/local/bin
            self.driver = Ie(executable_path="C:/webdrivers/iedriverserver.exe", capabilities=caps)

        self.driver.delete_all_cookies()
        try:
            self.driver.maximize_window()
        except AttributeError:
            self.driver.set_window_size(1920, 1200)
        except WebDriverException:
            self.driver.set_window_size(1920, 1200)
        self.driver.get(self.BASE_LINK)

    def tearDown(self):
        global result
        if hasattr(self, '_outcome'):  # Python 3.4+
            result = self.defaultTestResult()
            self._feedErrorsToResult(result, self._outcome.errors)
        if len(result.errors) > 0 or len(result.failures) > 0:
            fail_url = self.driver.current_url
            print(fail_url)
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
            fn = os.path.join(os.path.dirname(__file__), '..', '..', 'screenshots/Screenshot_%s.png' % now)
            self.driver.get_screenshot_as_file(fn)
            print(str("Screenshot added at path: " + fn))
        self.driver.close()
        self.driver.quit()

    # THIS IS THE OLD tearDown and it is working in python2.7 but not in 3.5 and above
    # def tearDown(self):
    #     if sys.exc_info()[0]:  # Returns the info of exception being handled
    #         fail_url = self.driver.current_url
    #         print(fail_url)
    #         now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
    #         fn = os.path.join(os.path.dirname(__file__), '..', '..', 'screenshots/Screenshot_%s.png' % now)
    #         self.driver.get_screenshot_as_file(fn)
    #         print(str("Screenshot added at path: " + fn))
    #     self.driver.close()
    #     # firefox complains on this
    #     try:
    #         self.driver.quit()
    #     except SessionNotCreatedException:
    #         pass
