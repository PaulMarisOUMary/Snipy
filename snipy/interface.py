from .connection import IPV4Connection
from .system import SYSTEM, HOST

import socket

class Interface():
    def __init__(self, 
        socket_family: socket.AddressFamily = socket.AF_INET,
        socket_type: socket.SocketKind = socket.SOCK_STREAM,
        socket_protocol: int = 0
        ) -> None:

        self.__sock = socket.socket(
            family=socket_family, 
            type=socket_type, 
            proto=socket_protocol
        )

    def recv(self, x = 0xffff) -> bytes:
        return self.__sock.recv(x)