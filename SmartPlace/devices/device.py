import socket
import struct
import time
from abc import ABC, abstractmethod
from enum import Enum
from uuid import uuid4


class Requests(str, Enum):
    IDENTIFY = "Identifique-se device"
    CMD = "Comando"


class DeviceType(str, Enum):
    LAMP = "lamp"
    TELEVISION = "television"
    TEMP_SENSOR = "temp_sensor"
    UNIDENTIFIED = "unidentified"


class Device(ABC):
    def __init__(self, type) -> None:
        self.id = uuid4()
        self.type: DeviceType = type
        self.sock = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def list_actions(self):
        pass

    @abstractmethod
    def perform_action(self, command: str):
        pass

    def connect(self, host_port):
        self.sock.setsockopt(
            socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.sock.bind(('', host_port[1]))

        mreq = struct.pack('4sl', socket.inet_aton(
            host_port[0]), socket.INADDR_ANY)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        while True:
            try:
                request = self.sock.recv(10240).decode('utf-8')
                print(request)
                if request == Requests.IDENTIFY:
                    msg_ = f"Oi, sou o {self.type}"
                    self.sock.sendto(msg_.encode("utf-8"), host_port)
                    print("Mandei mensagem")
            except:
                print("Fui incapaz de mandar mensagem")
                break
