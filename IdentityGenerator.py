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
year = random.randint(1990, 2001)
month = random.randint(1, 12)
day = random.randint(1, 31)

print(" ")
print("Gender: ", gender)
print("Password: ", password)
print("Email: ", email)
print("Birthday: ", year, month, day)
print(" ")
