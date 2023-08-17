#! /usr/bin/python3

def read_all_usersInfo():
    try:
        with open("./systemFiles/usersInfo.json", 'r') as fileObject:
            data = fileObject.read()

            if len(data) > 0:
                return data
            
            return "[]"
            
    except Exception as e:
        print("\033[31m"+ f"ERROR: {e}" + "\033[0m")

        