from abc import ABC, abstractmethod
from enum import Enum
from uuid import uuid4


class DeviceType(str, Enum):
    LAMP = "lamp"
    TELEVISION = "television"
    TEMP_SENSOR = "temp_sensor"
    UNIDENTIFIED = "unidentified"


class Device(ABC):
    def __init__(self, type) -> None:
        self.id = uuid4()
        self.type: DeviceType = type

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def list_actions(self):
        pass

    @abstractmethod
    def perform_action(self, command: str):
        pass
