import socket
import threading


def join():
    address = input("IP: ")
    port = input("Porta: ")
    try:
        s.connect((address, int(port)))
    except:
        print("Conexão mal-sucedida, tente novamente.")
        return
    # Servidor pede nickname
    nickname_request = s.recv(1024).decode()
    response = input(nickname_request)
    s.sendall(response.encode('utf-8'))

    print("\n\n===================================")
    receive_thread = threading.Thread(target=receiveMessages)
    receive_thread.start()
    send_thread = threading.Thread(target=sendMessages)
    send_thread.start()
    while True:
        if not (receive_thread.is_alive() and send_thread.is_alive()):
            break


def receiveMessages():
    while True:
        try:
            server_response = s.recv(1024).decode()
            print(server_response)
        except ConnectionError:
            break


def sendMessages():
    while True:
        message = input("")
        if message == "/SAIR":
            disconnect()
            break

        s.sendall(message.encode('utf-8'))


def disconnect():
    s.close()


HOST = "localhost"
PORT = 6789

while True:
    print("Digite /ENTRAR para conectar-se")

    message_ = input()
    if message_ == "/ENTRAR":
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        join()
    elif message_ == "q":
        break
    else:
        print("Comando inválido: ", message_)
