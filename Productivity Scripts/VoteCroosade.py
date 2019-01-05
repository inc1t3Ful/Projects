"""
VoteCroosade.py by Anthony Lee
v2.0
Last updated: 03 Jan 2019

#########################################################################
This script automates the voting process for CroosadeMS v100, a
Maplestory private server, and will automatically vote again every
reset period, which is 6 hours.

It leverages the site's lack of vote verification from the 3rd-party sites
and automates navigation to the main site, login, and the voting site
selections, avoiding all the CAPTCHAs.

#########################################################################
USAGE: ($ represents command-line arg)

1. If you do not have Selenium already installed, please run:
    $ pip install selenium

2. If you do not have Selenium Chrome Driver installed:
    https://sites.google.com/a/chromium.org/chromedriver/downloads

3. Extract 'chromedriver.exe' and place in any directory, preferably in the
same directory as this script

4. Note directory path and update it accordingly in this script as denoted on
line 61. DO NOT remove the quotation marks ("")

5. Fill in login credentials as denoted on lines 64-65. DO NOT remove the
quotation marks ("")

6. Assuming you are in the same directory as your script, to run script:
    $ python VoteCroosade.py

#########################################################################
"""
# import webbrowser as wb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

starttime = time.time()

# Repetitive block to buffer page loading
# USAGE: x = seconds to sleep
def pageLoadSleep(x):
    print("")
    print("Ensuring page loads...")
    print("")
    time.sleep(x)

# This locks loop to system clock; guaranteed run every x interval
# NOTE: sleep is in seconds (21900 seconds = 6 HR 5 MIN; Script runs ~30 SEC)
while True:
    # NOTE: Place script in same directory as ChromeWebdriver or vice versa;
    # NOTE: EDIT PATH TO CHROMEDRIVER.EXE ON LINE BELOW
    driver = webdriver.Chrome("/filepath/chromedriver")

    # NOTE: INPUT LOGIN CREDENTIALS BELOW
    username = "username"
    password = "password"

    ## Navigate to Croosade main site
    print("")
    print("Current time: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
    print(">> Navigating to Croosade site")
    driver.get("https://croosade.com/")
    pageLoadSleep(1)

    ## Access drop down menu and click login
    print(">> Clicking Drop down menu")
    dropDownAccountButton = driver.find_element_by_link_text("Account")
    dropDownAccountButton.click()
    print(">> Clicking Sign In")
    signInButton = driver.find_element_by_link_text("Sign in")
    signInButton.click()

    ## Enter login credentials
    print("")
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
    pageLoadSleep(1)

    ## On Dashboard panel, go to voting panel
    print("Currently on: << " + driver.current_url + " >>")
    print(">> Clicking Vote for NX")
    voteForNX = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[2]/a")
    voteForNX.click()
    pageLoadSleep(1)

    ## Vote for Gtop100
    # by default, Gtop100 is already selected ; do not need to select dropdown menu
    print("Currently on: << " + driver.current_url + " >>")
    print(">> Voting for Gtop100")
    voteButton = driver.find_element_by_css_selector("#formVote > button")
    voteButton.click()
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(1)

    ## Vote for XtremeTop100
    print(">> Voting for XtremeTop100")
    selectTopList = driver.find_element_by_id("selectToplist")
    selectOption2 = driver.find_element_by_css_selector("#selectToplist > option:nth-child(2)")
    selectTopList.click()
    selectOption2.click()
    voteButton.click()
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(1)

    ## Vote for TopG
    print(">> Voting for TopG")
    selectOption3 = driver.find_element_by_css_selector("#selectToplist > option:nth-child(3)")
    selectTopList.click()
    selectOption3.click()
    voteButton.click()
    driver.switch_to_window(driver.window_handles[0])
    pageLoadSleep(2)

    print(">> Closing window")
    driver.quit() # this closes the entire window/ driver instance

    ## Loop block
    print("")
    print("Current time: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
    print(">> Script will automatically rerun in ~ 6 hours")
    print("")
    print("Please do not close your Command Prompt/ Terminal")
    print("To stop the program at any time, press CTRL + C")
    time.sleep(21900.0 - ((time.time() - starttime) % 21900.0)) # DO NOT CHANGE TIME
