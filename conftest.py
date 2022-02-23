#!/usr/bin/python3
# -*- encoding=utf8 -*-

import pytest
import allure
import uuid
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser(chrome_options):
    browser = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())
    #browser.set_window_size(1920/2, 1080)
    # grid_url = "http://localhost:4444/wd/hub"
    # desired_caps = DesiredCapabilities.CHROME
    # browser = webdriver.Remote(desired_capabilities=desired_caps, command_executor=grid_url)
    yield browser

    # if request.node.rep_call.failed:
    #     # Make the screen-shot if test failed:
    #     try:
    #         browser.execute_script("document.body.bgColor = 'white';")
    #
    #         # Make screen-shot for local debug:
    #         browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')
    #
    #         # Attach screenshot to Allure report:
    #         allure.attach(browser.get_screenshot_as_png(),
    #                       name=request.function.__name__,
    #                       attachment_type=allure.attachment_type.PNG)
    #
    #         # For happy debugging:
    #         print('URL: ', browser.current_url)
    #         print('Browser logs:')
    #         for log in browser.get_log('browser'):
    #             print(log)
    #
    #     except:
    #         pass  # just ignore any errors here

    browser.quit()

@pytest.fixture
def chrome_options(chrome_options):
    # chrome_options.binary_location = '/usr/bin/google-chrome-stable'
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')
    chrome_options.add_argument("--window-size=1920/2,1080")

    return chrome_options

def get_test_case_docstring(item):
    """ This function gets doc string from test case and format it
        to show this docstring instead of the test case name in reports.
    """

    full_name = ''

    if item._obj.__doc__:
        # Remove extra whitespaces from the doc string:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Generate the list of parameters for parametrized test cases:
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            # Create List based on Dict:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Add dict with all parameters to the name of test case:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """ This function modifies names of test cases "on the fly"
        during the execution of test cases.
    """

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)

def pytest_collection_finish(session):
    """ This function modified names of test cases "on the fly"
        when we are using --collect-only parameter for pytest
        (to get the full list of all existing test cases).
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # If test case has a doc string we need to modify it's name to
            # it's doc string to show human-readable reports and to
            # automatically import test cases to test management system.
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')