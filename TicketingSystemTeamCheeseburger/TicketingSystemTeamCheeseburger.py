import os

from utility_functions import filesystem_creator
from utility_functions import json_parser

def main():
#Main function, fruitless. Handles startup tasks.
    filesystem_creator.check_filesystem()

    working_directory = os.getcwd()

    with open(working_directory + '\\Users\\Administrator.json') as f:
        json_parser.read_log_user(f, "display")

if __name__ == '__main__':
    main()
