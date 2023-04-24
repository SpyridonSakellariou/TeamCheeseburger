import os
import json 

from utility_functions import filesystem_creator
from utility_functions import json_parser
from utility_functions import generic_functions

from classes import user_classes

def create_new_user(a_working_directory):
    duplicate_username = True

    user_input_username = "None"

    while duplicate_username:
        user_input_username = input("Please select a username: ")

        duplicate_username = json_parser.get_username_exists(a_working_directory, user_input_username)

        if duplicate_username:
            print("Username already exists. Please pick a different one.")

    user_input_password = input("Please select a password: ")

    temp_user = user_classes.user(user_input_username, user_input_password)
    user_data = temp_user.obtain_record()

    generic_functions.append_to_file(a_working_directory + '\\Users\\User.json', "users", user_data)

    return temp_user


def create_secondary_menu(a_user_credentials):
    pass

def main():
#Main function, fruitless. Handles startup tasks.
    print("Starting background tasks...")

    working_directory = os.getcwd()
    user_info = json_parser.get_default_user(working_directory)
    repair_directory = False
    continue_menu = True

    if not user_info:
        print("Critical error, filesystem corrupt. Rebuilding...")
        repair_directory = True

    filesystem_creator.check_filesystem(repair_directory)
    print("Background tasks done.")

    while continue_menu:
        print("Wellcome to the ticketing system for SuperGalactic Racing Games!")
        print("Do you wish to create a new account (1), or do you already have an account (2), or do you wish to quit (3)?")
        user_input = generic_functions.get_int(1,3)

        if user_input == 1:
            user =  create_new_user(working_directory)

        elif user_input == 2:
            user = json_parser.get_user_login(working_directory)
    
        else:
            continue_menu = False
            continue

        user.show_menu()

if __name__ == '__main__':
    main()
