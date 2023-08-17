#! /usr/bin/python3

import myModules as md


fname = md.read_valid_string_input("Enter Your First Name: ")
lname = md.read_valid_string_input("Enter Your Last Name: ")
email = md.read_valid_email("Enter Your Email Address: ")
password = md.read_valid_password("Enter Your Password: ")
mobNumber = ""

userinfo = {
    "fname":fname,
    "lname":lname,
    "email":email,
    "passord":password,
    "mobile":mobNumber
}

md.write_data(userinfo)

