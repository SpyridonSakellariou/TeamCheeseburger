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




