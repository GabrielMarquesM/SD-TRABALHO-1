from devices.device import DeviceType
from devices.lamp import Lamp
from devices.television import Television
from devices.temp_sensor import TempSensor

lamp = Lamp(DeviceType.LAMP)
# television = Television(DeviceType.TELEVISION)
sensor = TempSensor(DeviceType.TEMP_SENSOR)
