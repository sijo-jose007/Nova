from selenium.webdriver import Chrome
import pytest
from pages.pageprojectont import ProjectPage
from locators.projectont import Projectontwikkelaars
from pages.investorspage import Investor
from locators.investorsloc import Investeerders
from locators.homepage import Homepageloc
from pages.startpage import Startpagina
import logging
import logging.config

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
file_handler = logging.FileHandler("test.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


@pytest.fixture()
def browser():
    driver = Chrome(r"C:\Users\Sijo.Jose\Desktop\sel\tests\chromedriver")
    driver.maximize_window()
    driver.get_cookies()
    driver.implicitly_wait(10)

    yield driver
    driver.save_screenshot("screenshot.png")
    driver.quit()


def test_project(browser):
    start = Startpagina(browser)
    # load url
    start.load()
    # verify title
    title = start.titlecheck()
    assert title == Homepageloc.title
    # slide verification
    slide = start.slides()
    try:
        assert slide == Homepageloc.slide2Title
    except AssertionError:
        logging.exception("Exception occurred")
    project = ProjectPage(browser)
    # move to projects
    project.newproject()
    # title verification
    pro_title = start.titlecheck()
    assert pro_title == Projectontwikkelaars.pro_page_title

    # lastname
    project.datafield(Projectontwikkelaars.lastname, "sijo")
    # firstname
    project.datafield(Projectontwikkelaars.firstname, "jose")
    # title van het project
    project.datafield(Projectontwikkelaars.titel_van_het_project, "myproject")
    # type
    project.dropdown(Projectontwikkelaars.type, "12")
    # company
    project.datafield(Projectontwikkelaars.company, "xyz co pvt ltd")
    # location
    project.datafield(Projectontwikkelaars.location, "brussels")
    # state
    project.dropdown(Projectontwikkelaars.state, "3")
    # gsm number
    project.datafield(Projectontwikkelaars.telephone, "9874561230")
    # description
    project.datafield(Projectontwikkelaars.description, "sample project to be created")
    # email
    project.datafield(Projectontwikkelaars.email, "abc@xyc.com")

    invest = Investor(browser)
    # invertors
    invest.linkclick(Investeerders.investor)
    # title assertion
    title = start.titlecheck()
    assert title == Investeerders.title
    # click on more details
    invest.linkclick(Investeerders.details)
    # imgae verification
    img = invest.imgpresence()
    assert img == Investeerders.imgclass
    # lastname
    invest.datafield(Investeerders.lastname, "sijo")
    # firstname
    invest.datafield(Investeerders.firstname, "jose")
    # email
    invest.datafield(Investeerders.email, "abc@xyc.com")
    # postcode
    invest.datafield(Investeerders.postcode, "45632114")
    # checkbox
    invest.checkbox()
    # cookie
    invest.linkclick(Investeerders.cookie)
