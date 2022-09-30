from enum import Enum

from devices.device import Device


class Color(str, Enum):
    WHITE = "Branco"
    RED = "Vermelho"
    GREEN = "Verde"
    BLUE = "Azul"
    YELLOW = "Amarelo"
    ORANGE = "Laranja"


class Actions(str, Enum):
    CHANGE_COLOR = 1
    CHANGE_INTENSITY = 2
    SWITCH_POWER = 3


class Lamp(Device):
    def __init__(self, type) -> None:
        super().__init__(type)
        self.color: Color = Color.WHITE
        self.status: bool = True
        self.intensity: float = 0.5

    def actions_to_string(self, enum: Actions):
        match enum:
            case Actions.CHANGE_COLOR:
                return "Trocar cor"
            case Actions.CHANGE_INTENSITY:
                return "Mudar intensidade"
            case Actions.SWITCH_POWER:
                return "Ligar/Desligar"

    def change_color(self, color: Color):
        self.color = color

    def get_info(self):
        pass

    def list_actions(self):
        r = f"{self.type} - Lista de comandos\n"
        for id in Actions:
            r += f"{id.value} - {self.actions_to_string(id)}\n"
        return r

    def perform_action(self, command: Actions):
        pass
