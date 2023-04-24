import os

from utility_functions import filesystem_creator
from utility_functions import json_parser
from classes import user_classes

def main():
#Main function, fruitless. Handles startup tasks.
    filesystem_creator.check_filesystem()

    working_directory = os.getcwd()

    #driver - login
    #json_parser.get_user_login(working_directory)

    test_user = user_classes.user(2, "user_3", "user3")

    print(test_user.obtain_record())

    

if __name__ == '__main__':
    main()
