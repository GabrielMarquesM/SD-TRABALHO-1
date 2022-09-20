
import json
import socket
import threading
from enum import Enum

from message import Message


class UserCommand(str, Enum):
    USERS = "/USUARIOS"


def initialize():
    while True:
        try:
            client, address = s.accept()
            msg = Message("Nickname: ", server_name).toJSON()
            client.send(msg.encode())
            serialized_response = json.loads(client.recv(1024).decode())
            response = Message(**serialized_response)
            nickname = response.content

            clients[nickname] = client

            joinedMsg = f"--- {nickname} entrou ---"

            print(joinedMsg)
            messageToAll(Message(joinedMsg, server_name), client)

            client_thread = threading.Thread(target=handleMsg, args=[nickname])
            client_thread.start()
        except:
            print("Failed to initialize")

# Mensagem para o grupo todo


def messageToAll(message: Message, sender: socket):
    response = message.toJSON()
    for client in clients.values():
        if client != sender:
            client.send(response.encode("utf-8"))


def getUsers():
    user_list = f"| LISTA DE USUARIOS - {len(clients)} ONLINE"
    for nickname in clients.keys():
        user_list += "\n| * " + nickname
    return Message(user_list, server_name).toJSON()


def handleMsg(nickname):
    #id = clients.index(client)
    client = clients[nickname]
    while True:
        try:
            message_serialized = json.loads(client.recv(1024).decode('utf-8'))
            message = Message(**message_serialized)
            if message.content == UserCommand.USERS:
                userList = getUsers()
                client.send(userList.encode('utf-8'))
            else:
                messageToAll(message, client)
        except:
            disconnectClient(nickname)
            break

# Problema:
# Caso um cliente mais antigo desconecte antes de um mais novo
# Uma exceção é lançada out of range é lançada em relação ao ID
# Ex: cliente 1 desconecta, cliente 0 desconecta, OK
# Ex: cliente 0 desconecta, cliente 1 desconecta:
#     response = f" --- {nicknames[id]} saiu --- : IndexError: list index out of range"


def disconnectClient(nickname):

    response = f" --- {nickname} saiu --- "
    print(response)
    messageToAll(Message(response, server_name), clients[nickname])
    clients.pop(nickname)


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
