import json 
import os
from utility_functions import generic_functions


def get_user_login(a_working_directory):
    logging_in = True

    while logging_in:
        print("Provide the category you are trying to access (1 - user, 2 - employee, 3 - admin): ")
        user_provided_category = generic_functions.get_int(1,3)
        user_provided_username = input("Please provide a username: ")
        user_provided_password = input("Please provide a password: ")

        file_to_search = a_working_directory + '\\Users\\User.json'

        if user_provided_category == 1:
            file_to_search = a_working_directory + '\\Users\\User.json'

        elif user_provided_category == 2:
            file_to_search = a_working_directory + '\\Users\\Employee.json'

        else:
            file_to_search = a_working_directory + '\\Users\\Administrator.json'

        with open(file_to_search) as f:
            returned_index = generic_functions.log_in(f, user_provided_username, user_provided_password)

        if returned_index == -1:

            print("Incorrect username or password. Please try again.")
            continue 

        return [user_provided_category, returned_index]


def view_file_contents(a_file):
    json_data = json.load(a_file)
    print(json_data["user_1"]["password"])


def get_default_user(a_working_directory):
    path = a_working_directory + '\\Users\\User.json'

    with open(path) as f:
        if os.stat(path).st_size > 0:
            json_data = json.load(f)
        else:
            return

    for user in json_data:
        if user:
            return json_data[user]

def get_user_by_reference(a_working_directory, a_reference):
    if a_reference[0] == 1:
        path = a_working_directory + '\\Users\\User.json'
    elif a_reference[1] == 2:
        path = a_working_directory + '\\Users\\Employee.json'
    else:
        path = a_working_directory + '\\Users\\Administrator.json'

    index = a_reference[1]

    with open(path) as f:
        json_data = json.load(f)

    for key in json_data:
        index -= 1

        if index < 0:
            return json_data[key]