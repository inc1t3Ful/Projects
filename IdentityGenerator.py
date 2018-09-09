import random
import string

# identity function
genderList = ["M" , "F"]
gender = genderList[random.randint(0, len(genderList)-1)]

# password function
passLength = input("Length of password: ")
x = int(passLength)
password = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(x))

# email function
# selfnote: sharklasers, guerillamail, mailinator, index.net = tempmailaddress.com
addresses = ["sharklasers.com", "guerillamail.info", "grr.la", "guerillamail.com", "guerillamail.net", "guerillamail.org", "pokemail.net", "spam4.me", "mailinator.com", "index.net"]
email = addresses[random.randint(0, len(addresses)-1)]

# birthday function
year = str(random.randint(1990, 2001))
month = str(random.randint(1, 12))
if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    day = str(random.randint(1, 31))
elif(month == 4 or month == 6 or month == 9 or month == 11):
    day = str(random.randint(1, 30))
else:
    day = str(random.randint(1, 28))

print(" ")
print("Gender: " + gender)
print("Password: " + password)
print("Email: " + email)
print("Birthday: " + year + "-" + month + "-" + day)
print(" ")
