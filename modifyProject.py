#! /usr/bin/python3

import myModules as md

def editProject(userEmail):

    md.clear_screen()
    print("---------------- Edit Project -----------------")

    user_Projects = md.read_project_data(userEmail)

    if len(user_Projects) > 0:

        project_title = md.read_string_with_spaces("Enter Title of The Project That You Want To Edit: ")

        for project in user_Projects["projects"]:

            if project["title"] == project_title:
                
                title = md.read_string_with_spaces("Enter a New Project Title: ")
                details = md.read_string_with_spaces("Enter New Project Details: ")
                target = md.read_valid_number("Enter New Project Total Target in EGP: ")
                startDate = md.read_valid_date("Enter New Start Date of Your Campaign: ")
                endDate = md.read_valid_date("Enter New End Date of Your Campaign: ")

                project["title"]= title
                project["details"]=details
                project["target"]=target
                project["startDate"]=startDate
                project["endDate"]=endDate

                md.update_user_projects_data(userEmail, user_Projects)
                print("\033[32m" + f"Project With Title {project_title} Updated successfully." + "\033[0m")
                break
        else: 
            print("\033[31m" + "No Projects Found With This Title, Try Again ..." + "\033[0m")
    else: 
        print("\033[34m" + "No Projects Found !!" + "\033[0m")
