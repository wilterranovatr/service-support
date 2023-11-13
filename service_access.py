import os
import shutil
import socket
import threading
import psutil
import wmi
import pythoncom

# Configura la dirección IP y el puerto en el que el servicio escuchará
HOST = '127.0.0.1'
PORT = 1345


def main():
    try:
        SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SERVER_SOCKET.bind((HOST, PORT))
        SERVER_SOCKET.listen(1)
        print(f"El servicio está escuchando en {HOST}:{PORT}")
    except:
        stop_port(PORT)
        SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SERVER_SOCKET.bind((HOST, PORT))
        SERVER_SOCKET.listen(1)

    while True:
        client_socket, addr = SERVER_SOCKET.accept()
        print(f"Conexión establecida con {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

def handle_client(client_socket):
    printer_name ="BIXOLON SRP-350III"
    printer=None
    status = None
    try:
        pythoncom.CoInitialize()
        c = wmi.WMI()
        printer = c.Win32_Printer(Name="BIXOLON SRP-350III")
        if str(printer[0].WorkOffline) == "False":
            status = "True"
        else:
            status = "False"
    except Exception as e:
        print(e)
        status = "False"
    print("Estado activo de la impresora: "+status)
    if status == "False":
        response = f"Error con la impresora {printer_name}.\nComuniquese con SOPORTE TÉCNICO.;IMP_ERR"
    try:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            
            if status == "True":
                # Procesa el comando recibido y realiza acciones en carpetas con privilegios de administrador
                if "copy;" in data:
                    print("Función ejecutar: COPIAR")
                    source, destination = data.split(";")[1], data.split(";")[2]
                    try:
                        shutil.copy(source, destination)
                        print(f"Se copió {source} --> {destination}")
                        response = f"Archivo copiado correctamente."
                    except Exception as e:
                        print(e)
                        response = f"Error al copiar el archivo: {str(e)};IMP_ERR"
                    
                    # Procesa el comando recibido y realiza acciones en carpetas con privilegios de administrador
                elif "move;" in data:
                    print("Función ejecutar: MOVER")
                    source, destination = data.split(";")[1], data.split(";")[2]
                    try:
                        shutil.move(source, destination)   #### Verificar
                        print(f"Se movió {source} --> {destination}")   ###
                        response = f"Archivo movido correctamente."
                    except Exception as e:
                        print(e)
                        response = f"Error al mover el archivo: {str(e)};IMP_ERR"
                else:
                    response = "Comando no reconocido;SER05"
            
            client_socket.send(response.encode())

    except Exception as e:
        print(f"Error en la comunicación con el cliente: {str(e)}")

    finally:
        client_socket.close()
        
def stop_port(puerto):
    for conexion in psutil.net_connections():
        if conexion.laddr.port == puerto:
            print(f"El puerto {puerto} está siendo utilizado por el proceso con PID {conexion.pid}")
            os.system(f'taskkill /pid {conexion.pid} /F')
def stop():
    stop_port(PORT)

if __name__ == '__main__':
    main()
