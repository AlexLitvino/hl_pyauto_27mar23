from L17.p2_facade.BluetoothController import BluetoothController
from L17.p2_facade.PCBController import PCBController
from L17.p2_facade.WiFiController import WiFiController


class SystemController:

    def __init__(self):
        self._pcb_controller = PCBController()
        self._wifi_controller = WiFiController()
        self._bluetooth_controller = BluetoothController()

    def init(self):
        self._pcb_controller.turn_on()
        self.enable_communication()

    def disable_communication(self):
        self._wifi_controller.turn_off_wifi()
        self._bluetooth_controller.turn_off_bluetooth()

    def enable_communication(self):
        self._wifi_controller.turn_on_wifi()
        self._bluetooth_controller.turn_on_bluetooth()

    def shutdown(self):
        self.disable_communication()
        self._pcb_controller.turn_off()


if __name__ == '__main__':

    system_controller = SystemController()
    system_controller.init()
    # testing
    system_controller.disable_communication()
    # testing
    system_controller.shutdown()
