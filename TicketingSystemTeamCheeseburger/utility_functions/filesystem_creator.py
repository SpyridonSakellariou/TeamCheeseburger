import os
import json


default_admin_contents = {
    "admin_1": {
        "username":"admin",
        "password":"admin"
    },
    "admin_2" : {
        "username":"admin2",
        "password":"admin2"
    }
}

default_employee_contents = {
    "employee_1": {
        "username":"employee",
        "password":"employee2",
        "role":"support_in_game"
    },
    "employee_2" : {
        "username":"employee2",
        "password":"employee2",
        "role":"support_monetary"
    }
}


def sublist_handler(a_list, a_result):
#A utility recursive function that finds the base elements of a list of unknown nested lists, and appends them to a given list.
    should_continue = True

    if not isinstance(a_list, list):
        a_result.append(a_list)
        should_continue = False

    if should_continue:
        for potential_file in a_list:
            sublist_handler(potential_file, a_result)


def check_users_filesystem(a_working_directory, a_result_list_directories, a_result_list_files):
#Function for checking the user filesystem.

    users_directory = a_working_directory + '\\Users\\'

    users_directory_administrator = users_directory + 'Administrator.json'
    users_directory_owner = users_directory + 'Owner.json'

    users_directory_files = [users_directory_administrator, users_directory_owner]
    users_directory_directories = [users_directory]

    
    sublist_handler(users_directory_files, a_result_list_files)
    sublist_handler(users_directory_directories, a_result_list_directories)


def check_logs_filesystem(a_working_directory, a_result_list_directories, a_result_list_files):
#Function for checking the user filesystem.

    logs_directory = a_working_directory + '\\Logs\\'
    logs_directory_administrator = logs_directory + 'Administrator\\'
    logs_directory_employee = logs_directory + 'Employee\\'
    logs_directory_user = logs_directory + 'User\\'

    logs_file_admin = logs_directory_administrator + 'Administrator.json'
    logs_file_employee = logs_directory_employee + 'Employee.json'
    logs_file_user = logs_directory_user + 'User.json'

    users_directory_files = [logs_file_admin, logs_file_employee, logs_file_user]
    users_directory_directories = [logs_directory, logs_directory_administrator, logs_directory_employee, logs_directory_user]

    
    sublist_handler(users_directory_files, a_result_list_files)
    sublist_handler(users_directory_directories, a_result_list_directories)


def check_filesystem():
#Checks to see if the filesystem is intact. Creates necessary directories and files.
    

    working_directory = os.getcwd()

    users_directories = []
    users_files = [] 
    check_users_filesystem(working_directory, users_directories, users_files)


    logs_directories = []
    logs_files = [] 
    check_logs_filesystem(working_directory, logs_directories, logs_files)


    all_directories = [] 
    sublist_handler([users_directories, logs_directories], all_directories)

    all_files = [] 
    sublist_handler([users_files, logs_files], all_files)
    

    #Directory creation here.
    for candidate_directory in all_directories:
        if not os.path.exists(candidate_directory):
            os.mkdir(candidate_directory)


    #File creation here.
    for candidate_file in all_files:
        if not os.path.exists(candidate_file):
            with open(candidate_file, 'w'):
                pass

    #Sanitize entries
    json_data_list = [default_admin_contents, default_employee_contents]
    i = 0
    for entry in json_data_list:
        with open(all_files[i], 'w') as f:
            json.dump(entry, f)
            i += 1
