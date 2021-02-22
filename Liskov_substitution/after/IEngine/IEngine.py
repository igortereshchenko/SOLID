from Liskov_substitution.after.IEngine.IStartProcess.IStartProcess import IStartProcess
from Liskov_substitution.after.IEngine.IStopProcess.IStopProcess import IStopProcess


class IEngine:

    def __init__(self, start_process: IStartProcess, stop_process: IStopProcess):
        self.start_process = start_process
        self.stop_process = stop_process


    def get_engine(self):
        raise NotImplemented

    def start_engine(self):
        self.start_process.start()

    def stop_engine(self):
        self.stop_engine().stop()
