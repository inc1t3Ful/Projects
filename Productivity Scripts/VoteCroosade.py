"""
VoteCroosade.py by Anthony Lee
v2.6
Last updated: 2 Aug 2019

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
line 61. DO NOT remove the quotation marks ("") or the "options = options"

5. Fill in login credentials as denoted on lines 64-65. DO NOT remove the
quotation marks ("")

6. Assuming you are in the same directory as your script, to run script:
    $ python3 VoteCroosade.py

#########################################################################
"""
import time
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

STARTTIME = time.time()

# Repetitive block to buffer page loading
# USAGE: x = seconds to sleep
def page_load_sleep(x):
    print("\nEnsuring page loads...\n")
    time.sleep(x)

# This locks loop to system clock; guaranteed run every x interval
# NOTE: sleep is in seconds (21630 seconds = 6 HR 30 S; Script runs ~15 SEC)
while True:
    # options = Options()
    # options.headless = True
    # NOTE: Place script in same directory as ChromeWebdriver or vice versa;
    # NOTE: EDIT PATH TO CHROMEDRIVER.EXE ON LINE BELOW
    DRIVER = webdriver.Chrome("/filepath/chromedriver")
    WINDOW1 = DRIVER.window_handles[0]

    # NOTE: INPUT LOGIN CREDENTIALS BELOW
    USERNAME = "username"
    PASSWORD = "password"

    print("\nCurrent time: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
    print(">> Navigating to Croosade site")
    DRIVER.get("https://croosade.com/")

    print(">> Clicking Drop down menu")
    dropDownAccountButton = WebDriverWait(DRIVER, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Account")))
    dropDownAccountButton.click()
    print(">> Clicking Sign In")
    signInButton = WebDriverWait(DRIVER, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
    signInButton.click()

    print("\nCurrently on: << " + DRIVER.current_url + " >>")
    print(">> Inputting username and password")
    print(">> Username: " + USERNAME)
    print(">> Password: " + PASSWORD)
    usernameField = WebDriverWait(DRIVER, 5).until(
        EC.presence_of_element_located((By.ID, "inputUsername")))
    passwordField = WebDriverWait(DRIVER, 5).until(
        EC.presence_of_element_located((By.ID, "inputPassword")))
    usernameField.send_keys(USERNAME)
    passwordField.send_keys(PASSWORD)
    submitLogin = DRIVER.find_element_by_css_selector("#formLogin > button")
    submitLogin.click()
    print("\nLogging in...")
    page_load_sleep(1)

    print("Currently on: << " + DRIVER.current_url + " >>")
    print(">> Clicking Vote for NX")
    currentNX = DRIVER.find_element_by_css_selector("body > div.minh-100 > div > div.row > div:nth-child(1) > div > div.card-body > p").text
    voteForNX = DRIVER.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[2]/a")
    voteForNX.click()
    page_load_sleep(1)

    print("Currently on: << " + DRIVER.current_url + " >>")
    print(">> Voting for Gtop100")
    selectTopList = DRIVER.find_element_by_id("selectToplist")
    voteButton = DRIVER.find_element_by_css_selector("#formVote > button")
    voteButton.click()
    DRIVER.switch_to.window(WINDOW1)

    print(">> Voting for XtremeTop100")
    selectOption2 = DRIVER.find_element_by_css_selector("#selectToplist > option:nth-child(2)")
    selectTopList.click()
    selectOption2.click()
    voteButton.click()
    DRIVER.switch_to.window(WINDOW1)

    print(">> Voting for TopG")
    selectOption3 = DRIVER.find_element_by_css_selector("#selectToplist > option:nth-child(3)")
    selectTopList.click()
    selectOption3.click()
    voteButton.click()
    DRIVER.switch_to.window(WINDOW1)
    page_load_sleep(1)

    print(">> Closing window")
    DRIVER.quit()

    ## Loop block
    newNXTotal = int(currentNX.replace(",", '')) + 4000
    print("\n<< CURRENT NX TOTAL: " + str(newNXTotal) + " >>")
    print("\nCurrent time: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
    print(">> Script will automatically rerun in ~ 6 hours\n")
    print("Please do not close your Command Prompt/ Terminal")
    print("To stop the program at any time, press CTRL + C")
    time.sleep(21630.0 - ((time.time() - STARTTIME) % 21630.0)) # DO NOT CHANGE TIME
