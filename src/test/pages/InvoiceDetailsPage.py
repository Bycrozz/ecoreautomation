import re

from selenium.webdriver.common.by import By


class InvoiceDetailsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_invoice_fields(self):
        #returns the texts displayed in the invoice screen for each required element, based on their xpath locator
        customer_details_parts = self.driver.find_element(By.XPATH, "//h5[text()='Customer Details']/following-sibling::div").text.splitlines()
        data = {
            "hotel_name": self.driver.find_element(By.XPATH, "//h4[@class='mt-5']").text,
            "invoice_date": self.driver.find_element(By.XPATH, "//li[span[text()='Invoice Date:']]").text.replace("Invoice Date:", "").strip(),
            "due_date": self.driver.find_element(By.XPATH, "//li[span[text()='Due Date:']]").text.replace("Due Date:", "").strip(),
            "invoice_number": re.search(r"#(\d+)", self.driver.find_element(By.XPATH, "//h6[@class='mt-2']").text).group(1),
            "booking_code": self.driver.find_element(By.XPATH, "//td[text()='Booking Code']/following-sibling::td").text,
            "customer_name": customer_details_parts[0].strip(),
            "customer_address": customer_details_parts[1].strip(),
            "customer_address_number": customer_details_parts[2].strip(),
            "room": self.driver.find_element(By.XPATH, "//td[text()='Room']/following-sibling::td").text,
            "check_in": self.driver.find_element(By.XPATH, "//td[text()='Check-In']/following-sibling::td").text,
            "check_out": self.driver.find_element(By.XPATH, "//td[text()='Check-Out']/following-sibling::td").text,
            "total_stay_count": self.driver.find_element(By.XPATH, "//td[text()='Total Stay Count']/following-sibling::td").text,
            "total_stay_amount": self.driver.find_element(By.XPATH, "//td[text()='Total Stay Amount']/following-sibling::td").text,
            "deposit_now": self.driver.find_element(By.XPATH, "//h5[text()='Billing Details']/following-sibling::table[@class='table']/tbody//td[1]").text,
            "tax_and_vat": self.driver.find_element(By.XPATH, "//h5[text()='Billing Details']/following-sibling::table[@class='table']/tbody//td[2]").text,
            "total_amount": self.driver.find_element(By.XPATH, "//h5[text()='Billing Details']/following-sibling::table[@class='table']/tbody//td[3]").text
        }
        return data




