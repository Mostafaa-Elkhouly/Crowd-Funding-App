#! /usr/bin/python3

import myModules as md


fname = md.read_valid_string_input("Enter Your First Name: ")
lname = md.read_valid_string_input("Enter Your Last Name: ")
email = md.read_valid_email("Enter Your Email Address: ")
password = md.read_valid_password("Enter Your Password: ")

if md.confirm_password("Confirm Your New Password: ", password):
    print("\033[32m" + "Password confirmed successfully." + "\033[0m")

else:
    print("\033[31m" + "Password confirmation failed." + "\033[0m")
        
    password = md.read_valid_password("Please enter your password again: ")
    md.confirm_password("Confirm Your New Password: ", password)








mobNumber = ""

userinfo = {
    "fname":fname,
    "lname":lname,
    "email":email,
    "passord":password,
    "mobile":mobNumber
}

md.write_data(userinfo)

