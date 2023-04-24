import json 
import os
from utility_functions import generic_functions
from classes import user_classes

def get_user_login(a_working_directory):
    logging_in = True

    while logging_in:
        print("Provide the category you are trying to access (1 - user, 2 - employee): ")
        user_provided_category = generic_functions.get_int(1,2)
        user_provided_username = input("Please provide a username: ")
        user_provided_password = input("Please provide a password: ")

        file_to_search = a_working_directory + '\\Users\\User.json'

        if user_provided_category == 1:
            file_to_search = a_working_directory + '\\Users\\User.json'

        else:
            file_to_search = a_working_directory + '\\Users\\Employee.json'

        with open(file_to_search) as f:
            candidate_user = generic_functions.log_in(f, user_provided_username, user_provided_password)

        if not candidate_user:
            print("Incorrect username or password. Please try again.")
            continue 

        return candidate_user


def get_default_user(a_working_directory):
    path = a_working_directory + '\\Users\\User.json'

    if not os.path.exists(path):
        return

    with open(path) as f:
        if os.stat(path).st_size > 0:
            json_data = json.load(f)
        else:
            return

    return json_data["users"][0]


def get_username_exists(a_working_directory, a_username):
    users_path = a_working_directory + '\\Users\\'
    working_path = users_path + 'Employee.json'

    duplicate = False 

    with open(working_path) as f:
        json_data = json.load(f)

    for candidate_match in json_data["employees"]:
        if candidate_match["username"] == a_username:
            duplicate = True

    working_path = users_path + 'User.json'

    with open(working_path) as f:
        json_data = json.load(f)

    for candidate_match in json_data["users"]:
        if candidate_match["username"] == a_username:
            duplicate = True

    return duplicate


def get_ticket_by_index(a_index):
    path = os.getcwd() + '\\Tickets\\Tickets.json'

    with open(path) as f:
        json_data = json.load(f)
        
        title                 = json_data["tickets"][0]["title"]
        submitting_user_index = json_data["tickets"][0]["submitting_user_index"]
        priority              = json_data["tickets"][0]["priority"]
        nature                = json_data["tickets"][0]["nature"]
        content               = json_data["tickets"][0]["content"]
        status                = json_data["tickets"][0]["status"]
