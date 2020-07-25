"""
ProductivityTimer.py by Anthony Lee
v2.2
Last updated: 25 Jun 2020

This script serves as a timer to facilitate productivity; it does so by
tracking specified work periods and break times, notifying users of their respective
starts and stops.
"""
import sys
import string
import time
from time import sleep

# TODO:
# 1. modularize code into FUNCTIONS
# 2. add ability to loop program a number of times
# 3. improve UI

sysArg = sys.argv
len_sysArg = len(sys.argv)
unit_word = " minutes"
default_unit = unit_word

# argument length check
if len_sysArg != 3:
    print("\n>> Usage: [ python3 ] Productivity_Timer.py study_minutes break_minutes")
    print(">> Example: [ python3 ] Productivity_Timer.py 30 10\n")
    print(">> Use a value of 0 minutes for testing the alarm immediately.")
    print(">> Boops a few times after the duration is over.")
    print(">> Press Ctrl-C to terminate the alarm clock early.\n")
    print(">> Studies suggests maximum productivity can be achieved with :")
    print(">> ~52 minute work intervals and ~17 minute breaks\n")
    print(">> Now exiting...")
    sys.exit(1)

# check argument type
try:
    study_minutes = int(sysArg[1])
    break_minutes = int(sysArg[2])

    if study_minutes < 0 or break_minutes < 0:
        raise ValueError("Int <= 0")
except ValueError:
    print("\n>> Invalid numeric value for minutes")
    print(">> Should be an integer >= 0\n")
    print(">> Now exiting...")
    sys.exit(1)

def reset_unit():
    global unit_word
    unit_word = default_unit

try:
    if study_minutes > 0:
        print("\nBreak time will be in " + str(study_minutes) + unit_word + "! Time to work c:")
        while study_minutes != 0:
            if study_minutes == 1:
                unit_word = " minute"
            print("\n")
            print(" ~ " + str(study_minutes) + unit_word + " left before break ~")
            time.sleep(60)
            study_minutes -= 1

    for i in range(5):
        print(chr(7))
        sleep(1)

    print("\nBreak time! :D\n")
    reset_unit()

    if break_minutes > 0:
        print("\nEnjoy your break :D You gotta head back to work in " + str(break_minutes) + unit_word)
        while break_minutes != 0:
            if break_minutes == 1:
                unit_word = " minute"
            print("\n")
            print(" ~ " + str(break_minutes) + unit_word + " of break left ~")
            time.sleep(60)
            break_minutes -= 1

    for i in range(5):
        print(chr(7))
        sleep(1)

    print("\nBreak's over! Back to work O:\n")

    print(">> To continue, run the program again\n")
    print(">> Now exiting...")

except KeyboardInterrupt:
    print("\n\nHey man, why you getting distracted D:\n")
    print(">> Now exiting...")
    sys.exit(1)
