# Ecore automation project

---
### Tools used:

- Phyton
- Selenium
- Pytest
---
### Folder structure:

- **src/test/pages** - The page object classes
- **src/test/testData** - The JSON files with data to be used in the test scenarios
- **src/test/tests** - The files containing the test scenarios to be run
- **src/test/utils** - Utility classes
---
### Setup and run the tests: 
Requirements: Have the [latest version](https://www.python.org/downloads/) of Python installed. 

1. Open the terminal and clone the git repository:

        git clone https://github.com/Bycrozz/ecoreautomation.git
2. Navigate with the terminal to the cloned git folder and install the dependencies:

        python -m pip install -r requirements.txt
3. Run the tests using the pytest command will automatically run all the tests

        python -m pytest

    3.1 - To run a specific test class use the following command (example with login):

        python -m pytest src/test/tests/login_test.py

    3.2 - This project supports multithreading (parallel testing) and headless. To run a test class with multiple threads and headless use the command below:

         python -m pytest src/test/tests/login_test.py -n 5 --headless
   where "-n 5" means 5 threads will be used, so to run with more or less threads change this parameter.
                     
   3.3 - It's possible to run a specific test scenario instead of the test class. Each scenario is marked with `@pytest.mark.TAGNAME` (this can be combined with parallel running and headless)

         python -m pytest -m TAGNAME
4. After running the tests the results are shown in the terminal, but a HTML report is generated in folder `ecoreautomation/reports/html_report/report.html`
---
###  Test cases and expected results:

1 - **Valid login:** Should pass with the current credentials.

2 - **Invalid login:** Should pass with all the invalid credentials, with the valid credentials should fail.

3 - **Invoice details:** Should fail because the "tax and vat" and "total amount" are displaying the values in a format different from the expected in the test case documentation.