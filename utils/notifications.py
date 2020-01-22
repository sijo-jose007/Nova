from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

import logging
import logging.config


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
file_handler = logging.FileHandler("irtc.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

chrome_options = Options()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
logger.info("turning off browser notifications")
driver = Chrome(chrome_options=chrome_options, executable_path=r"C:\Users\Sijo.Jose\Desktop\sel\tests\chromedriver")

driver.maximize_window()
driver.get_cookies()
driver.get("https://www.irctc.co.in/nget/train-search")


