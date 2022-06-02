import struct
import ctypes

class IPV4Connection(ctypes.Structure):
    """Header:
            04 bits | Protocol version
            04 bits | Header length
            08 bits | Type of service
            16 bits | Total length
            16 bits | Identification
            03 bits | Flags :
                - 01 bits | Null bit
                - 01 bits | Don't fragment
                - 01 bits | More fragments
            13 bits | Fragment offset
            08 bits | Time to leave
            08 bits | Protocol
            16 bits | Header checksum
            32 bits | Source IP
            32 bits | Destination IP

            -> Minimum header length == 20 bytes (160 bits)
            -> Maximum header length == 60 bytes (480 bits)
        Option:
            00 - 40 bytes | Options
        Data:
            20 - 65535 bytes | Data

    (32 bits == 4 bytes)

    from RFC 791
    """

    _fields_ = [
        ("version",         ctypes.c_ubyte, 4),
        ("header_length",   ctypes.c_ubyte, 4),
        ("type_of_service", ctypes.c_ubyte, 8),
        ("total_length",    ctypes.c_ubyte, 16),
        ("identification",  ctypes.c_ubyte, 16),
        ("flags",           ctypes.c_ubyte, 3),
        ("fragment_offset", ctypes.c_ubyte, 13),
        ("time_to_leave",   ctypes.c_ubyte, 8),
        ("protocol",        ctypes.c_ubyte, 8),
        ("header_checksum", ctypes.c_ubyte, 16),
        ("source",          ctypes.c_ubyte, 32),
        ("destination",     ctypes.c_ubyte, 32)
    ]

    def __init__(self, raw_data: bytes, host: tuple[str, int]):
        self.raw_data = raw_data
        self.host = host[0]
        #self.header = 

        self.__dig_header()

    def __str__(self) -> str:
        raise NotImplementedError
        #return f"[{self.protocol}] | {self.host} | {self.source} -> {self.destination}"

    def __dig_header(self) -> None:
        raise NotImplementedError
