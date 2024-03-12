class EntertainmentDevice:
    def connect_device_to_power_outlet(self, device): pass


class ConnectRca:
    def rca_connect(self, obj):
        pass


class ConnectHDMI:
    def hdmi_connect(self, obj):
        pass


class ConnectETH:
    def eth_connect(self, obj):
        pass


class Television(EntertainmentDevice, ConnectRca, ConnectHDMI):
    def connect_to_dvd(self, dvd_player):
        super().rca_connect(dvd_player)

    def connect_to_game_console(self, game_console):
        super().hdmi_connect(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class DVDPlayer(EntertainmentDevice, ConnectHDMI):
    def connect_to_tv(self, television):
        super().hdmi_connect(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(EntertainmentDevice, ConnectHDMI, ConnectETH):
    def connect_to_tv(self, television):
        super().hdmi_connect(television)

    def connect_to_router(self, router):
        super().eth_connect(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EntertainmentDevice, ConnectETH):
    def connect_to_tv(self, television):
        super().eth_connect(television)

    def connect_to_game_console(self, game_console):
        super().eth_connect(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)
