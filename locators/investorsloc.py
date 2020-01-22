from selenium.webdriver.common.by import By


class Investeerders:

    investor = (By.CSS_SELECTOR, "li.main-item.nav-item:nth-child(2) >a")
    title = "Investeerders | ECCO NOVA"
    details = (By.CSS_SELECTOR, "div.info >a[href*='horizon-paradis']")
    imgclass = "project__img"
    imgloc = (By.CSS_SELECTOR, "img[src$='slide_0.jpg']")
    lastname = (By.CSS_SELECTOR, "input#lastname.form-control")
    firstname = (By.CSS_SELECTOR, "input#firstname.form-control")
    email = (By.CSS_SELECTOR, "input#email.form-control")
    postcode = (By.CSS_SELECTOR, "input#postcode_code.form-control")
    check = (By.CSS_SELECTOR, "div.form-group.checkbox >label")
    cookie = (By.CSS_SELECTOR, "button.js-cookie-consent-agree")