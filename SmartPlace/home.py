from devices.device import DeviceType
from devices.lamp import Lamp

host_port = ('225.0.0.250', 5007)

lamp = Lamp(DeviceType.LAMP)

lamp.connect(host_port)
