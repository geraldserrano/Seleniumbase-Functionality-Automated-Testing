from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import time

class OrderAssertions(BaseCase):
    def assert_select_province(self):
        self.click("select#city")  # Click on the city dropdown to expand it
        self.wait_for_element_present("select#city option[value='18845']")  # Wait for the BAAO option to be loaded
        # Assert that 'BAAO' is one of the options in the city dropdown
        self.assert_element("select#city option[value='18845']")
        self.assert_text("BAAO", "select#city option[value='18845']")
        time.sleep(3)

    def assert_select_city(self):
        time.sleep(4)
        self.wait_for_element_present("select#barangay")  # Ensure barangay dropdown is ready for interaction
        self.click("select#barangay")  # Click the barangay dropdown to expand it
        self.wait_for_element_present("select#barangay option")  # Wait for the options to be loaded
        self.assert_text("Abella", "select#barangay")
        time.sleep(4)
        
    def assert_select_barangay(self):
        time.sleep(2)
        selected_option_text = self.get_text("select#barangay option:checked")
        self.assert_equal("Abella", selected_option_text)
        time.sleep(3)
        
    def assert_select_date(self):
        date_element = self.wait_for_element_visible("td.sorting_1")
        displayed_date = date_element.text.strip()  # Get the text content of the element
        # Parse the displayed date to a datetime object
        displayed_datetime = datetime.strptime(displayed_date, "%m/%d/%y %I:%M:%S %p")
        # Calculate the date range for last month
        today = datetime.now()
        first_day_of_last_month = datetime(today.year, today.month - 1, 1)
        last_day_of_last_month = first_day_of_last_month + timedelta(days=30)  # Approximation
        # Check if the displayed date falls within the last month date range
        assert first_day_of_last_month <= displayed_datetime <= last_day_of_last_month, \
            f"The displayed date '{displayed_date}' is not from last month."
        time.sleep(4)
        
    def assert_select_user(self):
        # Locate the element containing the displayed user (in this case, <span> with class "badge-warning")
        user_element_locator = "span.fsc-9.me-1.badge.badge-warning"
        # Retrieve the text displayed for the user
        displayed_user = self.get_text(user_element_locator)
        # Define the expected user value
        expected_user = "S3"
        # Assert that the displayed user matches the expected user
        assert displayed_user.strip() == expected_user, f"Displayed user '{displayed_user}' does not match expected user '{expected_user}'"
        time.sleep(4)
        
    def verify_city(self):
        xpath_locator = '//*[@id="macpos-orders"]/tbody/tr[1]/td[8]'  # Adjust as needed
        # Find the <td> element using the XPath locator
        td_element = self.find_element(By.XPATH, xpath_locator)
        # Get the text content of the <td> element
        td_text = td_element.text.strip()
        # Assert that the text content matches the expected value
        expected_text = "NAGA CITY"
        self.assertEqual(td_text, expected_text, f"Expected '{expected_text}', but found '{td_text}'")
        time.sleep(4)    
        
    def assert_pdf_opened_in_new_tab(self):
        assert ".pdf" in self.get_current_url(), "PDF file did not open in a new tab"
        time.sleep(4)
        
    def assert_sort_reference(self):
        reference_elements = self.find_elements("span.fsc-9.me-1.badge.badge-secondary")

        # Extract and store the reference numbers from the elements
        reference_numbers = []
        for element in reference_elements:
            reference_text = element.text.strip()
            if reference_text.isdigit():  # Check if the text is a number
                reference_numbers.append(int(reference_text))  # Convert to integer and store

        # Check if the reference numbers are in ascending order
        is_ascending = all(reference_numbers[i] <= reference_numbers[i + 1] for i in range(len(reference_numbers) - 1))

        # Assert that the reference numbers are in ascending order
        self.assertTrue(is_ascending, "Reference numbers are not in ascending order")
        time.sleep(4)
    
    def _convert_to_datetime(self, date_str):
        # Convert date-time string to a datetime object
        # Adjust the format according to your date-time string (e.g., "04/15/24 04:40:52 PM")
        from datetime import datetime
        date_format = "%m/%d/%y %I:%M:%S %p"
        return datetime.strptime(date_str, date_format)
      
    def assert_ordered_at(self):
        # Find all date elements using the CSS selector for the specific column
        date_elements = self.find_elements("td.sorting_1")
        # Extract and store the date-time strings from the elements
        date_strings = []
        for element in date_elements:
            date_text = element.text.strip()
            date_strings.append(date_text)  # Store the date-time string
        # Convert date-time strings to datetime objects for comparison
        date_objects = []
        for date_str in date_strings:
            date_obj = self._convert_to_datetime(date_str)
            date_objects.append(date_obj)
        # Check if the date objects are in ascending order
        is_ascending = all(date_objects[i] <= date_objects[i + 1] for i in range(len(date_objects) - 1))
        # Assert that the date objects are in ascending order
        self.assertTrue(is_ascending, "Dates are not in ascending order")
        time.sleep(4)
    
    def assert_sort_amount(self):
        numeric_elements = self.find_elements("td.text-end.fw-semibold.sorting_1")
        # Extract and store the numeric values from the elements
        numeric_values = []
        for element in numeric_elements:
            numeric_text = element.text.strip()
            # Remove any non-numeric characters and convert to float
            numeric_value = float(''.join(filter(str.isdigit, numeric_text)))
            numeric_values.append(numeric_value)  # Store the numeric value
        # Check if the numeric values are in ascending order
        is_ascending = all(numeric_values[i] <= numeric_values[i + 1] for i in range(len(numeric_values) - 1))
        # Assert that the numeric values are in ascending order
        self.assertTrue(is_ascending, "Numeric values are not in ascending order")
        time.sleep(4)
        
    def assert_sort_items(self):
        td_elements = self.find_elements("td.text-end")
        # Extract and store the numeric values from the <td> elements
        values = []
        for element in td_elements:
            value_text = element.text.strip()
            # Convert the text value to an integer for comparison
            try:
                value = int(value_text)  # Convert text to integer
                values.append(value)  # Store the integer value
            except ValueError:
                # Handle cases where the text cannot be converted to an integer
                pass
        # Check if the values are in ascending order
        is_ascending = all(values[i] <= values[i + 1] for i in range(len(values) - 1))
        # Assert that the values are in ascending order
        self.assertTrue(is_ascending, "Values are not in ascending order")
        time.sleep(4)      
            
    def assert_search_store(self):
        # Define the XPath locator for the specific <td> element containing "Juan's Store"
        xpath_locator = '//*[@id="macpos-orders"]/tbody/tr[1]/td[7]/div'

        # Wait for the <td> element to become visible and interactable
        self.wait_for_element_visible(xpath_locator)

        # Get the text content of the <td> element using the XPath locator
        td_text = self.get_text(xpath_locator)

        # Assert that the expected text ("Juan's Store") is present in the <td> element
        expected_text = "Tess Store"
        self.assert_equal(td_text, expected_text, f"Expected '{expected_text}', but found '{td_text}'")
        time.sleep(4)