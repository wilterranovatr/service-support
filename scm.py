import win32event
import win32service
import win32serviceutil
from abc import ABC, abstractmethod

class PythonService(win32serviceutil.ServiceFramework, ABC):
    
    @classmethod
    def parse_command_line(cls):
        win32serviceutil.HandleCommandLine(cls)
    
    @abstractmethod
    def stop(self):
        pass
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def main(self):
        pass
    
    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
    
    def SvcStop(self):
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
    
    def SvcDoRun(self):
        self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
        self.start()
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        self.main()