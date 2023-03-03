import pytest
from selenium.webdriver.common.by import By

from pages.launch_page import launch_page
from pages.search_results import search_results
from utilities.utils import Utils
from base.base_driver import BaseDriver
from ddt import ddt, data, file_data, unpack
import unittest
import allure

@pytest.mark.usefixtures("setup")
@ddt
class TestSearch(unittest.TestCase):

    # ALL_TITLES = "//span[@class='a-size-medium a-color-base a-text-normal']"
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp=launch_page(self.driver)
        self.sr=search_results(self.driver)
        self.ut=Utils()

    # @data("nokia")
    # @unpack
    @file_data("../testdata/testdata.json")
    def test_search_demo(self,search_text):

        # alltitlelist= self.bd.wait_for_presence_of_elements("XPATH",self.ALL_TITLES)
        self.lp.performSearch(search_text)
        self.sr.get_search_results()
        # self.ut.get_filtered_results(alltitlelist)
        # self.ut.assertInListItem(alltitlelist,search_text)
        self.driver.back()

