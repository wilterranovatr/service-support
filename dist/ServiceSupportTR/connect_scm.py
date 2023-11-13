from scm import PythonService
import service_access

class ServiceSupport(PythonService):
    _svc_name_ ="ServiceSupportTR"
    _svc_display_name_= "ServiceSupportTR"
    _svc_description_="Servicio de Soporte Impresión"
    _exe_name_ ="I:\\git\\service_support\\venv\\Scripts\\pythonservice.exe"
    
    ###
    def start(self):
        self.isrunning = True
    
    def stop(self):
        self.isrunning = False
        service_access.stop()
        
    def main(self):
        while self.isrunning:
            service_access.main()
        
        
if __name__ == '__main__':
    ServiceSupport.parse_command_line()

