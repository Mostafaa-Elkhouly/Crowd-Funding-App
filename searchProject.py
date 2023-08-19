#! /usr/bin/python3

from tabulate import tabulate
import myModules as md

def search_projects_by_date(user_email):

    md.clear_screen()
    print("---------------- search for projects using date -----------------")

    search_date = md.read_valid_date("Enter The Date of Your Campaign: ")

    project_info = md.read_project_data(user_email)

    if len(project_info) > 0:

        matching_projects = [project for project in project_info["projects"] if project["startDate"] <= search_date <= project["endDate"]]

        if matching_projects:

            print("============> Matching projects:")
            # Convert the dictionary to a list of [key, value] pairs
            for proj in matching_projects:
                project_table = [[key, value] for key, value in proj.items()]
                print(tabulate(project_table, tablefmt="grid"))  
        else:
            print("\033[31m" + "No projects found for the specified date." + "\033[0m")
    else: 
        print("\033[34m" + "No Projects Found !!" + "\033[0m")