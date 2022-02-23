#!/usr/bin/python3
# -*- encoding=utf8 -*-
import pytest
from time import sleep
from pages.rms_pages import RMSHome


def test_global_search_runner_full_name(browser):
    """ Check that possible find any runner by Runner Full name. """

    home_page = RMSHome(browser)

    home_page.search = "Michael Capiraso"
    home_page.search_button.click()
    home_page.runners_count.is_visible()
    runners_count = home_page.runners_count.get_text()
    assert home_page.runners_count.get_text() == "RUNNERS: 96"

    sleep(2)