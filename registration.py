#! /usr/bin/python3

import myModules as md


fname = md.read_valid_string_input("Enter Your First Name: ")
lname = md.read_valid_string_input("Enter Your Last Name: ")
email = md.read_valid_email("Enter Your Email Address: ")
password = md.read_valid_password("Enter Your Password: ")
checkTrue = md.confirm_password("Confirm Your New Password: ", password)

while not checkTrue:

    print("\033[31m" + "Password confirmation failed." + "\033[0m")   
    password = md.read_valid_password("Please enter your password again: ")
    if md.confirm_password("Confirm Your New Password: ", password) == True:
        break

mobNumber = md.read_valid_egyptian_mobile_number("Enter Your Mobile Number: ")

userinfo = {
    "fname":fname,
    "lname":lname,
    "email":email,
    "passord":password,
    "mobile":mobNumber
}

md.write_data(userinfo)

