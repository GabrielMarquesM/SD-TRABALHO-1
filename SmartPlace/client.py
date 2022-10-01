import os
import socket

HOST = 'localhost'
PORT = 5678


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


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
        device_cmds = s.recv(10240).decode('utf-8')
        selected_cmd = input(device_cmds)
        s.sendall(selected_cmd.encode('utf-8'))
        cmd_result = s.recv(10240).decode('utf-8')
        clear_console()
        print(cmd_result)
        # break


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
initialize_app()
s.close()
