#! /usr/bin/python3

def read_valid_string_input(promptMsg):
    while True:
        user_input = input(promptMsg).strip().lower()
        
        # Check if the input contains only characters
        if user_input.isalpha():
            return user_input
        else:
            print("\033[31m" + "please enter a valid string containing only characters." + "\033[0m")

