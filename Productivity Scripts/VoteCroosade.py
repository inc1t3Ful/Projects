"""
VoteCroosade.py by Anthony Lee
v1.0
Last updated: 26 Dec 2018

This script serves to automate the voting process for CroosadeMS v100, a
Maplestory private server
"""
# import webbrowser as wb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import logging

# Note: Place script in same directory as ChromeWebdriver or vice versa;
# Edit the path as necessary
driver = webdriver.Chrome("/filepath/chromedriver")

# Note: Input your login credentials here
username = "username"
password = "password"

# driver.switch_to_window(window_name) # need to find window name
# using driver.get() refreshes the page instance, removing logins
# print(driver.assertTrue("https://www.croosade.com/vote", currURL)) # assert is not working atm

## Navigate to Croosade main site
print("")
print(">> Navigating to Croosade site")
driver.get("https://croosade.com/")
print("")
print("Ensuring page loads...")
print("")
time.sleep(1)

## Access drop down menu and click login
print(">> Clicking Drop down menu")
dropDownAccountButton = driver.find_element_by_link_text("Account")
dropDownAccountButton.click()
print(">> Clicking Sign In")
signInButton = driver.find_element_by_link_text("Sign in")
signInButton.click()

print("")
print("Ensuring page loads...")
print("")
time.sleep(1)

## Enter login credentials
print("Currently on: << " + driver.current_url + " >>")
print(">> Inputting username and password")
print(">> Username: " + username)
print(">> Password: " + password)
# Wait for login fields to be located before attempting to input
usernameField = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'inputUsername')))
passwordField = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'inputPassword')))
usernameField.send_keys(username)
passwordField.send_keys(password)
submitLogin = driver.find_element_by_css_selector("#formLogin > button")
submitLogin.click()
print("")
print("Logging in...")

print("")
print("Ensuring page loads...")
print("")
time.sleep(2)

## On Dashboard panel, go to voting panel
print("Currently on: << " + driver.current_url + " >>")
print(">> Clicking Vote for NX")
voteForNX = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[2]/a")
voteForNX.click()

print("")
print("Ensuring page loads...")
print("")
time.sleep(2)

## Vote for Gtop100
# by default, Gtop100 is already selected ; do not need to select dropdown menu
print("Currently on: << " + driver.current_url + " >>")
print(">> Voting for Gtop100")
voteButton = driver.find_element_by_css_selector("#formVote > button")
voteButton.click()
# print("Currently on: << " + driver.current_url + " >>")
driver.switch_to_window(driver.window_handles[0])
# print("Currently on: << " + driver.current_url + " >>")
time.sleep(1)

## Vote for XtremeTop100
print(">> Voting for XtremeTop100")
selectTopList = driver.find_element_by_id("selectToplist")
selectOption2 = driver.find_element_by_css_selector("#selectToplist > option:nth-child(2)")
selectTopList.click()
selectOption2.click()
time.sleep(1)
voteButton.click()
# print("Currently on: << " + driver.current_url + " >>")
driver.switch_to_window(driver.window_handles[0])
# print("Currently on: << " + driver.current_url + " >>")
time.sleep(1)

## Vote for TopG
print(">> Voting for TopG")
selectOption3 = driver.find_element_by_css_selector("#selectToplist > option:nth-child(3)")
selectTopList.click()
selectOption3.click()
time.sleep(1)
voteButton.click()
# print("Currently on: << " + driver.current_url + " >>")
driver.switch_to_window(driver.window_handles[0])
# print("Currently on: << " + driver.current_url + " >>")

print("")
print("Ensuring page loads...")
print("")
time.sleep(3)
# print("Closing tab...")
# driver.close()
print("Closing window...")
driver.quit() # this closes the entire window
