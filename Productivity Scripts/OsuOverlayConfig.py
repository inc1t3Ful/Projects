"""
1. Convert string input, separated by whitespace, to comma separated
2. Find duplicate key codes between 2 lists

Ex.
input: 0
input: 1 2 3 4
output: 1, 2, 3, 4

input: 1
input: 123,145,678
input: 123,456,789,asdf
output: {123}

Use case: Perform multiple services for Twitch Stream cam overlay setup in config
"""
import sys

def string_convert(input):
    if " " not in input:
        print("\nERROR: string does not include whitespace\n")
        sys.exit(1)

    string_comma = ', '.join(i for i in input.split(' '))
    return string_comma

def find_dupe(list1, list2):
    list1_converted = list(list1.split(","))
    list2_converted = list(list2.split(","))

    if type(list1_converted) is not list or type(list2_converted) is not list:
        print("\nERROR: input is not in list format\n")
        sys.exit(1)

    return set(list1_converted).intersection(list2_converted)

def service_select(choice_input):
    select_list = [0, 1]
    try:
        int(choice_input)
    except ValueError:
        print("\nValueError: Input is not an integer")
        sys.exit(1)

    choice_input_int = int(choice_input)

    if choice_input_int not in select_list:
        print("\nERROR: input is not a valid choice")

    if choice_input_int == 0:
        string_whitespace = input("\nPlease paste string of JavaScript event keycodes separated by whitespace: \n>> ")
        print(string_convert(string_whitespace))

    if choice_input_int == 1:
        print("\nPlease paste list of JavaScript event keycodes in comma-separated string format: Ex. 1,2,3\n")
        list1 = input("list1: >> ")
        list2 = input("list2: >> ")
        print("Duplicate elements: ", find_dupe(list1, list2))

print("\n")
print("0: Convert whitespace-separated string to comma-separated")
print("1: Find duplicate keycode in key1, key2 lists")
choice = input("\nPlease input # to select the service: \n>> ")
service_select(choice)
