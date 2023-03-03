from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self,driver):
        self.driver=driver

    def wait_for_elements_to_click(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 5)
        element=wait.until(EC.element_to_be_clickable((locator_type,locator)))
        return element

    def wait_for_presence_of_elements(self,locator_type,locator):
        wait = WebDriverWait(self.driver, 5)
        list_of_elements=wait.until(EC.presence_of_all_elements_located((locator_type,locator)))
        return list_of_elements

# some code from SDET2



