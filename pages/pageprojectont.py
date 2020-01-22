from locators.projectont import Projectontwikkelaars
from  selenium.webdriver.support.select import Select

class ProjectPage:

    def __init__(self,browser):
        self.browser = browser

    def newproject(self):
        self.browser.find_element(*Projectontwikkelaars.project_link).click()

    def datafield(self,locator,data):
        self.browser.find_element(*locator).send_keys(data)

    def dropdown(self,dd_loc,value):
        select = Select(self.browser.find_element(*dd_loc))
        select.select_by_value(value)