import json
import socket
import threading
import time
from enum import Enum

ADDRESS = 'localhost'
MCAST_GRP = '225.0.0.250'
MCAST_PORT = 5007
CLIENT_PORT = 5678
DEVICE_PORT = 4321
MULTICAST_TTL = 2
DISCOVER_SLEEP_TIME = 5


class Requests(str, Enum):
    IDENTIFY = "Identifique-se"
    CMD = "Comando"


def connect_client():
    sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_client.bind((ADDRESS, CLIENT_PORT))
    sock_client.listen(1)
    while True:
        try:
            client, address = sock_client.accept()
            client.send(devices_to_str().encode('utf-8'))
            selected_id = client.recv(10240).decode('utf-8')

            print(f"Dispositivo escolhido: {devices[selected_id]}")
        except Exception as err:
            print("Connection failed.")
            print(err)


def devices_to_str():
    msg = "Lista de dispositivos: \n"
    for id in devices.keys():
        device = devices[id]
        msg += f"{id} - {device['type']}\n"
    msg += "Digite o id do dispositivo desejado: "
    return msg


def handle_command(client: socket):
    while True:
        try:
            message = client.recv(10240).decode('utf-8')
            print(message)
            break
        except:
            break


def init_multicast():
    sock_multcast = socket.socket(
        socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock_multcast.setsockopt(
        socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
    id_msg = 'Identifique-se'
    while True:
        sock_multcast.sendto(bytes(id_msg, 'utf-8'), (MCAST_GRP, MCAST_PORT))
        time.sleep(DISCOVER_SLEEP_TIME)


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
        except:
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
            print("Connection failed.")
            print(err)


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


devices = {}

initialize()
# sock_multcast.close()
