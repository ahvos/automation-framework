# Author: Ashley Vo
# File: test_login.py


#library imports
from playwright.sync_api import Page

'''
Test Case: verify user can log in successfully with valid credentials.
args:
    page - 

'''
def test_valid_login(page: Page):
    #navigate to browser login page of demo website
    page.goto("https://the-internet.herokuapp.com/login")

    page.fill("#username", "tomsmith")              #fills username input field using CSS selector
    page.fill("#password", "SuperSecretPassword!")  #fills password input field using CSS selector

    #selector finds and clicks button element that submits login form
    page.click("button[type='submit']")

    #verify that the success message appears after logging in
    #playwright's locater finds success text on page
    success_message = page.locator("text=You logged into a secure area!")

    #assert that the success message is visible, if false, test fails.
    assert success_message.is_visible()


def test_invalid_login(page: Page):
    #navigate to browser login page of demo website
    page.goto("https://the-internet.herokuapp.com/login")

    #wrong information
    page.fill("#username", "tommysmith")            #fills username input field using CSS selector
    page.fill("#password", "SecretPassword!")       #fills password input field using CSS selector

    #selector finds and clicks button element that submits login form
    page.click("button[type='submit']")

    #verify that the error message appears after logging in
    #playwright's locater finds error text on page
    error_message = page.locator("text=Your username is invalid!")

    #assert that the success message is visible, if false, test fails.
    assert error_message.is_visible()


