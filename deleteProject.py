#! /usr/bin/python3

import myModules as md

def delete_project_by_title(userEmail):

    md.clear_screen()
    print("---------------- Delete Project -----------------")

    user_Projects = md.read_project_data(userEmail)

    if len(user_Projects) > 0:

        project_title = md.read_string_with_spaces("Enter Title of The Project That You Want To Delete: ")

        Found = [project for project in user_Projects["projects"] if project["title"] == project_title]

        if Found:
            
            user_Projects["projects"] = [project for project in user_Projects["projects"] if project["title"] != project_title]

            md.update_user_projects_data(userEmail, user_Projects)
            print("\033[32m" + f'Project With Title "{project_title}" Deleted successfully.' + "\033[0m")
        
        else: 
            print("\033[31m" + "No Projects Found With This Title, Try Again ..." + "\033[0m")
    else: 
        print("\033[34m" + "No Projects Found !!" + "\033[0m")