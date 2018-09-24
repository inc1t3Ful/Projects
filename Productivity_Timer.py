# Productivity_Timer.py by Anthony Lee
# v1.0
# Last update: 23 Sep 2018

import sys
import string
import time
from time import sleep

sa = sys.argv
lsa = len(sys.argv)

# argument length check
if lsa != 3:
    print " "
    print ">> Usage: [ python ] Productivity_Timer.py study_minutes break_minutes"
    print ">> Example: [ python ] Productivity_Timer.py 30 10"
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
    study_minutes = int(sa[1])
    break_minutes = int(sa[2])
except ValueError:
    print " "
    print ">> Invalid numeric value (%s) for minutes" % sa[1] %sa[2]
    print ">> Should be an integer >= 0"
    print " "
    print ">> Now exiting..."
    sys.exit(1)

if study_minutes < 0 || break_minutes < 0:
    print " "
    print ">> Invalid value for minutes"
    print ">> Should be >= 0"
    print " "
    print ">> Now exiting..."
    sys.exit(1)

# unit measurment variable
if study_minutes == 1:
    unit_word = " minute"
else:
    unit_word = " minutes"

if break_minutes == 1:
    unit_word = " minute"
else:
    unit_word = " minutes"

# run timer. update every minute, boops when time up
try:
    # study timer
    if study_minutes > 0:
        print " "
        print "Break time will be in " + str(study_minutes) + unit_word + "! Time to work c:"
        while study_minutes != 0:
            print " "
            print " ~ " + str(study_minutes) + unit_word + " left before break ~"
            time.sleep(60)
            study_minutes -= 1
    for i in range(5):
        print chr(7),
        sleep(1)
    print " "
    print "Break time! :D"
    print " "

    # break timer WIP

    print ">> Now exiting..."

# manual override timer
except KeyboardInterrupt:
    print " "
    print " "
    print "Hey man, why you getting distracted D:"
    print " "
    print ">> Now exiting..."
    sys.exit(1)
