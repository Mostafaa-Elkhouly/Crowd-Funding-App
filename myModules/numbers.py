#! /usr/bin/python3

def read_valid_number(promptMsg):
    while True:
        user_input = input(promptMsg).strip().lower()
        
        try:
            if user_input.isdigit():
                integer_value = int(user_input)
                return integer_value

        except ValueError:
            print("\033[31m" + "Invalid input. Please enter an integer." + "\033[0m")
