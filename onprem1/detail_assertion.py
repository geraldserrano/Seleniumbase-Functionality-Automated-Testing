from seleniumbase import BaseCase
from selenium.webdriver.common.by import By

import time

class DetailAssertions(BaseCase):
    def assert_pdf_opened_in_new_tab(self):
        assert ".pdf" in self.get_current_url(), "PDF file did not open in a new tab"
        time.sleep(4)

    def assert_picklist_opened_in_new_tab(self):
        assert "/picklists/" in self.get_current_url(), "Picklist did not open in a new tab"
        time.sleep(4)
        
    def assert_invoices_opened_in_new_tab(self):
        assert "/invoices/" in self.get_current_url(), "Invoices did not open in a new tab"
        time.sleep(4)
        
    def assert_action_input_present(self):
        self.assert_element_present("xpath", "//*[@id='delivery-input']")
        time.sleep(3)
        
    def assert_delivery_status_displayed(self):
        # Assert the presence of "in transit" text within <span> element inside <td> element
        self.assert_element_present("xpath", "//td[.//span[contains(text(), 'in transit')]]"), "Text 'in transit' not found in <td> element"
        time.sleep(4)
        
    def assert_void(self):
        self.wait_for_element_visible("xpath", "//div[@class='modal-content']")
        assert self.is_element_present("xpath", "//textarea[@id='macpos_order_void_reason']"), "Void reason textarea not found"
        time.sleep(4)
        
    def assert_void_form(self):
        # Assert that the "Void" button is hidden
        void_button_locator = "//button[@class='btn btn-sm btn-danger ms-1']"
        self.wait_for_element_not_visible(void_button_locator, timeout=10)
        # Assert that the "Delivery" button is disabled
        delivery_button_locator = "//a[@data-nadmin--macpos--order-details-target='deliverybtn']"
        delivery_button = self.find_element(delivery_button_locator)
        # Check if the "disabled" class is present in the button's class attribute
        button_classes = delivery_button.get_attribute("class")
        assert "disabled" in button_classes, "Delivery button is not disabled"
        # Assert that the "VOIDED" text is displayed
        voided_text_locator = "//span[@class='badge badge-danger' and contains(text(), 'VOIDED')]"
        voided_text_element = self.driver.find_element(By.XPATH, voided_text_locator)
        assert voided_text_element.is_displayed(), "VOIDED text is not visible"