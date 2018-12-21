"""
IdentityGenerator.py by Anthony Lee
v1.3
Last updated: 20 Dec 2018

This script allows you to randomly generate an identity for anonomyous account
across various platforms / services.
"""

import random
import string
from six.moves import input as raw_input # to maintain usability between Python 2 and 3
import os # for text centering

# TO DO:
# 1. CENTER THE TEXT APPROPRIATELY FOR UI
# 2. MODULARIZE CODE INTO FUNCTIONS
# 3. CODE CLEAN UP
# 4. STREAMLINE THE 'CENTERING' CODE

# variable declarations
FEATURES_LIST = [" - Gender", " - Password", " - Email Domain", " - Birthday"]
HEADER_BLOCK = "// ================================================================================ //"
OS_WIDTH = os.get_terminal_size().columns
# identity function
GENDER_LIST = ["M", "F"]
GENDER = GENDER_LIST[random.randint(0, len(GENDER_LIST)-1)]

# password function
YES = {"yes", "y", ""}
NO = {"no", "n"}

# PROGRAM FIRST OUTPUT. CENTER THIS. ALSO START MODULARIZING CODE BY PLACING THEM INTO FUNCTIONS
print(" ")
print((HEADER_BLOCK.center(OS_WIDTH))) # text centering is working
print((HEADER_BLOCK.center(OS_WIDTH)))
print(" ")
print(("Welcome to the Random Identity Generator!").center(OS_WIDTH))
print(("Here we can randomly generate an identity for you for ease of account creation.").center(OS_WIDTH))
print(("This includes the following:").center(OS_WIDTH))
print(" ")
for item in range(len(FEATURES_LIST)):
    print((FEATURES_LIST[item]).center(OS_WIDTH))
# print(('\n'.join(map(str, FEATURES_LIST))))
print(" ")
print((HEADER_BLOCK.center(OS_WIDTH)))
print((HEADER_BLOCK.center(OS_WIDTH)))
print(" ")

print(" ")
print((HEADER_BLOCK.center(OS_WIDTH)))
print(("Input: ").center(OS_WIDTH))
print((HEADER_BLOCK.center(OS_WIDTH)))
print(" ")
PASS_LENGTH = input(" >>> Enter desired password length: ")
INT_PASS_LENGTH = int(PASS_LENGTH)

# CANNOT CENTER THE INPUT QUESTION
print(" ")
print("By default, password generated will allow inclusion of special characters.")
SPECIAL_CHAR_STATUS = input(" >>> Allow special characters (punctuation) in password? [Y / N]: ").lower()
if SPECIAL_CHAR_STATUS in YES:
    SPECIAL_CHAR_STATUS = True
elif SPECIAL_CHAR_STATUS in NO:
    SPECIAL_CHAR_STATUS = False
else:
    print("Please input Y or N <case insensitive>")

if SPECIAL_CHAR_STATUS:
    PASSWORD = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(INT_PASS_LENGTH))
else:
    PASSWORD = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(INT_PASS_LENGTH))

# email function
# selfnote: sharklasers, guerillamail, mailinator, index.net = tempmailaddress.com
DOMAIN_LIST = ["sharklasers.com", "guerillamail.info", "grr.la", "guerillamail.com", "guerillamail.net", "guerillamail.org", "pokemail.net", "spam4.me", "mailinator.com", "index.net"]
DOMAIN = DOMAIN_LIST[random.randint(0, len(DOMAIN_LIST)-1)]

# birthday function
YEAR = str(random.randint(1990, 2001))
MONTH = str(random.randint(1, 12))
if MONTH in (1, 3, 5, 7, 8, 10, 12):
    DAY = str(random.randint(1, 31))
elif MONTH in (4, 6, 9, 11):
    DAY = str(random.randint(1, 30))
else:
    DAY = str(random.randint(1, 28))

print(" ")
print((HEADER_BLOCK.center(OS_WIDTH)))
print(("Output:").center(OS_WIDTH))
print((HEADER_BLOCK.center(OS_WIDTH)))
print(" ")

# print('{: >20}'.format('test'))
# FIGURE OUT HOW TO CHANGE PADDING FOR LEFT ALIGN; CENTERING LOOKS UGLY
print("{:<50}".format("GENDER: " + GENDER))
print("{:<50}".format("EMAIL DOMAIN: " + DOMAIN))
print("{:<50}".format("PASSWORD: " + PASSWORD))
print("{:<50}".format("BIRTHDAY: " + YEAR + "-" + MONTH + "-" + DAY))
print(" ")

print((HEADER_BLOCK.center(OS_WIDTH)))
# print(" ")
print(("End of Program").center(OS_WIDTH))
# print(" ")
print((HEADER_BLOCK.center(OS_WIDTH)))
# print(string.punctuation
