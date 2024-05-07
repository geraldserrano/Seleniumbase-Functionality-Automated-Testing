from login import LoginUtility
from orders_element import ElementUtility
from orders_assertion import AssertionUtility
import time


class TestDashboard(LoginUtility, ElementUtility, AssertionUtility):
    def test_access_orders_page(self):
        self.login_to_nadmin("intern_gerald", "gerald")  # Use actual credentials
        
        # Click Transsactions
        self.click_transactions_button()
        
        # click Orders
        #self.click_orders_button()
        self.wait_for_element_visible("xpath", "//a[@data-sidebars-target='menu' and @href='/nadmin/macpos/orders']")
        self.click("xpath", "//a[@data-sidebars-target='menu' and @href='/nadmin/macpos/orders']")
        time.sleep(4)
        
        self.set_date()
        
        # Click the first reference number  
        self.click_reference()
    
        current_window = self.driver.current_window_handle

        # Click pdf button
        self.click_pdf_button()
        # Assert that the PDF opened in a new tab
        self.assert_pdf_opened_in_new_tab() 
        self.switch_to_window(current_window)
        time.sleep(2)

        # click picklist
        self.click_picklist_button()
        # Assert that the Picklist opened in a new tab
        self.assert_picklist_opened_in_new_tab()
        self.switch_to_window(current_window)
        time.sleep(2)
        
        # Click Invoices
        self.click_invoices_button()
        # Assert that the Picklist opened in a new tab
        self.assert_invoices_opened_in_new_tab()
        self.switch_to_window(current_window)
        time.sleep(2) """
        
        self.click_delivery_button()
        # Assert the presence of the Action input field in the form
        self.assert_action_input_present()
        
        # Input the delivery status "in transit"
        self.input_delivery_status("in transit")   
        # Assert that the status is displayed as "in transit"
        self.assert_delivery_status_displayed()
        
        # Click the <a> element containing the text "Orders" using XPath
        self.click_orders_button()
        
        # Click other reference
        self.click_order_by_reference_number("HELI-1-57")
        
        # Click Void
        self.click_void()
        self.assert_void()
        
        # # test void form
        self.input_void_form()
        
        self.click_orders_button()
        self.click_voided_ref("J2-1-2")
        self.assert_void_form()
        
