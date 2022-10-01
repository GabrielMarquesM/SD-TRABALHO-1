from enum import Enum
import random
from devices.device import Device

# Este dispositivo vai atuar como sensor contínuo, que envia a cada ciclo de X segundos um valor para o Gateway

# esse device vamos ter que tratar de maneira diferente

class Actions(str, Enum):
    SHOW_TEMPERATURE = 1
    CHANGE_SCALE = 2
    GET_INFO = 3

class TempSensor(Device):
    def __init__(self, type) -> None:
        super().__init__(type)
        self.scale: str = "Celsius"
        self.temperature: float = 0.0

    def actions_to_string(self, enum: Actions):
        match enum:
            case Actions.SHOW_TEMPERATURE:
                return "Mostrar temperatura em tempo real"
            case Actions.CHANGE_SCALE:
                return "Mudar escala - (Celsius | Fahrenheit)"
            case Actions.GET_INFO:
                return "Ver informações"
    
    def calculate_temperature(self):
        value = random.uniform(25.5, 40.5)
        if self.scale == "Celsius":
            return ""+round(value, 1)+"C"
        if self.scale == "Fahrenheit":
            value_f = (value * (9/5)) + 32
            return ""+round(value_f, 1)+"F"
    
    def show_temperature(self):
        pass
    
    def get_info(self):
        info = "Info."
        return info
    
    def list_actions(self):
        msg = f"{self.type} - Lista de comandos\n"
        for id in Actions:
            msg += f"{id.value} - {self.actions_to_string(id)}\n"
        msg += "Dispositivo Desejado - Comando: "
        return msg

    def perform_action(self, command: str):
        pass
    

