"""
IdentityGenerator.py by Anthony Lee
v2.0.1
Last updated: 21 Dec 2018

This script allows you to randomly generate an identity for anonomyous account
creation across various platforms / services.
"""

import random
import string
from six.moves import input as raw_input # to maintain usability between Python 2 and 3
import os # for text centering

### Variable declarations ###
FEATURES_LIST = [" - Gender", " - Password", " - Email Domain", " - Birthday"]
HEADER_BLOCK = "// ================================================================================ //"
OS_WIDTH = os.get_terminal_size().columns

GENDER_LIST = ["M", "F"]

YES = ["yes", "y", ""]
NO = ["no", "n"]

DOMAIN_LIST = ["sharklasers.com", "guerillamail.info", "grr.la",
            "guerillamail.com", "guerillamail.net", "guerillamail.org",
            "pokemail.net", "spam4.me", "mailinator.com", "index.net"]

MONTH_31 = [1, 3, 5, 7, 8, 10, 12]
MONTH_30 = [4, 6, 9, 11]
YEAR = str(0)
MONTH = str(0)
DAY = str(0)


### Functions ###
# prints features of this program
def PRINT_FEATURES(FEATURES_LIST):
    for item in range(len(FEATURES_LIST)):
        print(("{:<15}".format(FEATURES_LIST[item])).center(OS_WIDTH))

# returns random gender
def DECIDE_GENDER():
    GENDER = GENDER_LIST[random.randint(0, len(GENDER_LIST)-1)]
    return GENDER

# returns random email domain
def DECIDE_EMAIL():
    DOMAIN = DOMAIN_LIST[random.randint(0, len(DOMAIN_LIST)-1)]
    return DOMAIN

# returns integer version of PASS_LENGTH
def DECIDE_PASS_LENGTH(PASS_LENGTH):
    INT_PASS_LENGTH = int(PASS_LENGTH)
    return INT_PASS_LENGTH

# requests input to allow/ disallow special char in PASSWORD; raises flag
def DECIDE_PASS_SPECIAL():
    print(" ")
    SPECIAL_CHAR_STATUS = input(" >>> Allow special characters (punctuation) in password? [Y / N]: ".center(OS_WIDTH)).lower()
    if SPECIAL_CHAR_STATUS in YES:
        SPECIAL_CHAR_STATUS = True
        return SPECIAL_CHAR_STATUS
    elif SPECIAL_CHAR_STATUS in NO:
        SPECIAL_CHAR_STATUS = False
        return SPECIAL_CHAR_STATUS
    else:
        print(" ")
        print(("ERROR: Please input Y or N < case insensitive >").center(OS_WIDTH))
        DECIDE_PASS_SPECIAL()

# takes special char flag and password length parameter as rules for generating PASSWORD
def DECIDE_PASS(SPECIAL_CHAR_STATUS, INT_PASS_LENGTH):
    if SPECIAL_CHAR_STATUS:
        PASSWORD = ''.join(random.SystemRandom().choice(string.ascii_letters
                    + string.digits
                    + string.punctuation) for _ in range(INT_PASS_LENGTH))
        return PASSWORD
    else:
        PASSWORD = ''.join(random.SystemRandom().choice(string.ascii_letters
                    + string.digits) for _ in range(INT_PASS_LENGTH))
        return PASSWORD

def DECIDE_YEAR():
    YEAR = str(random.randint(1990, 2001))
    return YEAR

def DECIDE_MONTH():
    MONTH = str(random.randint(1, 12))
    return MONTH

def DECIDE_DAY(MONTH):
    if MONTH in MONTH_31:
        DAY = str(random.randint(1, 31))
    elif MONTH in MONTH_30:
        DAY = str(random.randint(1, 30))
    else:
        DAY = str(random.randint(1, 28))

    return DAY

def PRINT_OUTPUT():
    print(("{:<35}".format("GENDER: " + DECIDE_GENDER())).center(OS_WIDTH))
    print(("{:<35}".format("EMAIL DOMAIN: " + DECIDE_EMAIL())).center(OS_WIDTH))
    print(("{:<35}".format("PASSWORD: " + DECIDE_PASS(SPECIAL_CHAR_STATUS, INT_PASS_LENGTH))).center(OS_WIDTH))
    print(("{:<35}".format("BIRTHDAY: " + DECIDE_YEAR() + "-" + DECIDE_MONTH() + "-" + DECIDE_DAY(DECIDE_MONTH()))).center(OS_WIDTH))
    print(" ")

### PROGRAM FLOW ###
# start program block header
print(" ")
print((HEADER_BLOCK.center(OS_WIDTH)))
print(("Start of Program").center(OS_WIDTH))
print((HEADER_BLOCK.center(OS_WIDTH)))
print(" ")
print(("Welcome to the Random Identity Generator!").center(OS_WIDTH))
print(("Here we can randomly generate an identity for you for ease of account creation.").center(OS_WIDTH))
print(("This includes the following:").center(OS_WIDTH))
PRINT_FEATURES(FEATURES_LIST)
print(" ")

# input block header
print(" ")
print((HEADER_BLOCK.center(OS_WIDTH)))
print(("Input: ").center(OS_WIDTH))
print((HEADER_BLOCK.center(OS_WIDTH)))
print(" ")

# take input
# note to self: all other functions are ran at PRINT_OUTPUT()
# this is because they are static return functions; password function calls for
# multiple inputs and passing of variables, so input inquiry is separated from
# decider logic
PASS_LENGTH = input(" >>> Enter desired password length: ".center(OS_WIDTH))
INT_PASS_LENGTH = DECIDE_PASS_LENGTH(PASS_LENGTH)
print(" ")
print(("By default, password generated will allow inclusion of special characters.").center(OS_WIDTH))
SPECIAL_CHAR_STATUS = DECIDE_PASS_SPECIAL()

# output block header
print(" ")
print((HEADER_BLOCK.center(OS_WIDTH)))
print(("Output:").center(OS_WIDTH))
print((HEADER_BLOCK.center(OS_WIDTH)))
print(" ")

PRINT_OUTPUT()

# eof block header
print((HEADER_BLOCK.center(OS_WIDTH)))
print(("End of Program").center(OS_WIDTH))
print((HEADER_BLOCK.center(OS_WIDTH)))
