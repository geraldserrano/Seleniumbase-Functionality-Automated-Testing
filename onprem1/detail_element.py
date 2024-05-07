from selenium.webdriver.support.ui import Select
from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class DetailElements(BaseCase):
    def select_dropdown_by_value(self, selector, value):
        select_dropdown = Select(self.find_element(selector))
        select_dropdown.select_by_value(value)
        
    def click_transactions_button(self):
        self.wait_for_element_visible('a:contains("Transactions")')
        # Navigate to the Transactions and Orders page
        self.click('a:contains("Transactions")')
        time.sleep(4)
        
    def click_orders_button(self):
         self.wait_for_element_visible("xpath", "//a[@data-sidebars-target='menu' and @href='/nadmin/macpos/orders']")
         self.click("xpath", "//a[@data-sidebars-target='menu' and @href='/nadmin/macpos/orders']")
         time.sleep(4)
        
    def set_date(self):
        date_dropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'date')))
        ActionChains(self.driver).move_to_element(date_dropdown).click().perform()
        
        # Wait for the list of options to appear
        date_options = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//select[@id='date']/option")))

        # Iterate through each option and find "Custom"
        custom_option = None
        for option in date_options:
            if option.text == "Custom":
                custom_option = option
                break
        
        # If "Custom" option found, click on it
        if custom_option:
            custom_option.click()
            time.sleep(2)
            # Wait for the start date input field to be clickable
            start_date_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "start_date")))
            # Input start date as Apr 1, 2023
            start_date_input.send_keys("01-03-2023")
            time.sleep(4)
            # Wait for the end date input field to be clickable
            end_date_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "end_date")))
            # Input end date as Apr 01, 2024
            end_date_input.send_keys("01-03-2024")
            time.sleep(4)
        
    def click_reference(self):
        self.wait_for_element_visible("xpath", "//span[@class='fsc-9 me-1 badge badge-success']")
        reference_num = self.find_element("xpath", "//span[@class='fsc-9 me-1 badge badge-success']")
        reference_num.click()
        time.sleep(4)
        
    def click_pdf_button(self):
        self.wait_for_element_visible("xpath", "//span[@class='mt-3 material-icons' and text()='picture_as_pdf']")
        # Find and click the PDF link
        pdf_link = self.find_element("xpath", "//span[@class='mt-3 material-icons' and text()='picture_as_pdf']/ancestor::a")
        pdf_link.click()
        time.sleep(4)
        # Switch to the new tab
        self.switch_to_window(len(self.driver.window_handles) - 1)
        time.sleep(4)
        
    def click_picklist_button(self):
        self.wait_for_element_visible("xpath", "//span[@class='mt-3 material-icons' and text()='check_box']")
        # Find and click the Picklist link
        picklist_link = self.find_element("xpath", "//span[@class='mt-3 material-icons' and text()='check_box']/ancestor::a")
        picklist_link.click()
        time.sleep(4)
        # Switch to the new tab
        self.switch_to_window(len(self.driver.window_handles) - 1)
        time.sleep(4)
        
    def click_invoices_button(self):
        self.wait_for_element_visible("xpath", "//span[@class='mt-3 material-icons' and text()='point_of_sale']")
        # Find and click the Picklist link
        invoice_link = self.find_element("xpath", "//span[@class='mt-3 material-icons' and text()='point_of_sale']/ancestor::a")
        invoice_link.click()
        time.sleep(4)
        # Switch to the new tab
        self.switch_to_window(len(self.driver.window_handles) - 1)
        time.sleep(4)
        
    def click_delivery_button(self):
        time.sleep(4)
        self.wait_for_element_visible("xpath", "//span[@class='mt-3 material-icons' and text()='local_shipping']")
        delivery_link = self.find_element("xpath", "//span[@class='mt-3 material-icons' and text()='local_shipping']/ancestor::a")
        delivery_link.click()
        time.sleep(4)
   
    def input_delivery_status(self, status):
        self.wait_for_element_visible("xpath", "//*[@id='delivery-input']")
        action_input = self.find_element("xpath", "//*[@id='delivery-input']")
        action_input.clear() 
        action_input.send_keys(status)
        time.sleep(5)
        create_button = self.find_element("xpath", "//*[@id='appModalContent']/form/div[3]/input")
        create_button.click()
        time.sleep(4)
                
    def click_order_button(self):
        self.click("xpath", "/html/body/div[1]/div[2]/nav/ol/li[3]/a")
        time.sleep(4)
        
    def click_order_by_reference_number(self, reference_number):
       # Wait for the specific reference number element to be visible
        self.wait_for_element_visible("xpath", f"//span[@class='fsc-9 me-1 badge badge-success' and text()='{reference_number}']")
        # Scroll to the element before clicking
        self.scroll_to_element("xpath", f"//a[contains(@href, '/orders/') and .//span[@class='fsc-9 me-1 badge badge-success' and text()='{reference_number}']]")
        time.sleep(2)
        # Click the <a> element with the specific reference number using XPath
        self.click("xpath", f"//a[contains(@href, '/orders/') and .//span[@class='fsc-9 me-1 badge badge-success' and text()='{reference_number}']]")
        time.sleep(4)
        
    def click_voided_ref(self, reference_number):
        self.wait_for_element_visible("xpath", f"//span[@class='fsc-9 me-1 badge badge-danger' and text()='{reference_number}']")
        # Scroll to the element before clicking
        self.scroll_to_element("xpath", f"//a[contains(@href, '/orders/') and .//span[@class='fsc-9 me-1 badge badge-danger' and text()='{reference_number}']]")
        time.sleep(2)
        # Click the <a> element with the specific reference number using XPath
        self.click("xpath", f"//a[contains(@href, '/orders/') and .//span[@class='fsc-9 me-1 badge badge-danger' and text()='{reference_number}']]")
        time.sleep(4)
        
    def click_void(self):
        self.wait_for_element_visible("xpath", "//button[contains(@class, 'btn-danger') and contains(@class, 'ms-1') and contains(span/@class, 'material-icons') and span[contains(text(), 'block')]]")
        self.click("xpath", "//button[contains(@class, 'btn-danger') and contains(@class, 'ms-1') and contains(span/@class, 'material-icons') and span[contains(text(), 'block')]]")
        time.sleep(4)

    def input_void_form(self):
        textarea_xpath = '/html/body/div[3]/div/div/form/div[2]/div[1]/textarea'
        # Wait for the textarea element to be visible and interactable
        self.wait_for_element_visible(textarea_xpath)
        # Input new text into the textarea
        new_text = "This is a test message for the textarea"
        self.type(textarea_xpath, new_text)
        # Wait for the button to be visible and interactable
        button_xpath = '//*[@id="appModalContent"]/form/div[3]/input'
        self.wait_for_element_visible(button_xpath)
        # Click the button to submit the form
        self.click(button_xpath)
        time.sleep(4)
