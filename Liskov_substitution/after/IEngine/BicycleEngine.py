from Liskov_substitution.after.IEngine.IEngine import IEngine
from Liskov_substitution.after.IEngine.IStartProcess.BicyclerStartProcess import BicyclerStartProcess
from Liskov_substitution.after.IEngine.IStopProcess.BicyclerStopProcess import BicyclerStopProcess


class BicycleEngine(IEngine):

    def __init__(self):
        super.__init__(BicyclerStartProcess(), BicyclerStopProcess())