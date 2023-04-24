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
    json_data = json.load(a_file)

    for candidate_user in json_data["users"]:
        if candidate_user["username"] == a_username and candidate_user["password"] == a_password:
            return user_classes.user(candidate_user["username"], candidate_user["password"], candidate_user["active_ticket"])

    return


def append_to_file(a_file, a_field, a_data):
    with open(a_file,'r+') as f:
        json_data = json.load(f)
        json_data[a_field].append(a_data)
        f.seek(0)
        json.dump(json_data, f)