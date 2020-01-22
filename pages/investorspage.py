from locators.investorsloc import Investeerders


class Investor:

    def __init__(self, browser):
        self.browser = browser

    def linkclick(self,link):
        self.browser.find_element(*link).click()

    def imgpresence(self):
        elem = self.browser.find_element(*Investeerders.imgloc)
        return elem.get_attribute('class')

    def datafield(self,locator,data):
        self.browser.find_element(*locator).send_keys(data)

    def checkbox(self):
        self.browser.find_element(*Investeerders.check).click()
