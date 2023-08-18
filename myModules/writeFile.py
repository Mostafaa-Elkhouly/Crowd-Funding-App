#! /usr/bin/python3

import json
import myModules as md

def write_data(data, filename):
    try:
        data_list = md.read_all_data(filename)

        with open(f"./systemFiles/{filename}", 'w') as fileObject:
            data_list.append(data)
            #convert list of dicts to string -  Serialize obj as a JSON formatted str
            new_data = json.dumps(data_list, indent=2)
            fileObject.write(new_data)
    except Exception as e:
        print("\033[31m"+ f"ERROR: {e}" + "\033[0m")

        