#! /usr/bin/python3

import re

def read_valid_password(promptMsg):

    print("\033[33m" + "Password length must be greater than 8 and less than 20" + "\033[0m")
    print("\033[33m" + "Password must contains at least one upper case letter" + "\033[0m")
    print("\033[33m" + "Password must contains at least one lower case letter" + "\033[0m")
    print("\033[33m" + "Password must contains at least one digit letter" + "\033[0m")
    print("\033[33m" + "Password must contains at least one special character" + "\033[0m")

    while True:

        password = input(promptMsg).strip()

        # Check if length is between 8 and 20 characters
        if len(password) < 8 or len(password) > 20:
            print("\033[31m" + "Password length must be between 8 and 20." + "\033[0m")
            continue
        
        # Check if it contains at least one uppercase letter
        if not any(char.isupper() for char in password):
            print("\033[31m" + "Password must contains at least one upper case letter." + "\033[0m")
            continue

        # Check if it contains at least one lowercase letter
        if not any(char.islower() for char in password):
            print("\033[31m" + "Password must contains at least one lower case letter" + "\033[0m")
            continue

        # Check if the password contains at least one digit
        if not any(char.isdigit() for char in password):
            print("\033[31m" + "Password must contains at least one digit letter" + "\033[0m")
            continue

        # Check if the password contains at least one special character
        if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\-]', password):
            print("\033[31m" + "Password must contains at least one special character" + "\033[0m")
            continue

        return password


def confirm_password(promptMsg, password):
    
    attemps = 3

    while attemps > 0:
        confirm_pass = input(promptMsg).strip()

        if password == confirm_pass:
            print("\033[32m" + "Password confirmed successfully." + "\033[0m")
            return True
        else:
            print("\033[31m" + f"You have {attemps-1} attemps left" + "\033[0m")
            print("\033[31m" + "Password not matched, please try again" + "\033[0m")
            attemps -= 1 
    
    return False
