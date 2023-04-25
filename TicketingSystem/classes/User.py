from classes import Application_User
from utility_functions import generic_functions
from utility_functions import json_operations

"""User class. Used extensively throughout the program, it is used to substantiate
a user whose attributes are inherited from the Application_User class.
Authors Tynan Orr, Sypridon Sakellariou
Date: March 31th, 2023
Last Update: April 25th"""

class User(Application_User.Application_User):
    def __init__(self, username, password, tickets, tickets_directory):
        super().__init__(username, password, tickets, tickets_directory)
        self.role = "User"

    def Get_Data(self):
        return {
                    "username":self.username,
                    "password":self.password,
                    "tickets": self.tickets,
                    "role":    self.role
               }

    def Show_Menu(self):
        show_menu = True
        print("")
        print("===============================================")
        print("                  User Menu                    ")
        print("===============================================")
        print(f'Welcome {self.username}!')

        while show_menu:
            print("")
            print("")
            print("1. Show tickets.")
            print("2. Submit ticket.")
            print("3. Logout.\n \n")
            
            user_choice = generic_functions.get_int(1,3)

            if user_choice == 1:
                with open(self.tickets_directory) as f:
                    my_tickets = json_operations.get_tickets_by_username(f, self.username)

                    if len(my_tickets) > 0:
                        print(my_tickets)

                    else:
                        print("You don't have any active tickets.")

            elif user_choice == 2:

                ticket_title = input("Give your new ticket a title: ")
                ticket_content = input("Give some details regarding your issue: ")
                print("Select a category - Financial (1), Technical (2), Other (3)")
                user_choice = generic_functions.get_int(1,3)

                ticket_category = "Other"

                if user_choice == 1:
                    ticket_category = "Financial"

                elif user_choice == 2:
                    ticket_category = "Technical"

                with open(self.tickets_directory) as f:
                    json_operations.create_ticket(self.tickets_directory, ticket_title, ticket_category, self.username, ticket_content)

            else:
                show_menu = False
