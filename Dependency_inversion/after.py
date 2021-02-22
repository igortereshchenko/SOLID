class Developer:
    def develop(self):
        raise NotImplementedError

class BackendDeveloper(Developer):

    def develop(self):
        self.python()

    @staticmethod
    def python():
        print('Writting Python code')

class FrontendDeveloper(Developer):

    def develop(self):
        self.python()

    @staticmethod
    def javascript():
        print('Writting JavaScript code')


class Developers(Developer):
    def __init__(self):
        self.backend = BackendDeveloper()
        self.front = FrontendDeveloper()

    # team = 1 developer
    # how team work as 1 developer
    def develop(self):
        self.backend.develop()
        self.front.develop()


class Project:

    def __init__(self):
        self.developers = Developers()

    def developing_cooperation(self):
        self.developers.develop()


project =Project()
project.developing_cooperation()

