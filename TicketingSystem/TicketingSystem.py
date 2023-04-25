from utility_functions import filesystem_creator
from utility_functions import json_operations
from utility_functions import generic_functions
from classes import Application_User
from classes import User
from classes import Ticket
from classes import Employee


def create_new_user(a_working_directory):
    duplicate_username = True

    user_input_username = "None"

    while duplicate_username:
        user_input_username = input("Please select a username: ")

        found_duplicate = False

        with open(a_working_directory + '\\Users\\User.json') as f:
            found_duplicate = json_operations.get_username_exists(f, "users", user_input_username)
        
        if not found_duplicate:
            with open(a_working_directory + '\\Users\\Employee.json') as f:
                found_duplicate = json_operations.get_username_exists(f, "employees", user_input_username)
        
        duplicate_username = found_duplicate

        if duplicate_username:
            print("Username already exists. Please pick a different one.")

    user_input_password = input("Please select a password: ")

    temp_user = User.User(user_input_username, user_input_password, [], a_working_directory + '\\Tickets\\Tickets.json')
    user_data = temp_user.Get_Data()

    json_operations.append_to_file(a_working_directory + '\\Users\\User.json', "users", user_data)

    return temp_user


def create_secondary_menu(a_user_credentials):
    pass

def main():
#Main function, fruitless. Handles startup tasks.
    print("Starting background tasks...")
    working_directory = filesystem_creator.get_cwd()
    repair_directory = False
    continue_menu = True
    filesystem_creator.check_filesystem(repair_directory)
    print("Background tasks done.")

    while continue_menu:
        print("Wellcome to the ticketing system for SuperGalactic Racing Games!")
        print("Do you wish to create a new account (1), or do you already have an account (2), or do you wish to quit (3)?")
        user_input = generic_functions.get_int(1,3)

        if user_input == 1:
            user =  create_new_user(working_directory)

        elif user_input == 2:
            user = json_operations.log_in(working_directory)
    
        else:
            continue_menu = False
            continue

        temp_user = User.User(user["username"],  user["password"], user["tickets"], working_directory + '\\Tickets\\Tickets.json')
        temp_user.Show_Menu()

if __name__ == '__main__':
    main()
