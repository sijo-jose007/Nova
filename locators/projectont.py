from selenium.webdriver.common.by import By

class Projectontwikkelaars:

    project_link = (By.CSS_SELECTOR, "li.main-item.nav-item:nth-child(3) >a")
    pro_page_title = "Projectleiders | ECCO NOVA"
    lastname = (By.CSS_SELECTOR, "input#lastname.form-control")
    firstname = (By.CSS_SELECTOR, "input#firstname.form-control")
    titel_van_het_project = (By.CSS_SELECTOR, "input#title.form-control")
    type = (By.CSS_SELECTOR, "select#type_id.form-control")
    company = (By.CSS_SELECTOR, "input#company.form-control")
    location = (By.CSS_SELECTOR, "input#location.form-control")
    state = (By.CSS_SELECTOR, "select#state.form-control")
    telephone = (By.CSS_SELECTOR, "input#tel.form-control")
    description = (By.CSS_SELECTOR, "textarea#description")
    email = (By.CSS_SELECTOR, "input#email.form-control")