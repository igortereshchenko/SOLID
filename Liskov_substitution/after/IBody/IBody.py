# interface
class IBody:

    def __init__(self, body_type):
        self.body_type = body_type

    def get_body_type(self):
        return self.body_type