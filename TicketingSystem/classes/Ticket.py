#This class fills the ticket object with its variables and returns it
#Authors Tynan Orr, Sypridon Sakellariou
#Date: March 31th, 2023
#Last Update: April 25th
class Ticket:
    def __init__(self, title, category, submitting_user_name, priority, content, status):
        self.title                = title
        self.category             = category
        self.submitting_user_name = submitting_user_name
        self.priority             = priority
        self.content              = content
        self.status               = status

    def get_ticket_data(self):
        return {
            {
                "title":                self.title,
                "submitting_user_name": self.submitting_user_name,
                "priority":             self.priority,
                "content":              self.content,
                "status":               self.status
            }
        }




