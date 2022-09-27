import socket
import threading

HOST = 'localhost'
PORT = 5678


def initialize_app():
    try:
        s.connect((HOST, PORT))
        print(f'Connected successfully to {HOST}:{PORT}')
    except:
        print(f'Failed to connect {HOST}:{PORT}')
    while True:
        device_list = s.recv(10240).decode('utf-8')
        selected_device = input(device_list)
        s.sendall(selected_device.encode('utf-8'))
        break


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
initialize_app()
s.close()
