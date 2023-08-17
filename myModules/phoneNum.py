#! /usr/bin/python3

import re

def read_valid_egyptian_mobile_number(promptMsg):
    
    # Check if the phone number matches the Egyptian mobile number pattern
    pattern = r'^(010|011|012|015|016)\d{8}$'

    while True:

        phone_number = input(promptMsg).strip()

        if re.match(pattern, phone_number) is not None:
            return phone_number
        else:
            print("\033[31m" + "Invalid egyptian mobile number." + "\033[0m")