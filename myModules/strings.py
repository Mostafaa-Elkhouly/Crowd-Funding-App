#! /usr/bin/python3

def read_valid_string_input(promptMsg):
    while True:
        user_input = input(promptMsg).strip().lower()
        
        # Check if the input contains only characters
        if user_input.isalpha():
            return user_input
        else:
            print("\033[31m" + "please enter a valid string containing only characters." + "\033[0m")


def read_string_with_spaces(promptMsg):
    while True:
        user_input = input(promptMsg).strip().lower()
        
        if len(user_input) > 0:
            # Check if the input contains only characters
            if all(char.isalpha() or char.isspace() for char in user_input):
                return user_input
            else:
                print("\033[31m" + "please enter a valid string containing only characters." + "\033[0m")
        else:
            print("\033[31m" + "String Must be not Empty." + "\033[0m")