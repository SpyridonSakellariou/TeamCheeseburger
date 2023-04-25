from classes import Application_User
from classes import Ticket
from utility_functions import generic_functions
from utility_functions import json_operations

class Employee(Application_User.Application_User):
    def __init__(self, username, password, tickets, tickets_directory):
        super().__init__(username, password, tickets, tickets_directory)
        self.role = "Employee"

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
        print("                Employee Menu                  ")
        print("===============================================")
        print(f'Welcome {self.username}!')

        while show_menu:
            print("")
            print("")
            print("1. Show my tickets.")
            print("2. Claim ticket.")
            print("3. Logout.\n \n")
            
            user_choice = generic_functions.get_int(1,3)

            if user_choice == 1:
                with open(self.tickets_directory) as f:
                    my_tickets = json_operations.get_tickets_by_employee(f, self.username)

                    if len(my_tickets) > 0:
                        for ticket in my_tickets:
                            print(f'{ticket["title"]} - {ticket["submitting_user_name"]}')

                    else:
                        print("You don't have any active tickets.")

            elif user_choice == 2:
                claimed_ticket = False
                ticket_data = {}

                with open(self.tickets_directory) as f:
                    available_tickets = json_operations.get_tickets_by_employee(f, "None")
                    f.seek(0)

                    if len(available_tickets) == 0:
                        print("Error: No available tickets")

                        continue

                    selecting_ticket = True

                    while selecting_ticket:
                        for ticket in available_tickets:
                            print(f'Ticket title: {ticket["title"]} - {ticket["submitting_user_name"]}')

                        print("Select the name of a ticket you wish to manage.")
                        print("")

                        temp_list = []
                        for ticket in available_tickets:
                            temp_list.append(ticket["title"])

                        ticket_title = generic_functions.get_str(temp_list)

                        temp_list = []
                        for ticket in available_tickets:
                            temp_list.append(ticket["submitting_user_name"])
                        
                        print("Please input the user of the ticket you wish to manage.")
                        submitting_user = generic_functions.get_str(temp_list)


                        for recorded_ticket in available_tickets:
                            if recorded_ticket["title"] == ticket_title and recorded_ticket["submitting_user_name"] == submitting_user:
                                ticket_data = recorded_ticket

                        ticket_object = Ticket.Ticket(
                            ticket_data["title"],
                            ticket_data["category"],
                            ticket_data["submitting_user_name"],
                            ticket_data["managing_employee"],
                            1,
                            ticket_data["content"],
                            "ongoing"
                            )

                        print("")
                        print("Ticket details to follow:")
                        print(f'Ticket title:    \n {ticket_object.title}')
                        print(f'Ticket category: \n {ticket_object.category}')
                        print(f'Ticket user:     \n {ticket_object.submitting_user_name}')
                        print(f'Ticket priority: \n {ticket_object.priority}')
                        print(f'Ticket content:  \n {ticket_object.content}')
                        print(f'Ticket status:   \n {ticket_object.status}')
                        print("")
                        print("Claim this ticket (yes/no)?")

                        user_choice = generic_functions.get_str(["yes", "no"])

                        if user_choice == "yes":
                            ticket_object.managing_employee_name = self.username
                            ticket_object.status = "claimed"
                            selecting_ticket = False
                            claimed_ticket = True
                            continue

                        else:
                            print("Manage another ticket (yes/no)?")
                            user_choice = generic_functions.get_str(["yes", "no"])

                            if user_choice == "no":
                                selecting_ticket = False
                                
                            continue
                if claimed_ticket:
                    json_operations.set_ticket_claimed(self.tickets_directory, ticket_data["title"], ticket_data["submitting_user_name"], self.username)
            else:
                show_menu = False
