from login import LoginUtility
from detail_element import DetailElements
from detail_assertion import DetailAssertions
from order_element import OrderElements
from order_assertion import OrderAssertions
import time


class TestDashboard(LoginUtility, DetailElements, DetailAssertions, OrderElements, OrderAssertions):
    def test_access_orders_page(self):
        self.login_to_nadmin("intern_gerald", "gerald")  # Use actual credentials
        
        # Click Transsactions
        self.click_transactions_button()
        
        # click Orders
        self.click_orders_button()
        
        self.select_province()
        self.assert_select_province()
        
        self.select_city()
        self.assert_select_city()
        
        self.select_barangay()
        self.assert_select_barangay()
        
        self.select_date()
        self.assert_select_date()
        
        self.select_user()
        self.assert_select_user()
        
        self.verify_city()
        
        current_window = self.driver.current_window_handle
        
        self.print_selected()
        self.assert_pdf_opened_in_new_tab()
        self.switch_to_window(current_window)
        time.sleep(2)
        
        self.sort_reference()
        # self.assert_sort_reference()
        
        self.sort_ordered_at()
        self.assert_ordered_at()
        
        self.sort_amount()
        self.assert_sort_amount()
        
        self.sort_items()
        self.assert_sort_items()
        
        self.search_store()
        self.assert_search_store()
        
##############################################################

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
        time.sleep(2)
        
        self.click_delivery_button()
        # Assert the presence of the Action input field in the form
        self.assert_action_input_present()
        
        # Input the delivery status "in transit"
        self.input_delivery_status("in transit")   
        # Assert that the status is displayed as "in transit"
        self.assert_delivery_status_displayed()
        
        # Click the <a> element containing the text "Orders" using XPath
        self.click_order_button()
        
        # Click other reference
        self.click_order_by_reference_number("F-1-9")
        
        # Click Void
        self.click_void()
        self.assert_void()
        
        # # test void form
        self.input_void_form() 
                
        # self.click_orders_button()
        # self.click_voided_ref("J2-1-2")
        self.assert_void_form()
         