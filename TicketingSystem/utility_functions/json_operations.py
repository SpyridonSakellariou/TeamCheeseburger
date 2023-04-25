import json

def append_to_file(a_file, a_field, a_data):
    with open(a_file,'r+') as f:
        json_data = json.load(f)
        json_data[a_field].append(a_data)
        f.seek(0)
        json.dump(json_data, f)


def get_username_exists(a_file, a_field, a_username):
    duplicate = False 
    json_data = json.load(a_file)

    for candidate_match in json_data[a_field]:
        if candidate_match["username"] == a_username:
            duplicate = True

    return duplicate


def get_ticket_data_by_index(a_file, a_index):
    json_data = json.load(a_file)
        
    title                 = json_data["tickets"][a_index]["title"]
    submitting_user_name  = json_data["tickets"][a_index]["submitting_user_name"]
    priority              = json_data["tickets"][a_index]["priority"]
    nature                = json_data["tickets"][a_index]["nature"]
    content               = json_data["tickets"][a_index]["content"]
    status                = json_data["tickets"][a_index]["status"]

    return {
                "title":                title,
                "submitting_user_index":submitting_user_name,
                "priority":             priority,
                "nature":               nature,
                "content":              content,
                "status":               status
           }


def get_ticket_data_by_name(a_file, a_user_username, a_name):
    json_data = json.load(a_file)

    for ticket in json_data["tickets"]:
        if ticket["title"] == a_name and ticket["submitting_user_name"] == a_user_username:
            print("Successfully found ticket")
            return {
                        "title":                ticket["title"],
                        "submitting_user_index":ticket["submitting_user_name"],
                        "priority":             ticket["priority"],
                        "content":              ticket["content"],
                        "status":               ticket["status"]
                   }

    return {}


def get_user_data_by_name(a_file, a_field, a_username):
    json_data = json.load(a_file)

    for user in json_data[a_field]:
        if user["username"] == a_username:
            return {
                        "username":user["username"],
                        "password":user["password"],
                        "tickets": user["tickets"],
                        "role":    user["role"]
                   }

    return


def get_tickets_by_username(a_file, a_user_username):
    json_data = json.load(a_file)
    response = []

    for ticket in json_data["tickets"]:
        if ticket["submitting_user_name"] == a_user_username:
            response.append(ticket)

    return response


def get_tickets_by_employee(a_file, a_user_username):
    json_data = json.load(a_file)
    response = []

    for ticket in json_data["tickets"]:
        if ticket["managing_employee"] == a_user_username:
            response.append(ticket)

    return response


def set_ticket_claimed(a_path, a_ticket_name, a_ticket_user, a_ticket_employee):
    with open(a_path, "r+") as f:
        json_data = json.load(f)

        for ticket in json_data["tickets"]:
            if ticket["title"] == a_ticket_name and ticket["submitting_user_name"] == a_ticket_user:
                ticket["managing_employee"] = a_ticket_employee
                ticket["status"] = "claimed"
        f.seek(0)
        json.dump(json_data, f)


def log_in(a_working_directory):
    logging_in = True
    users_path = a_working_directory + '\\Users\\User.json'
    employees_path = a_working_directory + '\\Users\\Employee.json'

    while logging_in:
        conflicting_username = False
        user_level = "guest"
        user_username = "None"
        user_password = "None"

        while not conflicting_username:
            user_choice = input("Please provide a username: ")
            user_username = user_choice
            user_level = "Guest"

            with open(users_path) as f:
                temp_bool = get_username_exists(f, "users", user_choice)

                if temp_bool:
                    user_level = "users"
                    break

            with open(employees_path) as f:
                temp_bool = get_username_exists(f, "employees", user_choice)

                if temp_bool:
                    user_level = "employees"
                    break
            
                    
            if not temp_bool:
                print("Username does not exist, please try again. \n")
            conflicting_username = temp_bool

        appropriate_password = False

        while not appropriate_password:
            user_password = input("Please provide a password: ")

            if user_level == "users":
                with open(users_path) as f:
                    response = check_credentials(f, "users", user_username, user_password)
           
            else:
                with open(employees_path) as f:
                    response = check_credentials(f, "employees", user_username, user_password)
            

            if response:
                appropriate_password = response
                logging_in = False
            else:
                print("Incorrect password. Please try again. \n")

    if user_level == "users":
        with open(users_path) as f:
            return get_user_data_by_name(f, "users", user_username)

    with open(employees_path) as f:
        return get_user_data_by_name(f, "employees", user_username)

def check_credentials(a_file, a_field, a_username, a_password): 
    json_data = json.load(a_file)

    for candidate_user in json_data[a_field]:
        if candidate_user["username"] == a_username and candidate_user["password"] == a_password:
            return True

    return False

def create_ticket(a_file, a_title, a_category, a_username, a_content):
    new_ticket_data = {
                            "title":               a_title,
                            "category":            a_category,
                            "submitting_user_name":a_username,
                            "managing_employee"   :"None",
                            "priority":            0,
                            "content":             a_content,
                            "status":              "ongoing"
                      }
    append_to_file(a_file, "tickets", new_ticket_data)

def write_json(a_file, a_entry):
    json.dump(a_entry, a_file)