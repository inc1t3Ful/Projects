import random
import string
from six.moves import input as raw_input # to maintain usability between Python 2 and 3
# import os ;; I WANT TO ADD TEXT CENTERING

# variable declarations
FEATURES_LIST = [" - Gender", " - Password", " - Email Domain", " - Birthday"]
# identity function
GENDER_LIST = ["M", "F"]
GENDER = GENDER_LIST[random.randint(0, len(GENDER_LIST)-1)]

# password function
YES = {"yes", "y", ""}
NO = {"no", "n"}

# PROGRAM FIRST OUTPUT. CENTER THIS. ALSO START MODULARIZING CODE BY PLACING THEM INTO FUNCTIONS
print " "
print "// ================================================================================ //"
print "Welcome to the Random Identity Generator!"
print "Here we can randomly generate an identity for you for ease of account creation. "
print "This includes the following: "
print ('\n'.join(map(str, FEATURES_LIST)))
print "// ================================================================================ //"

print " "
print "Let's begin!"
print " "
PASS_LENGTH = input(" >>> Enter desired password length: ")
INT_PASS_LENGTH = int(PASS_LENGTH)

print " "
print "By default, password generated will allow inclusion of special characters."
SPECIAL_CHAR_STATUS = raw_input(" >>> Allow special characters (punctuation) in password? [Y / N]: ").lower()
if SPECIAL_CHAR_STATUS in YES:
    SPECIAL_CHAR_STATUS = True
elif SPECIAL_CHAR_STATUS in NO:
    SPECIAL_CHAR_STATUS = False
else:
    print "Please input Y or N <case insensitive>"

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

print " "
print "GENDER: " + GENDER
print "PASSWORD: " + PASSWORD
print "EMAIL DOMAIN: " + DOMAIN
print "BIRTHDAY: " + YEAR + "-" + MONTH + "-" + DAY
print " "
# print string.punctuation
