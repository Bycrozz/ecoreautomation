from selenium.webdriver.common.by import By

from src.test.pages.InvoiceListPage import InvoiceListPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/")

    def login(self, username, password):
        #log in the application with the given user and pass
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.ID, "btnLogin").click()

    def verify_successful_login(self):
            invoice_list_page = InvoiceListPage(self.driver)
            return invoice_list_page.get_invoice_list_header().is_displayed()

    def verify_failed_login(self):
            invalid_login_message = self.driver.find_element(By.XPATH, "//div[contains(@class, 'alert-danger') and "
                                                                       "contains(text(),'Wrong username or password')]")
            return invalid_login_message.is_displayed()
