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
    GET_INFO = 4


class StatusPower(str, Enum):
    OFF = "OFF"
    ON = "ON"


class Lamp(Device):
    def __init__(self, type) -> None:
        super().__init__(type)
        self.color: Color = Color.WHITE
        self.status: bool = True
        self.intensity: float = 0.5
        self.actions_map: dict = {Actions.CHANGE_COLOR: self.change_color, Actions.CHANGE_INTENSITY: self.change_intensity,
                                  Actions.SWITCH_POWER: self.switch_power, Actions.GET_INFO: self.get_info}

    def actions_to_string(self, enum: Actions):
        match enum:
            case Actions.CHANGE_COLOR:
                return "Trocar cor - (color, WHITE)"
            case Actions.CHANGE_INTENSITY:
                return "Mudar intensidade - (intensity, 0.x)"
            case Actions.SWITCH_POWER:
                return "Ligar/Desligar - (ON/OFF)"
            case Actions.GET_INFO:
                return "Ver informações"

    def change_color(self, color: Color):
        self.color = color

    def change_intensity(self, intensity: float):
        self.intensity = intensity

    def switch_power(self, status: StatusPower):
        if status == StatusPower.ON:
            self.status = True
        if status == StatusPower.OFF:
            self.status = False

    def get_info(self):
        info = "Info."
        return info

    def list_actions(self):
        msg = f"{self.type} - Lista de comandos\n"
        for id in Actions:
            msg += f"{id.value} - {self.actions_to_string(id)}\n"
        msg += "Dispositivo Desejado - Comando: "
        return msg

    def get_action_by_id(self, id: str):
        for action in Actions:
            #print(action.value, int(id))
            if action.value == int(id):
                return action

    def perform_action(self, command: str):
        # CMD field1:arg1,field2,arg2,field3,arg3

        cmd_args = command.split(" ")
        cmd = self.get_action_by_id(cmd_args[0])
        args = cmd_args[1].split(",")

        args_dict = dict([args])

        #print(cmd, args_dict)

        self.actions_map[cmd](**args_dict)
        return self.get_info()
