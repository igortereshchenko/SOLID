from Liskov_substitution.after.IBody.IBody import IBody
from Liskov_substitution.after.IEngine.IEngine import IEngine

class IMomement:

    def move_left(self):
        pass
    def move_right(self):
        pass
    def move_forward(self):
        pass
    def move_back(self):
        pass

class Car(IBody, IEngine,IMomement):
    pass

# class Bicycle(IBody, IEngine,IMomement):
#     pass
class Bicycle(IBody, IMomement):
    pass
