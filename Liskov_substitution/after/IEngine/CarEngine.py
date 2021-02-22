from Liskov_substitution.after.IEngine.IEngine import IEngine
from Liskov_substitution.after.IEngine.IStartProcess.CarStartProcess import CarStartProcess
from Liskov_substitution.after.IEngine.IStopProcess.CarStopProcess import CarStopProcess


class CarEngine(IEngine):

    def __init__(self):
        super.__init__(CarStartProcess(), CarStopProcess())