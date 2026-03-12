# Author: Ashley Vo
# File: test_login.py


#library imports
from playwright.sync_api import Page

#import object model
from framework.pages.login_page import LoginPage


'''
Function: test_valid_login
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

    #screenshot valid login
    page.screenshot(path="screenshots/valid_login_result.png")

    #verify success message appears
    assert page.get_by_text("You logged into a secure area!").is_visible()


'''
Function: test_invalid_login
Test Case: verify user cannot log in with invalid credentials.
Negative Path
'''
def test_invalid_login(page: Page):
    #create page object
    login_page = LoginPage(page)
    
    #navigate to browser login page of demo website
    login_page.open_browser()

    #performs login action: fill username and password, click login button
    login_page.perform_login("tommysmoth", "SecretPassword!")

    #screenshot invalid login
    page.screenshot(path="screenshots/invalid_login_result.png")

    #verify invalid message appears
    assert page.get_by_text("Your username is invalid").is_visible()


'''
Function: test_empty_username
Test Case: verify 
'''
def test_empty_username(page: Page):
    #create page object
    login_page = LoginPage(page)

    #navigate to browser login page of demo website
    login_page.open_browser()

    #perform login action with empty username
    login_page.perform_login("", "SuperSecretPassword!")
    
    #screenshot login with empty username
    page.screenshot(path="screenshots/empty_username_result.png")

    assert page.locator("#flash").is_visible()


'''
Function: test_empty_password
Test Case: verify 
'''
def test_empty_password(page: Page):
    #create page object
    login_page = LoginPage(page)

    #navigate to browser login page of demo website
    login_page.open_browser()

    #perform login action with empty username
    login_page.perform_login("tomsmith", "")
    
    #screenshot login with empty username
    page.screenshot(path="screenshots/empty_password_result.png")

    assert page.locator("#flash").is_visible()

