from enum import Enum

from devices.device import Device


class Color(str, Enum):
    WHITE = "Branco"
    RED = "Vermelho"
    GREEN = "Verde"
    BLUE = "Azul"
    YELLOW = "Amarelo"
    ORANGE = "Laranja"


class Lamp(Device):
    def __init__(self, type) -> None:
        super().__init__(type)
        self.color: Color = Color.WHITE

    def change_color(self, color: Color):
        self.color = color

    def get_info(self):
        pass

    def list_actions(self):
        pass

    def perform_action(self, command: str):
        pass
