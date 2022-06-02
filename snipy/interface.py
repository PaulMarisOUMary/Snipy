from .connection import IPV4Connection
from .system import SYSTEM, HOST

import socket

class Interface():
    def __init__(self, socket_family = socket.AF_INET) -> None:
        if SYSTEM == "linux":
            socketProtocol = socket.IPPROTO_TCP
        elif SYSTEM == "windows":
            socketProtocol = socket.IPPROTO_IP
        elif SYSTEM == "darwin":
            socketProtocol = socket.IPPROTO_ICMP
        else:
            raise ValueError("Unsupported system")

        # Create a raw socket and bind it to the public interface
        self.__sock = socket.socket(
            family=socket_family, 
            type=socket.SOCK_RAW, 
            proto=socketProtocol
        )
        self.__sock.bind((HOST, 0))

        # Include IP headers
        self.__sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        # Receive all packages
        self.__sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    def close(self) -> None:
        self.__sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

    def recv(self) -> IPV4Connection:
        return IPV4Connection(*self.__sock.recvfrom(65565))