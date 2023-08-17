#! /usr/bin/python3

import os
from tabulate import tabulate
import registration as r
import login as l

table = [
    ["Press 1","To Register For New Account"],
    ["Press 2","If Have Already Existing Account"]
    ]

while True:
    val = input(tabulate(table) + "\n" + "Your choose: ")

    try:
        integer_value = int(val)
        if integer_value == 1:
            os.system('clear')
            r.register_user()
        elif integer_value == 2:
            os.system('clear')
            l.login_user()
        else:
            raise ValueError

        break  
    except ValueError:
        print("\033[31m" + "Invalid input. Please enter an integer." + "\033[0m")
