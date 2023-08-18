#! /usr/bin/python3

import json

def read_all_usersInfo():
    try:
        with open("./systemFiles/usersInfo.json", 'r') as fileObject:
            data_str = fileObject.read()
            
            if len(data_str) > 0:
                # Convert the string to a list of dictionaries
                data = json.loads(data_str)
                return data
            
            return list()
            
    except Exception as e:
        print("\033[31m"+ f"ERROR: {e}" + "\033[0m")

        