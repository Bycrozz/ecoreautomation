import pytest

from src.test.pages.InvoiceDetailsPage import InvoiceDetailsPage
from src.test.pages.InvoiceListPage import InvoiceListPage
from src.test.utils.TestUtils import TestUtils


@pytest.mark.usefixtures("browser")
class TestInvoiceDetails(TestUtils):

    @pytest.mark.parametrize("invoice_data",
                             TestUtils.load_test_data("src/test/testData/invoiceData.json", "invoice_data"))
    @pytest.mark.invoice_details
    def test_invoice_details(self, browser, invoice_data, open_login_page):
        """
        Logs in the application, select the invoice by position and compare the invoice data displayed on the screen with
        the invoice data retrieved from the Json data file.
        """
        # Login
        open_login_page.login(invoice_data["username"], invoice_data["password"])

        # Retrieve Invoice Fields from the page
        invoice_list_page = InvoiceListPage(browser)
        invoice_list_page.select_invoice(1) #if needed to select a different invoice, this can be parametrized in the Json file
        TestUtils.switch_to_tab_with_url(browser, "/invoice")
        invoice_details_page = InvoiceDetailsPage(browser)
        actual_invoice_data = invoice_details_page.get_invoice_fields()

        # Compare each key-value pair in JSON data for invoice with the actual data
        for key, expected_value in invoice_data.items():
            # Skip username and password as they're not part of invoice details
            if key in ["username", "password"]:
                continue
            # Get the actual value from the page data
            actual_value = actual_invoice_data.get(key)
            assert actual_value == expected_value, f"Mismatch in {key}: Expected '{expected_value}', got '{actual_value}'"
