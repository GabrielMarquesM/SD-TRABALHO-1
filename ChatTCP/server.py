import socket
import threading

HOST = "localhost"
PORT = 6789

# socket.AF_INET suporta endereços http, ipv4
# socket.SOCK_STREAM é TCP 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))



clients = [] # clientes que estão conectados
nicknames = [] # como esse cliente vai ser identificado (nome)

def initialize():
    # Faz mais sentido eu receber o Host e Port no initialize?
    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.settimeout(20.0)

    while True:
        client, address = s.accept()
        # Mandar uma mensagem ao cliente perguntando o nome dele (client.send('Nickname: '))
        client.send().encode()
        nickname = client.recv(1024).decode()
        # Usar um dicionário é melhor??
        clients.append(client)
        nickname.append(nickname)
        messageToAll("Entrou".encode())
        client_thread = threading.Thread(target=handleMsn, args=(client))
        client_thread
        try:
            print("Eita")
        except:
            print("Show")
            s.close()

# Aqui seria a mensagem para o grupo todo
def messageToAll():
    pass

# aqui vai ter varias threads cada uma com um client diferente
def handleMsn():
    while True:
        try:
            pass
        except:
            break

# o initialize vai estar recebendo as connecções e cada conecção vai começar uma thread
initialize()
