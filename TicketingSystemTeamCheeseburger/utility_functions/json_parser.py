import json 
from utility_functions import generic_functions

def read_log_user(a_file, a_request):

    json_data = json.load(a_file)

    if a_request == "display":
        max_choices = len(json_data)

        print(generic_functions.get_int(1, max_choices))
