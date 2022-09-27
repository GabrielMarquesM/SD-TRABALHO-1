import socket
import threading
from select import select

ADDRESS = 'localhost'
MCAST_PORT = 6789
CLIENT_PORT = 5678

devices = {1: 'lamp', 2: 'television', 3: 'temperature sensor'}


def connect_to_client():
    sock_client.bind((ADDRESS, CLIENT_PORT))
    sock_client.listen(1)
    while True:
        # print(devices_to_str())
        try:
            client, address = sock_client.accept()
            #msg = Message("Nickname: ", server_name).toJSON()

            client.send(devices_to_str().encode('utf-8'))
            selected_id = client.recv(1024).decode('utf-8')
            print(f"Dispositivo escolhido: {devices[int(selected_id)]}")
            # serialized_response = json.loads(client.recv(1024).decode('utf-8'))
            # response = Message(**serialized_response)
            # nickname = response.content"
            # client_thread = threading.Thread(
            #     target=handle_command, args=[client])
            # client_thread.start()
        except Exception as err:
            print("Connection failed.")
            print(err)


def devices_to_str():
    msg = "Lista de dispositivos: \n"
    for id in devices.keys():
        msg += f"{id} - {devices[id]}\n"
    msg += "Digite o id do dispositivo desejado: "
    return msg


def handle_command(client: socket):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)

            break
        except:
            break


msg2 = 'Identifique o tipo do device'

sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# sock_multcast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock_multcast.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sock_multcast.bind((ADDRESS, MCAST_PORT))
# sock_multcast.sendto(bytes(msg2, 'utf-8'), (ADDRESS, MCAST_PORT))

# print(sock_multcast.recv(1024).decode('utf-8'))

connect_to_client()
# sock_multcast.close()
