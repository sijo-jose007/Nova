from selenium.webdriver.common.by import By


class Homepageloc:

    url = "https://www.ecconova.com/"
    title = "Startpagina | ECCO NOVA"
    slide1 = (By.CSS_SELECTOR, "div.slide.slide1  div.slide-content a")
    slide2 = (By.CSS_SELECTOR, "div.slide.slide2 div.slide-content a")
    slide3 = (By.CSS_SELECTOR, "div.slide.slide3 div.slide-content a")
    slide1Title = "Voir la page à propos"
    slide2Title = "Ontdek de projecten"
    slide3Title = "Uw project voorstellen"