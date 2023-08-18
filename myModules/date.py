#! /usr/bin/python3

import re


def read_valid_date(promptMsg):

    pattern = r'^\d{4}-\d{2}-\d{2}$'
    
    while True:
        date_input = input(promptMsg).strip().lower()

        if re.match(pattern, date_input) is not None:
                return date_input
        else:
            print("\033[31m" + "Invalid date format. Please use the format YYYY-MM-DD." + "\033[0m")
