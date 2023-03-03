import time

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

class launch_page(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    SEARCH_BOX="twotabsearchtextbox"
    SEARCH_BUTTON="nav-search-submit-button"

    def getSearchField(self):
        return self.wait_for_elements_to_click(By.ID, self.SEARCH_BOX)

    def getSearchButton(self):
        return self.wait_for_elements_to_click(By.ID, self.SEARCH_BUTTON)

    def enterSearchText(self,search_text):
        self.getSearchField().send_keys(search_text)

    def clickSearchButton(self):
        self.getSearchButton().click()

    def performSearch(self,search_text):
        self.enterSearchText(search_text)
        self.clickSearchButton()

