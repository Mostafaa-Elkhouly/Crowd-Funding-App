#! /usr/bin/python3

import myModules as md


def createProject(userEmail):
    
    title = md.read_string_with_spaces("Enter Your Project Title: ")
    details = md.read_string_with_spaces("Enter Your Project Details: ")
    target = md.read_valid_number("Enter Your Project Total Target in EGP: ")
    startDate = md.read_valid_date("Enter The Start Date of Your Campaign: ")
    endDate = md.read_valid_date("Enter The End Date of Your Campaign: ")

    projectInfo = {
        "title":title,
        "details":details,
        "target":target,
        "startDate":startDate,
        "endDate":endDate
    }
    
    md.write_user_projects_data(userEmail, projectInfo)
    print("\033[32m" + f'Project With Title "{title}" Added successfully.' + "\033[0m")