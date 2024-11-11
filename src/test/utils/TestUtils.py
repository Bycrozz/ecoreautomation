# TestUtils.py
import json


class TestUtils:
    @staticmethod
    def load_test_data(file_path, test_type):
        """
        Load test data from a specified JSON file based on the provided test type (e.g., 'valid' or 'invalid').

        Args:
            file_path (str): Path to the JSON file containing test data.
            test_type (str): Key in the JSON file to filter the data (e.g., "valid" or "invalid").

        Returns:
            list of dicts: Each dict contains a set of parameters for a test.
        """
        with open(file_path, "r") as f:
            data = json.load(f)

        # Return a list of dictionaries for each test case
        if test_type in data:
            return data[test_type]
        else:
            raise ValueError(f"Test type '{test_type}' not found in the file {file_path}.")

    @staticmethod
    def switch_to_tab_with_url(driver, url_substring):
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            if url_substring in driver.current_url:
                return
        raise ValueError(f"No tab with URL containing '{url_substring}' was found.")
