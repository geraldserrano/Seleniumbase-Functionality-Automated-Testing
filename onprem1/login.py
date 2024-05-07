from seleniumbase import BaseCase

class LoginUtility(BaseCase):
    def login_to_nadmin(self, username, password):
        # Open the login page
        self.open("https://review.onprem-cloud.nweca.com/nadmin/sign_in") 
        
        # Fill the login form
        self.type("#floatingInput", username)
        self.type("#floatingPassword", password)
        
        # Submit the login form
        self.click('input[type="submit"][name="commit"]')
        self.maximize_window()
