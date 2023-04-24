class employee:
    def __init__(self,employee_index, username, password, tickets, role):
        self.username = username
        self.employee_index = employee_index
        self.password = password
        self.role = role
        self.tickets = tickets

    def get_ticket_by_number(self, index):
        return tickets(index)

    def get_ticket_list_size(self):
        return len(tickets)

class user:
    def __init__(self, user_index, username, password, active_ticket = -1):
        self.user_index = user_index
        self.username = username
        self.password = password
        self.active_ticket = active_ticket

    def set_active_ticket(new_ticket):
        self.active_ticket = new_ticket

    def obtain_record(self):
        return {self.username: {
            "password":self.password,
            "active_ticket_index":self.active_ticket
            }
        }

class ticket:
    def __init__(self, ticket_index, title, submitting_user_index, priority, content, status):
        self.ticket_index
        self.title
        self.submitting_user_index
        self.priority
        self.content
        self.status

    def obtain_record(self):
        return {
            self.title: {
                "submitting_user_index":self.submitting_user_index,
                "priority":self.priority,
                "content":self.content,
                "status":self.status
            }
        }