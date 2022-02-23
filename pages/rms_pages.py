#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from baseUtils.base_page import BasePage
from baseUtils.elements import WebElement
from baseUtils.elements import manyWebElements


class RMSHome(BasePage):

    def __init__(self, web_driver, url=""):
        if not url:
            url = "http://192.168.51.7:8215/Home"
        super().__init__(web_driver, url)

    # Global search field
    search = WebElement(id='search-races-runners_value')

    # Search button
    search_button = WebElement(xpath="//div[@class='control_buttons']/a[1]")

    # Runners count on the Top of items grid
    runners_count = WebElement(xpath="//*[@id='filtr2']//li[1]/a")


class RMSClubStanding(BasePage):

    def __init__(self, web_driver, url="http://192.168.51.7:8215/clubstandings"):
        super().__init__(web_driver, url)