import os

from utility_functions import filesystem_creator
from utility_functions import json_parser
from utility_functions import generic_functions

from classes import user_classes

def create_new_user():
    pass

def create_secondary_menu():
    pass

def main():
#Main function, fruitless. Handles startup tasks.
    print("Starting background tasks...")
    working_directory = os.getcwd()

    user_info = json_parser.get_default_user(working_directory)

    repair_directory = False

    if not user_info:
        print("Critical error, filesystem corrupt. Rebuilding...")
        repair_directory = True

    filesystem_creator.check_filesystem(repair_directory)
    print("Background tasks done.")

    print("Wellcome to the ticketing system for SuperGalactic Racing Games!")
    print("Do you wish to create a new account (1), or do you already have an account (2)?")
    user_input = generic_functions.get_int(1,2)

    if user_input == 1:
        user_data =  create_new_user()

    else:
        user_data = json_parser.get_user_login(working_directory)

    user_credentials = json_parser.get_user_by_reference(working_directory, user_data)
    print(user_credentials)
    create_secondary_menu()

if __name__ == '__main__':
    main()
