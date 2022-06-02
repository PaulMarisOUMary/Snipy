from platform import system as _system

import socket

SYSTEM: str = _system().lower()
HOSTNAME: str = socket.gethostname()
HOST: str = socket.gethostbyname(HOSTNAME)