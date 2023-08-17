#! /usr/bin/python3

import myModules as md
import json

def write_data(info):
    try:
        old_data_str = md.read_all_usersInfo()

        # Convert the string to a list of dictionaries
        old_data = json.loads(old_data_str)

        with open("./systemFiles/usersInfo.json", 'w') as fileObject:
            old_data.append(info)
            #convert list of dicts to string -  Serialize obj as a JSON formatted str
            new_data = json.dumps(old_data, indent=2)
            fileObject.write(new_data)
    except Exception as e:
        print("\033[31m"+ f"ERROR: {e}" + "\033[0m")

        