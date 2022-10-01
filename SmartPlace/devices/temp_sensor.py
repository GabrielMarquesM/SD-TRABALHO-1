import random
import threading
import time
from enum import Enum, IntEnum

from devices.device import Device

# Este dispositivo vai atuar como sensor contínuo, que envia a cada ciclo de X segundos um valor para o Gateway

# esse device vamos ter que tratar de maneira diferente


class Actions(IntEnum):
    SHOW_TEMPERATURE = 1
    CHANGE_SCALE = 2
    GET_INFO = 3


class Scale(str, Enum):
    CELSIUS = "C"
    FAHRENHEIT = "F"


class TempSensor(Device):
    def __init__(self, type) -> None:
        super().__init__(type)
        self.scale: str = Scale.CELSIUS
        self.temperature: float = 20.0
        self.actions_map: dict = {Actions.SHOW_TEMPERATURE: self.show_temperature, Actions.CHANGE_SCALE: self.change_scale,
                                  Actions.GET_INFO: self.get_info}
        self.temperature_checker = threading.Thread(
            target=self.calculate_temperature)
        self.temperature_checker.start()

    def actions_to_string(self, enum: Actions):
        match enum:
            case Actions.SHOW_TEMPERATURE:
                return "Mostrar temperatura em tempo real"
            case Actions.CHANGE_SCALE:
                return "Mudar escala - (C | F)"
            case Actions.GET_INFO:
                return "Ver informações"

    def calculate_temperature(self):
        while True:
            value = random.uniform(20.5, 23.5)
            if self.scale == Scale.FAHRENHEIT:
                value = (value * (9/5)) + 32
            self.temperature = round(value, 1)
            time.sleep(3)

    def show_temperature(self):
        return f"{self.temperature} - {self.scale}°"

    def change_scale(self, scale: Scale):
        if not self.is_valid_arg(scale, Scale):
            return "Escala invalida"
        self.scale = scale
        return f"Escala atualizada para {'Fahrenheit' if self.scale == Scale.FAHRENHEIT else 'Celsius'}"

    def get_info(self):
        info = "Info."
        return info

    def list_actions(self):
        msg = f"{self.type} - Lista de comandos\n"
        for id in Actions:
            msg += f"{id.value} - {self.actions_to_string(id)}\n"
        msg += "Dispositivo Desejado - Comando: "
        return msg

    def select_action(self, command: str):
        cmd_args = command.split()
        cmd = cmd_args[0]

        args = ""
        if len(cmd_args) > 1:
            args = cmd_args[1]

        action = self.get_action_by_id(cmd, Actions)

        # No args
        if action == Actions.SHOW_TEMPERATURE:
            return self.show_temperature()

        if action == Actions.GET_INFO:
            return self.get_info()

        return self.actions_map[action](args.upper())
#
