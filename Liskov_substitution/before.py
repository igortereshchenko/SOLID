class Vehicle:
    def __index__(self, name, speed, wheels):
        self.name = name
        self.speed =speed
        self.wheels = wheels

    def get_engine(self):
        pass

    def start_engine(self):
        pass

    def stop_engine(self):
        pass


class Car(Vehicle):

    def __init__(self, name, speed, body_type):
        super.__init__(name, speed)
        self.body_type = body_type

    def get_body_type(self):
        return self.body_type


class Bicycle(Vehicle):
    def __init__(self, name, speed, speed_count):
        super.__init__(name, speed)
        self.speed_count = speed_count

    def get_engine(self):
        pass

    def start_engine(self):
        pass

    def stop_engine(self):
        pass