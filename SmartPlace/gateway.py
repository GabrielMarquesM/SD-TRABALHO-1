import json
import socket
import threading
import time
from collections import deque
from enum import Enum

ADDRESS = 'localhost'
MCAST_GRP = '225.0.0.250'
MCAST_PORT = 5007
CLIENT_PORT = 5678
DEVICE_PORT = 4321
MULTICAST_TTL = 2
DISCOVER_SLEEP_TIME = 5


class Requests(str, Enum):
    IDENTIFY = "IDENTIFY"
    CMD = "CMD"
    LIST_ACTIONS = "LIST_ACTIONS"


def connect_client():
    while True:
        try:
            client, address = sock_client.accept()
            client.send(devices_to_str().encode('utf-8'))
            id = client.recv(10240).decode('utf-8')
            # Cliente escolhe device
            if id in devices.keys():
                msg = {"type": Requests.LIST_ACTIONS,
                       "command": "", "target": id}
                send_cmd(msg)
                # Espera pela lista de comandos do device escolhido
                while not message_queue:
                    pass
                command_list = message_queue.popleft()
                client.send(command_list.encode('utf-8'))
                selected_cmd = client.recv(10240).decode('utf-8')

                msg = {"type": Requests.CMD,
                       "command": selected_cmd, "target": id}
                send_cmd(msg)
                # Espera pela info dos devices
                # while not message_queue:
                #     pass
                # command_list = message_queue.popleft()
                # print(command_list)
            else:
                client.send("Id Invalido".encode('utf-8'))

        except Exception as err:
            print("Connection failed. (connect_client)")
            print(err)


def devices_to_str():
    msg = "Lista de dispositivos: \n"
    i = 1
    for id in devices.keys():
        device = devices[id]
        msg += f"{id} - {device['type']}\n"
        i += 1
    msg += "Digite o id do dispositivo desejado: "
    return msg


def init_multicast():
    msg = {"type": Requests.IDENTIFY, "command": "", "target": "all"}
    serialized_msg = json.dumps(msg)

    while True:
        try:
            sock_multcast.sendto(bytes(serialized_msg, 'utf-8'),
                                 (MCAST_GRP, MCAST_PORT))
            time.sleep(DISCOVER_SLEEP_TIME)
        except Exception as err:
            print("Connection failed. (init_multicast)")
            print(err)


def send_cmd(msg: dict):
    try:
        serialized_msg = json.dumps(msg)
        sock_multcast.sendto(bytes(serialized_msg, 'utf-8'),
                             (MCAST_GRP, MCAST_PORT))
    except Exception as err:
        print("Command failed. (send_cmd)")
        print(err)


def handle_device_msgs(sock_device: socket):
    while True:
        try:
            message = json.loads(
                sock_device.recv(1024).decode('utf-8'))
            if message["req_type"] == Requests.IDENTIFY:
                if message["id"] not in devices:
                    devices[message["id"]] = {"type": message["type"],
                                              "address": message["address"], "port": message["port"]}
                    print(f"Dispositivo adicionado: {message['type']}")

            if message["req_type"] == Requests.CMD:
                message_queue.append(message["content"])

            if message["req_type"] == Requests.LIST_ACTIONS:
                message_queue.append(message["content"])

        except Exception as err:
            print(err)
            break


def connect_devices():
    sock_device = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_device.bind((ADDRESS, DEVICE_PORT))
    sock_device.listen(1)

    while True:
        try:
            device, address = sock_device.accept()
            device_thread = threading.Thread(
                target=handle_device_msgs, args=[device])
            device_thread.start()

        except Exception as err:
            print("Connection failed. (connect_devices)")
            print(err)
            # sock_device.close()
            break


def initialize():
    print("Gateway initialized.")

    multicast = threading.Thread(target=init_multicast)
    device_listener = threading.Thread(
        target=connect_devices)
    client_socket = threading.Thread(
        target=connect_client)

    multicast.start()
    device_listener.start()
    client_socket.start()


sock_multcast = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock_multcast.setsockopt(
    socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

devices = {}
message_queue = deque()

sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_client.bind((ADDRESS, CLIENT_PORT))
sock_client.listen(1)

initialize()

# sock_multcast.close()
# sock_client.close()
