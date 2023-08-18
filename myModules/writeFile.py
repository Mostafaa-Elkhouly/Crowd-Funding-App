#! /usr/bin/python3

import json
import myModules as md

def write_data(info):
    try:
        old_data = md.read_all_usersInfo()

        with open("./systemFiles/usersInfo.json", 'w') as fileObject:
            old_data.append(info)
            #convert list of dicts to string -  Serialize obj as a JSON formatted str
            new_data = json.dumps(old_data, indent=2)
            fileObject.write(new_data)
    except Exception as e:
        print("\033[31m"+ f"ERROR: {e}" + "\033[0m")

        