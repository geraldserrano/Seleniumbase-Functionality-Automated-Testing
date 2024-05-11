from selenium.webdriver.support.ui import Select
from seleniumbase import BaseCase
import time

class OrderElements(BaseCase):
    def select_dropdown_by_value(self, selector, value):
        select_dropdown = Select(self.find_element(selector))
        select_dropdown.select_by_value(value)
        
    def click_transactions_button(self):
        self.wait_for_element_visible('a:contains("Transactions")')
        # Navigate to the Transactions and Orders page
        self.click('a:contains("Transactions")')
        time.sleep(4)
        
    def click_orders_button(self):
        self.wait_for_element_visible('a:contains("Orders")')
        self.click('a:contains("Orders")')
        time.sleep(4)
    
    def select_province(self):
        # Wait for the dropdown to be present on the page
        self.wait_for_element_visible("select#province")
        # Scroll the dropdown into view
        self.scroll_to_element("select#province")
        # Click the dropdown to open it (optional depending on dropdown behavior)
        self.click("select#province")
        # Select the option "CAMARINES SUR" by its value
        self.select_option_by_value("select#province", "18779")
        time.sleep(3)
        
    def select_city(self):
        self.wait_for_element_visible("select#city")
        self.click("select#city")  # Click on the city dropdown to expand it
        self.select_option_by_value("select#city", "18817")
        time.sleep(3)
        
    def select_barangay(self):
        self.wait_for_element_visible("select#barangay")
        self.click("select#barangay")  # Click on the barangay dropdown to expand it
        self.select_option_by_value("select#barangay", "18818")
        time.sleep(3)
        
    def select_date(self):
        self.wait_for_element_visible("select#date")
        # Click the dropdown to view options (this may not be necessary in all cases)
        self.click("select#date")
        # Select the 'Last Month' option from the dropdown
        self.select_option_by_value("select#date", "lastMonth")
        time.sleep(4)
        
    def select_user(self):
        dropdown_locator = "select#user_type"
        self.wait_for_element_visible(dropdown_locator)
        self.click(dropdown_locator)
        # Select the option "S3" from the dropdown
        option_locator = f"{dropdown_locator} > option[value='Customer']"
        self.click(option_locator)
        time.sleep(4)
        
    def print_selected(self):
        checkbox_selector = "input.form-check-input[type='checkbox'][data-nadmin--macpos--orders-target='parentCheckbox']"
        # Wait for the checkbox to become visible and interactable
        self.wait_for_element_visible(checkbox_selector)
        # Find all checkbox elements that match the selector
        checkbox_elements = self.find_elements(checkbox_selector)
        # Loop through each checkbox element and click if not already selected
        for checkbox_element in checkbox_elements:
            if not checkbox_element.is_selected():
                checkbox_element.click()
        time.sleep(3)

        # Define the CSS selector for the "Print Selected" button
        print_button_selector = "button[data-action='nadmin--macpos--orders#generateBulkPDF']"
        # Wait for the "Print Selected" button to become visible and interactable
        self.wait_for_element_visible(print_button_selector)
        # Click on the "Print Selected" button
        self.click(print_button_selector)
        # Optionally wait for some time for the PDF generation to complete
        time.sleep(4)
        
    def sort_reference(self):
        reference_header_css = 'th[aria-label="Reference: activate to sort column ascending"]'
        # Wait for the "Ordered At" header to become clickable
        self.wait_for_element_visible(reference_header_css)
        # Click on the "Ordered At" header to sort the table
        self.click(reference_header_css)
        time.sleep(4)
        
    def sort_ordered_at(self):
        # Define the CSS selector for the "Ordered At" header
        ordered_header_css = 'th[aria-label="Ordered At: activate to sort column ascending"]'
        # Wait for the "Ordered At" header to become clickable
        self.wait_for_element_visible(ordered_header_css)
        # Click on the "Ordered At" header to sort the table
        self.click(ordered_header_css)
        time.sleep(4)
        
    def sort_amount(self):
        amount_header_css = 'th[aria-label="Amount: activate to sort column ascending"]'
        # Wait for the "Ordered At" header to become clickable
        self.wait_for_element_visible(amount_header_css)
        # Click on the "Ordered At" header to sort the table
        self.click(amount_header_css)
        time.sleep(4)
        
    def sort_items(self):
        items_header_css = 'th[aria-label="Items: activate to sort column ascending"]'
        # Wait for the "Ordered At" header to become clickable
        self.wait_for_element_visible(items_header_css)
        # Click on the "Ordered At" header to sort the table
        self.click(items_header_css)
        time.sleep(4)
        
    def search_store(self):
        search_input_selector = "#macpos-orders_filter input[type='search']"
        # Wait for the search input field to become visible and interactable
        self.wait_for_element_visible(search_input_selector)
        # Find the search input element
        search_input = self.find_element(search_input_selector)
        # Clear any existing text in the search input field
        search_input.clear()
        # Enter the search query "Juan's Store" into the input field
        search_input.send_keys("Juan's Store")
        time.sleep(4)