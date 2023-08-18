#! /usr/bin/python3

import json
import myModules as md

def write_user_data(data):
    try:
        data_list = md.read_all_data("users_info.json")

        with open("./systemFiles/users_info.json", 'w') as fileObject:
            data_list.append(data)
            #convert list of dicts to string -  Serialize obj as a JSON formatted str
            new_data = json.dumps(data_list, indent=2)
            fileObject.write(new_data)
    except Exception as e:
        print("\033[31m"+ f"ERROR: {e}" + "\033[0m")



def write_user_projects_data(userEmail, projectInfo):
    try:
        users_projects_list = md.read_all_data("users_projects.json")

        for user in users_projects_list:
            if user["email"] == userEmail:
                user["projects"].append(projectInfo)
                break
        else:
            new_user = {"email": userEmail, "projects": [projectInfo]}
            users_projects_list.append(new_user)

        with open(f"./systemFiles/users_projects.json", 'w') as fileObject:
            #convert list of dicts to string -  Serialize obj as a JSON formatted str
            new_data = json.dumps(users_projects_list, indent=2)
            fileObject.write(new_data)
    except Exception as e:
        print("\033[31m"+ f"ERROR: {e}" + "\033[0m")
        

def update_user_projects_data(userEmail, userProjects):
    try:
        users_projects_list = md.read_all_data("users_projects.json")

        for user in users_projects_list:
            if user["email"] == userEmail:
                user["projects"]=userProjects["projects"]
                break

        with open(f"./systemFiles/users_projects.json", 'w') as fileObject:
            #convert list of dicts to string -  Serialize obj as a JSON formatted str
            new_data = json.dumps(users_projects_list, indent=2)
            fileObject.write(new_data)
    except Exception as e:
        print("\033[31m"+ f"ERROR: {e}" + "\033[0m")
