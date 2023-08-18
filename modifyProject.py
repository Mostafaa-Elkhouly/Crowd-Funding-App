#! /usr/bin/python3

import myModules as md

def editProject(userEmail):

    project_info = md.read_project_data(userEmail)

    if len(project_info) > 0:

        project_title = md.read_string_with_spaces("Enter Title of The Project That You Want To Edit: ")
        
        for project in project_info["projects"]:

            if project["title"] == project_title:

                project.update("new_values")
            else: 
                print("\033[31m" + "No Projects Found With This Title, Try Again ..." + "\033[0m")

    else: 
        print("\033[34m" + "No Projects Found !!" + "\033[0m")
