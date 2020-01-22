from locators.homepage import Homepageloc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Startpagina:

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(Homepageloc.url)

    def titlecheck(self):
        return self.browser.title

    def slides(self):
        try:
            element_present = EC.presence_of_element_located((Homepageloc.slide1))
            elem = WebDriverWait(self.browser, 2).until(element_present)
            return elem.get_attribute('title')
        except TimeoutException:
            print("Timed out while waiting for page to load")


