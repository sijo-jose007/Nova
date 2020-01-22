from selenium.webdriver.common.keys import Keys


class Tabs:
    def __init__(self, browser):
        self.browser = browser

    def opentab(self):
        """You can use (Keys.CONTROL + 't') on other OSs
        Keys.COMMAND + 't')  on OSX"""
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

    def closetab(self):
        """(Keys.CONTROL + 'w') on other OSs.
        (Keys.COMMAND + 'w') on OSX """
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
        self.browser.close()


