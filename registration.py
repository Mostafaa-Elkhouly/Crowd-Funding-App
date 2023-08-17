#! /usr/bin/python3

import myModules as md

# ANSI escape codes for text color
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"

fname = md.read_valid_string_input("Enter Your First Name: ")
lname = md.read_valid_string_input("Enter Your Last Name: ")
