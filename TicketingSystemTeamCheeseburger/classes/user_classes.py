import os
import json

from utility_functions import generic_functions

class employee:
    def __init__(self, username, password, tickets, role):
        self.username = username
        self.password = password
        self.role = role
        self.tickets = tickets

class user:
    def __init__(self, username, password, active_ticket_index):
        self.username = username
        self.password = password
        self.active_ticket_index = active_ticket_index

    def obtain_record(self):
        return {
            "username":self.username,
            "password":self.password,
            "active_ticket_index":self.active_ticket_index
        }

    def show_menu(self):
        print(f'Welcome, {self.username}. What would you like to do?')

        continue_menu = True 

        while continue_menu:
            print(f'1. See progress on your ticket.')
            print(f'2. Submit new ticket (will replace the old ticket).')
            print(f'3. Log Out.')

            user_choice = generic_functions.get_int(1,3)
            ticket_directory = os.getcwd() + '\\Tickets\\Tickets.json'

            if user_choice == 1:
                with open(ticket_directory) as f:
                    json_data = json.load(f)

                    found_ticket = json_data["tickets"][0]

                    for candidate_match in json_data["tickets"]:
                        if candidate_match["title"] == self.active_ticket:
                            found_ticket = self.active_ticket
                            break

                    if not found_ticket["title"] == "None":
                        print(f'The status of your ticket is: {self.active_ticket.status} with priority: {self.active_ticket.priority}.')
                    else:
                        print("You do not seem to have a ticket in process.")

            elif user_choice == 2:
                with open(ticket_directory) as f:
                    json_data = json.load(f)
                    self.active_ticket.status = "abandoned"

                    ticket_title = input("Give your new ticket a title: ")
                    ticket_content = input("Give some details regarding your issue: ")

                    replacement_ticket = ticket(ticket_title, self.username, 0, ticket_content, "ongoing")
                    replacement_ticket_data = replacement_ticket.obtain_record()
                    generic_functions.append_to_file(ticket_directory, "tickets", replacement_ticket_data)
            else:
                continue_menu = False


class ticket:
    def __init__(self, title, submitting_user, priority, content, status):
        self.title = title
        self.submitting_user = submitting_user
        self.priority = priority
        self.content = content
        self.status = status

    def obtain_record(self):
        return {
            self.title: {
                "submitting_user_index":self.submitting_user_index,
                "priority":self.priority,
                "content":self.content,
                "status":self.status
            }
        }