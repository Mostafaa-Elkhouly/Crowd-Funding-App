#! /usr/bin/python3

import re
import myModules as md

def is_email_taken(email, user_list):
    for user in user_list:
        if user["email"] == email:
            return True
    return False

def read_valid_email(promptMsg, status="registration"):
    
    if status == "registration":
        print("\033[33m" + "Email Address should by something like: ___@___.___ " + "\033[0m")
        print("\033[33m" + "use can only write characters and number" + "\033[0m")
        print("\033[33m" + "Don't use any special character except . or _" + "\033[0m")

    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]+$'
    
    try:
        user_list = md.read_all_data("users_info.json")

        while True:
            email = input(promptMsg).strip().lower()
            
            if status == "registration":
                if is_email_taken(email, user_list):
                    print("\033[31m" + "Email already taken. Please choose another." + "\033[0m")
                    continue

            if re.match(pattern, email) is not None:
                return email
            else:
                print("\033[31m" + "please enter a valid email address." + "\033[0m")
    except Exception as e:
        print("\033[31m"+ f"ERROR: {e}" + "\033[0m")
    