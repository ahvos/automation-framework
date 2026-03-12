# Author: Ashley Vo
# File: test_login.py


#library imports
from playwright.sync_api import Page

#import object model
from pages.login_page import LoginPage


'''
Test Case: verify user can log in successfully with valid credentials.
Positive Path
'''
def test_valid_login(page: Page):
    #create page object
    login_page = LoginPage(page)
    
    #navigate to browser login page of demo website
    login_page.open_browser()

    #performs login action: fill username and password, click login button
    login_page.perform_login("tomsmith", "SuperSecretPassword!")

    #verify success message appears
    assert page.locator("text=You logged into a secure area!").is_visible()

'''
Test Case: verify user can log in unsuccessfully with unvalid credentials.
Negative Path
'''
def test_invalid_login(page: Page):
    #create page object
    login_page = LoginPage(page)
    
    #navigate to browser login page of demo website
    login_page.open_browser()

    #performs login action: fill username and password, click login button
    login_page.perform_login("tommysmoth", "SecretPassword!")

    #verify success message appears
    assert page.locator("text=Your username is invalid").is_visible()


