####
#Date & Time Printer
####
#Basic python code that prints date and time
#Completed by Anthony Lee
#from Unit2: "Strings and Console Output" on Codecademy

from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)