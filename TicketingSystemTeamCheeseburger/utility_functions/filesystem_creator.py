import os
import json

default_user_contents = {

    "user_1": {
        "password":"user1",
        "active_ticket_index":0
    }, 
    "user_2": {
        "password":"user2",
        "active_ticket_index":1
    }   
}

default_admin_contents = {
    "admin_1": {
        "password":"admin"
    },
    "admin_2" : {
        "password":"admin2"
    }
}

default_employee_contents = {
    "employee_1": {
        "password":"employee1",
        "role":"support_in_game",
        "tickets":[
            2,3,4,5
        ]
    },
    "employee_2" : {
        "password":"employee2",
        "role":"support_monetary",
        "tickets":[
            1
        ]
    }
}

default_tickets_contents = {
    "Cannot log in pls hlp": {
        "submitting_user_index":0,
        "priority":0,
        "nature":1,
        "content":"...",
        "status":"ongoing"
    },
    "Cannot purchase things from the cosmetics store": {
        "submitting_user_index":1,
        "priority":1,
        "nature":2,
        "content":"...",
        "status":"ongoing"
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
    users_directory_employee = users_directory + 'Employee.json'
    users_directory_user = users_directory + 'User.json'

    users_directory_files = [users_directory_administrator, users_directory_employee, users_directory_user]
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

"""Creates the necessary files for the tickets directory if it doesn't exist"""
def check_tickets_filesystem(a_working_directory, a_result_list_directories, a_result_list_files):
    tickets_directory = a_working_directory + '\\Tickets\\'
    tickets_holder = tickets_directory + 'Tickets.json'

    tickets_directory_files = [tickets_holder]
    tickets_directory_directories = [tickets_directory]

    sublist_handler(tickets_directory_files, a_result_list_files)
    sublist_handler(tickets_directory_directories, a_result_list_directories)


def clean_folders(a_working_directory, a_directory):
    for directory in a_directory:
        shutil.rmtree(directory)


def check_filesystem(a_repair):
#Checks to see if the filesystem is intact. Creates necessary directories and files.
    

    working_directory = os.getcwd()

    users_directories = []
    users_files = [] 
    check_users_filesystem(working_directory, users_directories, users_files)


    logs_directories = []
    logs_files = [] 
    check_logs_filesystem(working_directory, logs_directories, logs_files)

    tickets_directories = []
    tickets_files = []
    check_tickets_filesystem(working_directory, tickets_directories, tickets_files)

    all_directories = [] 
    sublist_handler([users_directories, logs_directories, tickets_directories], all_directories)

    all_files = [] 
    sublist_handler([users_files, tickets_files, logs_files], all_files)
    
    should_sanitize = False

    if a_repair:
        should_sanitize = True
    else:
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
        json_data_list = [default_admin_contents, default_employee_contents, default_user_contents, default_tickets_contents]
        i = 0
        for entry in json_data_list:
            with open(all_files[i], 'w') as f:
                json.dump(entry, f)
                i += 1
