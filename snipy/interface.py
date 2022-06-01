from .system import SYSTEM

import socket

class Interface():
    def __init__(self) -> None:
        if SYSTEM == "linux":
            self.__sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        elif SYSTEM == "windows":
            raise NotImplementedError
        elif SYSTEM == "darwin":
            raise NotImplementedError