#! /usr/bin/python3

import json

def read_all_data(filename):
    try:
        with open(f"./systemFiles/{filename}", 'r') as fileObject:
            data_str = fileObject.read()
            
            if len(data_str) > 0:
                # Convert the string to a list of dictionaries
                data = json.loads(data_str)
                return data
            
            return list()
    except Exception as e:
        print("\033[31m"+ f"ERROR: {e}" + "\033[0m")


def read_project_data(userEmail):
    try:  
        users_projects_list = read_all_data("users_projects.json")
        
        if len(users_projects_list)>0:

            for user_projects in users_projects_list:

                if user_projects["email"] == userEmail:
                    return user_projects
        else:
            return list()
    except Exception as e:
        print("\033[31m"+ f"ERROR: {e}" + "\033[0m")