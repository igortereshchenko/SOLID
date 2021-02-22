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

# common features
class Vehicle(IBody,IMomement):
    pass

class Car(Vehicle, IEngine):
    pass

class Bicycle(Vehicle):
    pass
