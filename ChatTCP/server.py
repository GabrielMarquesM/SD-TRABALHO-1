import socket
import threading


def initialize():
    while True:
        client, address = s.accept()
        try:
            client.send("Nickname: ".encode())
            nickname = client.recv(1024).decode()
            print(f"{nickname} entrou")

            clients.append(client)
            nicknames.append(nickname)

            messageToAll(f" --- {nickname} entrou --- ", client)

            client_thread = threading.Thread(target=handleMsg, args=[client])
            client_thread.start()

        except:
            print("Failed to initialize")

# Aqui seria a mensagem para o grupo todo


def messageToAll(message, sender):
    for client in clients:
        if client != sender:
            client.send(message.encode("utf-8"))


# aqui vai ter varias threads cada uma com um client diferente

def users_toString():
    user_list = f"| LISTA DE USUARIOS - {len(nicknames)} ONLINE"
    for nickname in nicknames:
        user_list += "\n| * " + nickname
    return user_list


def handleMsg(client):
    id = clients.index(client)
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "/USUARIOS":
                userList = users_toString()
                client.send(userList.encode('utf-8'))
            else:
                message = f"{nicknames[id]}: {message}"
                messageToAll(message, client)
        except ConnectionError:
            disconnectClient(id)
            break


def disconnectClient(id):
    res = f"{nicknames[id]} saiu"
    print(res)
    messageToAll(f" --- {res} --- ", clients[id])
    del clients[id]
    del nicknames[id]


HOST = ""
PORT = 6789

# socket.AF_INET suporta endereços http, ipv4
# socket.SOCK_STREAM é TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    clients = []  # clientes que estão conectados
    nicknames = []  # como esse cliente vai ser identificado (nome)

    # o initialize vai estar recebendo as connecções e cada conecção vai começar uma thread
    initialize()
