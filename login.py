#! /usr/bin/python3

import myModules as md


def login():

    print("---------------- Login Form -----------------")

    users = md.read_all_usersInfo()

    while True:
        email = md.read_valid_email("Enter Your Email Address: ", False)
        found = False
        
        for user in users:
            if user["email"] == email:
                found = True
                print(user)
                password = md.read_valid_password("Enter Your Password: ", False)
                
                if password == user["password"]:
                    print("\033[32m" + "Login successful!" + "\033[0m")
                    return
                else:
                    print("\033[31m" + "Incorrect password." + "\033[0m")
                    break
        if not found:
            print("\033[31m" + "User not found. Please re-enter your email." + "\033[0m")


