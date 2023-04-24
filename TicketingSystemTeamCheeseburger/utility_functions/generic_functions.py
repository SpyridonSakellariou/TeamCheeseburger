import json
from classes import user_classes


def get_int(a_min_value, a_max_value):
    proper_input = False 

    while not proper_input:
        print(f'Min value: {a_min_value}, max value: {a_max_value}')

        user_input = input("Please input your selection: ")

        try:
            user_float = float(user_input)

        except ValueError:
            print("Value error - expected int, was given string instead.")

            continue

        if not user_float * 2 % 2 == 0.0:
            print("Value error - expected int, was given float instead.")

            continue 

        if a_max_value >= user_float and a_min_value <= user_float:
            return int(user_float)

        print(f'Value error - expected number between {a_min_value} and {a_max_value}, was given {user_float} instead.')


def log_in(a_file, a_username, a_password):

    json_index = -1
    json_data = json.load(a_file)

    if a_username in json_data:
        if a_password == json_data[a_username]["password"]:
            json_index = list(json_data.keys()).index(a_username)

    return json_index


def manage_ticket(a_ticket, a_employee):
    a_ticket