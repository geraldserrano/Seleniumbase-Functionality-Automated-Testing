from seleniumbase import BaseCase
import time

class LoginUtility(BaseCase):
    def login_to_nadmin(self, username, password):
        # Open the login page
        self.open("https://review.onprem-cloud.nweca.com/nadmin/sign_in") 
        
        # Fill the login form
        self.type("#floatingInput", username)
        time.sleep(3)
        self.type("#floatingPassword", password)
        time.sleep(3)
        
        # Submit the login form
        self.click('input[type="submit"][name="commit"]')
        self.maximize_window()
        
