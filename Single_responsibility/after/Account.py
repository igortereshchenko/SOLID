from Single_responsibility.after.IImage import IImage
from Single_responsibility.after.Contact import Contact

class Account:

    def __init__(self, number, name, contact: Contact, avatar: IImage):
        # account info
        self.number = number
        self.name = name

        # contact as new class
        self.contact = contact

        # image processing as new class
        # self.avatar_image = avatar.get_image Fucked awful practice
        self.avatar = avatar

    def get_number(self):
        return self.number


