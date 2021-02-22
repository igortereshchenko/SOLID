class BackendDeveloper:
    @staticmethod
    def python():
        print('Writting Python code')

class FrontendDeveloper:
    @staticmethod
    def javascript():
        print('Writting JavaScript code')


class Project:
    def __init__(self):
        self.backend = BackendDeveloper()
        self.front = FrontendDeveloper()

    def developing_cooperation(self):
        self.backend.python()
        self.front.javascript()

project =Project()
project.developing_cooperation()

