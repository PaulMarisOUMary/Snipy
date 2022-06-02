from .system import SYSTEM

import socket

class Connection():
    def __init__(self, raw_data, host):
        self.raw_data = raw_data
        self.host = host

        self.destination: str = None
        self.source: str = None
        self.protocol: str = None

class Interface():
    def __init__(self) -> None:
        if SYSTEM == "linux":
            socketProtocol = socket.IPPROTO_TCP
        elif SYSTEM == "windows":
            raise NotImplementedError # IPPROTO_IP
        elif SYSTEM == "darwin":
            socketProtocol = socket.IPPROTO_ICMP # Wrong working only on local
        else:
            raise ValueError("Unsupported system")

        self.__sock: socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_RAW, proto=socketProtocol)

    def recv(self) -> Connection:
        return Connection(*self.__sock.recvfrom(65565))