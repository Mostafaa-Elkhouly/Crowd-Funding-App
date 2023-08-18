#! /usr/bin/python3

from tabulate import tabulate
import myModules as md

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
                viewAllProject(userEmail)
            elif integer_value == 3:
                editProject()
            elif integer_value == 4:
                deleteProject()
            elif integer_value == 5:
                serchForProject()
            else:
                raise ValueError
            break  
        except ValueError:
            print("\033[31m" + "Invalid input. Please enter an integer." + "\033[0m")




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
    print("\033[32m" + f"Project {title} Added successfully." + "\033[0m")


def viewAllProject(userEmail):

    users_projects_list = md.read_all_data("users_projects.json")
    projects = []
    for user_projects in users_projects_list:

        if user_projects["email"] == userEmail:

            for project in user_projects["projects"]:

                # Convert the dictionary to a list of [key, value] pairs
                project_table = [[key, value] for key, value in project.items()]
                print(tabulate(project_table, tablefmt="grid"))   

def editProject():
    pass

def deleteProject():
    pass

def serchForProject():
    pass