
import json
import socket
import threading
from enum import Enum

from message import Message


class UserCommand(str, Enum):
    USERS = "/USUARIOS"
    DISCONNECT = "/SAIR"


def initialize():
    print("Server initialized.")
    while True:
        try:
            client, address = s.accept()
            msg = Message("Nickname: ", server_name).toJSON()
            client.send(msg.encode('utf-8'))
            serialized_response = json.loads(client.recv(1024).decode('utf-8'))
            response = Message(**serialized_response)
            nickname = response.content

            clients[client] = nickname

            joinedMsg = f"--- {nickname} entrou ---"

            print(joinedMsg)
            messageToAll(Message(joinedMsg, server_name), client)

            client_thread = threading.Thread(target=handleMsg, args=[client])
            client_thread.start()
        except:
            print("Connection failed.")

# Mensagem para o grupo todo


def messageToAll(message: Message, sender: socket):
    response = message.toJSON()
    for client in clients.keys():
        if client != sender:
            client.send(response.encode('utf-8'))


def getUsers():
    user_list = f"| LISTA DE USUARIOS - {len(clients)} ONLINE"
    for nickname in clients.values():
        user_list += "\n| * " + nickname
    return Message(user_list, server_name).toJSON()


def handleMsg(client: socket):
    while True:
        try:
            message_serialized = json.loads(client.recv(1024).decode('utf-8'))
            message = Message(**message_serialized)
            if message.content == UserCommand.USERS:
                userList = getUsers()
                client.send(userList.encode('utf-8'))
            elif message.content == UserCommand.DISCONNECT:
                disconnectClient(client)
            else:
                messageToAll(message, client)
        except:
            # disconnectClient(client)
            break


def disconnectClient(client: socket):
    nickname = clients[client]
    response = f" --- {nickname} saiu --- "
    print(response)
    messageToAll(Message(response, server_name), client)
    clients.pop(client)
    client.close()


HOST = ""
PORT = 6789
server_name = "SERVER"

# socket.AF_INET suporta endereços http, ipv4
# socket.SOCK_STREAM é TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    clients = {}  # clientes que estão conectados

    # o initialize vai estar recebendo as conexões e cada conexão vai começar uma thread
    initialize()
