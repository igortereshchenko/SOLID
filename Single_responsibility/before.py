class Account:

    def __init__(self, number, email, avatar, name):
        # account info
        self.number = number
        self.name = name

        # contact
        # set of email
        self.email = { email }

        # image processing
        self.avatar = avatar

    def get_number(self):
        return self.number

    # new process
    def add_email(self, new_email):
        self.email.add(new_email)

    # new process
    def save(self):
        # save to db
        pass


