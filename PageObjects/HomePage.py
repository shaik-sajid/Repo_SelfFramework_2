from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    name = (By.XPATH, "(//input[@name='name'])[1]")
    email = (By.XPATH, "//input[@name='email']")
    dropdown = (By.XPATH, "//select[@id='exampleFormControlSelect1']")

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getDropdown(self):
        return self.driver.find_element(*HomePage.dropdown)