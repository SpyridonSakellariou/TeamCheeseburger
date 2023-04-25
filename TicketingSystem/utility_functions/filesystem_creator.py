#This class creates and manages the files
#Authors Tynan Orr, Sypridon Sakellariou
#Date: March 31th, 2023
#Last Update: April 25th

import os
from utility_functions import json_operations 

default_user_contents = {
    "users":[
        {
            "username":"user_1",
            "password":"user1",
            "tickets":[
            ]
        }, 
        {
            "username":"user_2",
            "password":"user2",
            "tickets":[
            ]
        }
    ]
}

default_employee_contents = {
    "employees":[
        {
            "username":"employee_1",
            "password":"employee1",
            "role":"support_in_game",
            "tickets":[
            ]
        },
        {
            "username":"employee_2",
            "password":"employee2",
            "role":"support_monetary",
            "tickets":[
            ]
        }
    ]
}

default_tickets_contents = {
    "tickets": [
    ]
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

    users_directory_employee = users_directory + 'Employee.json'
    users_directory_user = users_directory + 'User.json'

    users_directory_files = [users_directory_employee, users_directory_user]
    users_directory_directories = [users_directory]

    
    sublist_handler(users_directory_files, a_result_list_files)
    sublist_handler(users_directory_directories, a_result_list_directories)


"""Creates the necessary files for the tickets directory if it doesn't exist"""
def check_tickets_filesystem(a_working_directory, a_result_list_directories, a_result_list_files):
    tickets_directory = a_working_directory + '\\Tickets\\'
    tickets_holder = tickets_directory + 'Tickets.json'

    tickets_directory_files = [tickets_holder]
    tickets_directory_directories = [tickets_directory]

    sublist_handler(tickets_directory_files, a_result_list_files)
    sublist_handler(tickets_directory_directories, a_result_list_directories)


def check_filesystem(a_repair):
#Checks to see if the filesystem is intact. Creates necessary directories and files.
    

    working_directory = os.getcwd()

    users_directories = []
    users_files = [] 
    check_users_filesystem(working_directory, users_directories, users_files)

    tickets_directories = []
    tickets_files = []
    check_tickets_filesystem(working_directory, tickets_directories, tickets_files)

    all_directories = [] 
    sublist_handler([users_directories, tickets_directories], all_directories)

    all_files = [] 
    sublist_handler([users_files, tickets_files], all_files)
    
    should_sanitize = False

    if a_repair:
        should_sanitize = True

    #Directory creation here.
    for candidate_directory in all_directories:
        if not os.path.exists(candidate_directory):
            os.mkdir(candidate_directory)
            should_sanitize = True

    #File creation here.
    for candidate_file in all_files:
        if not os.path.exists(candidate_file):
            with open(candidate_file, 'w'):
                should_sanitize = True

    #Sanitize entries
    if should_sanitize == True:
        json_data_list = [default_employee_contents, default_user_contents, default_tickets_contents]
        i = 0
        for entry in json_data_list:
            with open(all_files[i], 'w') as f:
                json_operations.write_json(f, entry)
                i += 1

def get_cwd():
    return os.getcwd()
