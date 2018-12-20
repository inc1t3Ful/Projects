import random
import string

# identity function
GENDER_LIST = ["M", "F"]
GENDER = GENDER_LIST[random.randint(0, len(GENDER_LIST)-1)]

# password function
PASS_LENGTH = input("Length of password: ")
INT_PASS_LENGTH = int(PASS_LENGTH)
PASSWORD = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(INT_PASS_LENGTH))

# email function
# selfnote: sharklasers, guerillamail, mailinator, index.net = tempmailaddress.com
ADDRESSES = ["sharklasers.com", "guerillamail.info", "grr.la", "guerillamail.com", "guerillamail.net", "guerillamail.org", "pokemail.net", "spam4.me", "mailinator.com", "index.net"]
EMAIL = ADDRESSES[random.randint(0, len(ADDRESSES)-1)]

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
print "EMAIL: " + EMAIL
print "Birthday: " + YEAR + "-" + MONTH + "-" + DAY
print " "
