from Liskov_substitution.after.IBody.IBody import IBody
from Liskov_substitution.after.IEngine.BicycleEngine import BicycleEngine
from Liskov_substitution.after.IEngine.CarEngine import CarEngine
from Liskov_substitution.after.IEngine.IEngine import IEngine
from Liskov_substitution.after.IWheel.IWheel import IWheel


class Vehicle(IBody, IWheel, IEngine):
    def __index__(self, name, speed, body: IBody, engine: IEngine):
        self.name = name
        self.speed =speed
        self.body = body
        self.engine = engine




class Car(Vehicle):

    def __init__(self, name, speed):
        super.__init__(name, speed, None, CarEngine())



class Bicycle(Vehicle):
    def __init__(self, name, speed ):
        super.__init__(name, speed, None, BicycleEngine())


