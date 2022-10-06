
from selenium import webdriver
import time
import pytest

from Test.Test_Base import TestBase


class TestMainPage(TestBase):

    def test_go_to_description(self):
        time.sleep(5)
        temp = self.APP.any_page.click_button_description()
        assert temp == 'https://ngieu.ru/sveden/'
