class Contact:

    def __init__(self, email=None):
        self.email = set()
        if email:
            self.email.add(email)

    def add_new_email(self, new_email):
        self.email.add(new_email)


