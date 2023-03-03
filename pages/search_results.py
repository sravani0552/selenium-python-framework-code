from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

class search_results(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
        ITEMS_LIST = "//span[@class='a-size-medium a-color-base a-text-normal']"
        FILTERED_LIST = "//span[contains(text(),'Nokia') and @class='a-size-medium a-color-base a-text-normal']"
    def get_search_results(self):
        return self.wait_for_presence_of_elements(By.XPATH,self.ITEMS_LIST)

    def get_filtered_search_results(self):
        return self.wait_for_presence_of_elements(By.XPATH,self.FILTERED_LIST)

    # locators
    CHECK_FIRST_PAGE_LOAD = (By.XPATH, "//span[@aria-label='Current page, page 1']")

     # filtered_list= get_filtered_search_results()
    def get_search_results(self):
        # self.driver_find_element(*self.CHECK_FIRST_PAGE_LOAD)
        items_list = self.wait_for_presence_of_elements("xpath","//span[@class='a-size-medium a-color-base a-text-normal']")
        filtered_list = self.wait_for_presence_of_elements("xpath","//span[contains(text(),'Nokia') and @class='a-size-medium a-color-base a-text-normal']")
        for items in filtered_list:
            print(items.text)
