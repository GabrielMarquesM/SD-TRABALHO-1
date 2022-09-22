import json
import os
import socket
import threading
from datetime import datetime
from enum import Enum


class Command(str, Enum):
    JOIN = "/ENTRAR"
    USERS = "/USUARIOS"
    DISCONNECT = "/SAIR"
    QUIT = "q"


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def join():
    address = input("IP: ")
    port = input("Porta: ")
    try:
        s.connect((address, int(port)))
    except:
        print("Conexão mal-sucedida, tente novamente.")
        return
    # Servidor pede nickname
    server_request = s.recv(1024).decode('utf-8')
    server_message = json.loads(server_request)["content"]
    nickname = input(server_message)

    data = {"content": nickname, "user": nickname}
    data_serialized = json.dumps(data)

    s.sendall(data_serialized.encode('utf-8'))

    clear_console()
    print("===================================")
    print("Comandos Disponíveis: ")
    print("/USUARIOS: Lista os usuários conectados")
    print("/SAIR: Desconectar-se do chat")
    print("===================================")

    receive_thread = threading.Thread(target=receiveMessages)
    receive_thread.start()
    send_thread = threading.Thread(target=sendMessages, args=[nickname])
    send_thread.start()
    while True:
        if not (receive_thread.is_alive() and send_thread.is_alive()):
            break


def receiveMessages():
    while True:
        try:
            message = json.loads(s.recv(1024).decode('utf-8'))

            if message["user"] == "SERVER":
                print(message['content'])
            else:
                print(
                    f"{message['time']} - {message['user']}: {message['content']}")
        except:
            break


def sendMessages(nickname: str):
    while True:
        time = datetime.now().strftime("%H:%M:%S")
        message = input()
        print("\033[1A" + "\033[K", end="")
        print(f"{time} - Voce: {message}")
        data = {"content": message,  "user": nickname}
        data_serialized = json.dumps(data)

        if message == Command.DISCONNECT:
            clear_console()
            s.close()
            break

        s.sendall(data_serialized.encode('utf-8'))


HOST = "localhost"
PORT = 6789

while True:
    print("Digite /ENTRAR para conectar-se")
    message_ = input()
    if message_ == Command.JOIN:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        join()
    elif message_ == Command.QUIT:
        break
    else:
        print("Comando inválido: ", message_)
