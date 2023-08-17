#! /usr/bin/python3

import re

def read_valid_email(promptMsg):
    
    print("\033[33m" + "Email Address should by something like: ___@___.___ " + "\033[0m")
    print("\033[33m" + "use can only write characters and number" + "\033[0m")
    print("\033[33m" + "Don't use any special character except . or _" + "\033[0m")

    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]+$'

    while True:

        email = input(promptMsg).strip().lower()

        if re.match(pattern, email) is not None:
            return True
        else:
            print("\033[31m" + "please enter a valid string containing only characters." + "\033[0m")

