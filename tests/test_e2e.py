import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from Utils.BaseClass import BaseClass
from tests import UserData


class Test(BaseClass):
    def test_e2e(self, user_data):
        log = self.test_loggingDemo()
        url = "https://rahulshettyacademy.com/angularpractice/"
        self.driver.get(url)
        log.info("Url Entered" + url)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, 400)")
        log.info("Screen scrolled to 400 pixelds")
        home = HomePage(self.driver)
        home.getName().send_keys(user_data["Name"])
        log.info("First Name Entered " +  user_data["Name"])
        home.getEmail().send_keys(user_data["email"])
        log.info("Email Entered " + user_data["email"])
        #Select(home.getDropdown()).select_by_visible_text(user_data["gender"])
        #log.info("Gender Entered " + user_data["gender"])
        time.sleep(3)
        self.driver.refresh()

    @pytest.fixture(params=UserData.User_Data.get_data("TestCase2"))
    def user_data(self, request):
        return request.param
