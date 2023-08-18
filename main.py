#! /usr/bin/python3

from tabulate import tabulate
import myModules as md
from registration import register_user
from login import login
from projects import projectsMenu


print("---------------- Main Menu -----------------")

table = [
    ["Press 1","To Register: For New Account"],
    ["Press 2","To Login   : If You Already Have an Existing Account"],
    ["Press 0","To EXIT    !!!!!"]
    ]

while True:
    val = input(tabulate(table) + "\n" + "Your choose: ")

    try:
        integer_value = int(val)
        if integer_value == 1:
            md.clear_screen()
            register_user()
        elif integer_value == 2:
            md.clear_screen()
            userEmail = login()
            md.clear_screen()
            projectsMenu(userEmail)
        elif integer_value == 0:
            break
        else:
            raise ValueError
        
    except ValueError:
        print("\033[31m" + "Invalid input. Please enter an integer." + "\033[0m")
