# Framework (Python)


### Requirements to work with the framework

    * Python 3.6+
    * Python IDE by preference
    * Pip
    * chromium-browser



### Getting code from Git

#### Creating new repository (with SSH key)
Create a directory where you want to create and create a project.
Go into the project directory, open the console and type in next commands:

    git clone <<< YOUR REPO >>>


#### Install webdrivers

This command will install webdrivers for Linux:

    ./install.sh

#### Creating virtual environment for the testing

If you do not have virtualenv installed please add it as we won't upgrade venv each time there is a modification
to it in order to have freedom to experiment with diverse packages. We will assume you have python 3.6 or higher on
your machine as per requirements. Open console and direct yourself to the location where the project is installed e.g. /home/PiincTesting

#### Commands to install virtual environment are:

    sudo apt-get virtualenv

or in case that previous command throws error try:

    pip install virtualenv

To initialize virtual envirnment create a **venv** folder into the project directory and initialize it with command:

    virtualenv venv


#### To activate virtual environment type in command:

    source venv/bin/activate

Having the downloaded text file **requirements.txt** install them into venv with command

    pip install -r requirements.txt

For any further updates/changes regarding the requirements to update the venv use command:

    pip install -r requirements.txt --upgrade

This should keep up to date with new plugins and libraries added to project. But please do not add those into Git repo
unless there is an agreement to use it in the future, not just local branch experiment.


### Windows instalation and usage

To setup Python on Windows please follow the official guidelines on the [Official Python website](https://www.python.org/)

Additional useful tutorials for setup:

[How To Install Python, pip, and virtualenv on Windows with PowerShell](http://www.tylerbutler.com/2012/05/how-to-install-python-pip-and-virtualenv-on-windows-with-powershell/)

[Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/)


### Webdrivers fo Windows

Any webdriver desired to be used on by default for framework is on path "C:\webdrivers\YOUR_DRIVER" (ChromeDriver, InternetExplorerDriver...)

If you have saved it into different location you will need to update in the framework once downloaded.

In order for Windows to use the drivers globaly the location of the drivers need to be added on the System Environment Variable PATH, by default "C:\webdrivers\"


### Run tests in Internet Explorer 11

In order to run tests in Internet Explorer 11 you need InternetExplorerDriver (version 2.53.1 at the time of writing this update)
downloadable from [Selenium site](http://www.seleniumhq.org/download/)

Once you have downloaded the InternetExplorerDriver/ by framework default it is set up for path "C:\webdrivers\iedriverserver.exe"

If you have saved it into different location, please adjust the path in the framework before usage

Additional setup for Internet Explorer requires:

1. Security levels to be the same (open the IE browser, go to "Internet Options" - Security and set all options to same security level)
2. Enable Protected Mode should be enabled (open the IE browser, go to "Internet Options" - Security and set all options to Protected Mode bu selecting the checkbox)


#### Potential issue at test run - IE11 exceptions with IEDriverServer: Unable to get browser

I suggest to set it up before test runs anyway

    Create a DWORD value with the name "iexplore.exe" and the
    value of 0 in the following key (for 32-bit Windows):
    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE

    For 64-bit Windows installations, the following key should be used:
    KEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE


#### Guidelines for using the framework:

[Official Python website](https://www.python.org/)

[Selenium](http://www.seleniumhq.org/)

[Python-Selenium bindings](http://selenium-python.readthedocs.io/)

[Page Object Pattern Guide](https://github.com/SeleniumHQ/selenium/wiki/PageObjects)

[Python Unittest](https://docs.python.org/2/library/unittest.html)

[Pytest Documentation](http://doc.pytest.org/en/latest/contents.html)


# Framework folder, files hierarchy and usage


Installation of the framework should be done by now from the version control repository README file.
Framework is written in Python language and it has highly advised to follow the coding guides from their ruling:
Folder names, file names and method names are small letters divided with underscore between words. Class name words start with capital letters without underscore. Tests always start
with "__test___*" in order to be recognised by the unittest and pytest libraries that will execute tests.

Folder hierarchy:

	Project/
		framework/
			base/
			dialogs/
			pages/
		tests/
    	venv/
    	...


Folder **framework/** - to contain all the base files and functions, dialogs and pages for the platform, based on the Page Object pattern, grouped as visible.

Folder **tests/** - to contain all tests grouped by the grouping conventions.

Folder **venv/** - folder that contains the virtual environment libraries and other files, which is unique for the user specific and should never be added to the version control repository.

Other folders are added by some exclusions as the are generated by the Pytest or other library or the Screenshots Folder that is not relevant at the beginning, only the folder itself for
generating purposes. Sreenshots will be added to the designated folder by default inside the project.


### Base files

The **base/** folder contains base types of pages, functions and other page sections that are present on multiple places in order to group them under single usage and inherit them further
where they are used. Basic OOP standards - if some element or function is being used on more than one place it should be added to a corresponding "__base___*" file depending on which section
it appears. The **base_page.py** file is the placeholder for global functions used everywhere and contains generic locators which appear on pages and dialogs more than once.
All other pages and dialogs are extending this file in order to use the general functions.


### Dialogs

Dialog modals (pop-ups) are separated as they are used in the content type creations. Following Page-Object Pattern each content type has it’s own page file with locators and functions
specific for the dialog. All dialogs are derived as extension of **base_dialog.py**.


### Pages

Pages are separated in order of grouping them by Page-Object Pattern standardisation that each page is a file of its own with own non-generic locators, derived as extension
of the **base_page.py**.


### Tests

As previously mentioned the tests/ directory will contain the tests that will be automated and grouped into files by the Test Automation Guide description.
Tests will be runned from the project directory from testrunner.py or other files regarding the necessity for the testing. New test files will be added by necessity and the document will be
updated accordingly. These files will contain a collection of tests from the test files in the **test/** folder.
The **test_dummy.py** file is created for local testing and should not be updated in the version control repository.


### Test runs

To run test first check configuration file at **config.ini**. You can copy example configuration from **config.ini.example**:

    cp config.ini.example config.ini

Test runs are capable to run in single-sequential or parallel order, packaged into some runner file e.g testrunner.py and the executions can be conducted with various commands:

Run single-sequential, example command:

    ./run_test.py tests/testdummy.py

Run parallel with 3 browsers, example command:

    ./run_test.py -n 3 tests/testdummy.py -n 3

Run in parallel with HTML report generation at the end, example command:

    ./run_test.py --html tests/testdummy.py -n 3

**NOTE:** Combination of commands is possible, the pytest will parse it and work with it accordingly, parallel or single test run. The --html command will create the html report file in the report folder whit name of the runner file and timestamp (example: testdummy_02-04-2019_11-33-57.html )

For more commands run:

    ./run_test.py --help

### Additional

This document will be expanded in need, if some major changes or additions happened to the framework. This is a basic guideline to work with the framework with assumption that developer has
some previous skills in OOP, Python or other language and previous familiarity with the guides listed above.
# framework
# framework
