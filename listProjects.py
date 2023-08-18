#! /usr/bin/python3

from tabulate import tabulate
import myModules as md

def viewAllProjects(userEmail):

    project_info = md.read_project_data(userEmail)

    if len(project_info) > 0:
        for project in project_info["projects"]:

            # Convert the dictionary to a list of [key, value] pairs
            project_table = [[key, value] for key, value in project.items()]
            print(tabulate(project_table, tablefmt="grid"))  
    else: 
        print("\033[34m" + "No Projects Found !!" + "\033[0m")
