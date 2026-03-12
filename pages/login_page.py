# Author: Ashley Vo
# File: login_page.py


#library imports
from playwright.sync_api import Page


'''
LoginPage Class: represents the Login Page of application.
'''
class LoginPage:
    #automatically called every time a new instance is created
    def __init__(self, page: Page):
        self.page = page    #initialize Playwright page instance
        
        self.username_input = page.locator("#username")     #username input field
        self.password_input = page.locator("#password")     #password input field
        
        self.login_button = page.locator("button[type='submit']")   #login button
        self.flash_msg = page.locator("#flash")                     #flash message show after login attempt


'''
Function: opens login page within browser.
'''
def open_browser(self):
    #go to url
    self.page.goto("https://the-internet.herokuapp.com/login")


'''
Function: get flash message shown after login attempt.
'''
def get_flash_msg(self):
    #extract and return text within an element without HTML tags
    return self.flash_msg.text_content()


'''
Function: performs login action.
'''
def perform_login(self, username: str, password: str):
    self.username_input.fill(username)      #fill in username field
    self.password_input.fill(password)      #fill in password field
    self.login_button.click()               #click login button
