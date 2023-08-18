#! /usr/bin/python3

from tabulate import tabulate
import myModules as md
from addProject import createProject
from listProjects import viewAllProjects
from modifyProject import editProject
from modifyProject import deleteProject
from searchProject import serchForProject

def projectsMenu(userEmail):
        
    print("---------------- Projects Form -----------------")

    table = [
        ["Press 1","To Create a New Project"],
        ["Press 2","To View All Projects"],
        ["Press 3","To Edit a Project"],
        ["Press 4","To Delete a Project"],
        ["Press 5","To search for a project using date"],
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
                deleteProject()
            elif integer_value == 5:
                serchForProject()
            else:
                raise ValueError
            break  
        except ValueError:
            print("\033[31m" + "Invalid input. Please enter an integer." + "\033[0m")
