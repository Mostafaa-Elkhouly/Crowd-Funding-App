#! /usr/bin/python3

from tabulate import tabulate
import myModules as md
from addProject import createProject
from listProjects import viewAllProjects
from modifyProject import editProject
from deleteProject import delete_project_by_title
from searchProject import search_projects_by_date

def projectsMenu(userEmail):
        
    print("---------------- Projects Form -----------------")

    table = [
        ["Press 1","To Create a New Project"],
        ["Press 2","To View All Projects"],
        ["Press 3","To Edit a Project"],
        ["Press 4","To Delete a Project"],
        ["Press 5","To search for a project using date"],
        ["Press 0","To EXIT!"],
        ]

    while True:
        val = input(tabulate(table) + "\n" + "Your choose: ")

        try:
            integer_value = int(val)
            if integer_value == 1:
                createProject(userEmail)
            elif integer_value == 2:
                viewAllProjects(userEmail)
            elif integer_value == 3:
                editProject(userEmail)
            elif integer_value == 4:
                delete_project_by_title(userEmail)
            elif integer_value == 5:
                search_projects_by_date(userEmail)
            elif integer_value == 0:
                md.clear_screen()
                break
            else:
                raise ValueError

        except ValueError:
            print("\033[31m" + "Invalid input. Please enter an integer." + "\033[0m")
