from selenium.webdriver.common.by import By


class InvoiceListPage:
    def __init__(self, driver):
        self.driver = driver

    def select_invoice(self, position):
        # Select the invoice in the list based on the selected position
        invoice_list = self.driver.find_elements(By.LINK_TEXT, "Invoice Details")
        if len(invoice_list) >= position:
            invoice_list[position - 1].click()
        else:
            print(f"The invoice in desired position: {position} does not exist")

    def get_invoice_list_header(self):
        # Return the h2 element that contains the "Invoice List" text
        return self.driver.find_element(By.XPATH, "//h2[text()='Invoice List']")