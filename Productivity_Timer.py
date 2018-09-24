import sys
import string
import time
from time import sleep

sa = sys.argv
lsa = len(sys.argv)

# argument length check
if lsa != 2:
    print " "
    print ">> Usage: [ python ] Productivity_Timer.py duration_in_minutes"
    print ">> Example: [ python ] Productivity_Timer.py 10 <<"
    print " "
    print ">> Use a value of 0 minutes for testing the alarm immediately."
    print ">> Boops a few times after the duration is over."
    print ">> Press Ctrl-C to terminate the alarm clock early."
    print " "
    print ">> Studies suggests maximum productivity can be achieved with :"
    print ">> ~52 minute work intervals and ~17 minute breaks "
    print " "
    print ">> Now exiting..."
    sys.exit(1)

# check argument type
try:
    minutes = int(sa[1])
except ValueError:
    print " "
    print ">> Invalid numeric value (%s) for minutes" % sa[1]
    print ">> Should be an integer >= 0"
    print " "
    print ">> Now exiting..."
    sys.exit(1)

if minutes < 0:
    print " "
    print ">> Invalid value for minutes, should be >= 0"
    print " "
    print ">> Now exiting..."
    sys.exit(1)

# unit measurment variable
if minutes == 1:
    unit_word = " minute"
else:
    unit_word = " minutes"

# run timer. update every minute, notify when time up
try:
    if minutes > 0:
        print " "
        print "Break time will be in " + str(minutes) + unit_word + "! Time to work c:"
        while minutes != 0:
            print " "
            print " ~ " + str(minutes) + unit_word + " left before break ~"
            time.sleep(60)
            minutes -= 1
    for i in range(5):
        print chr(7),
        sleep(1)
    print " "
    print "Break time! :D"
    print " "
    print ">> Now exiting..."

# turn off timer
except KeyboardInterrupt:
    print " "
    print " "
    print "Hey man, why you getting distracted D:"
    print " "
    print ">> Now exiting..."
    sys.exit(1)
