import socket

class Snipy():
    def __init__(self, array: list) -> None:
        self.ESC = "\x1B"
        self.last = array

        print('\n'*len(array))

    def __to_latest_up(self) -> str:
        return f"{self.ESC}[{len(self.last)+1}A"

    def cleaner(self) -> None:
        text = self.__to_latest_up()

        for item in self.last:
            text += f"{' '*len(item)}\n"

        print(text)

    def log(self, array: list) -> None:
        self.cleaner()
        text = self.__to_latest_up()

        for item in array:
            text += f"{item}\n"

        print(text)
        self.last = array

def main(blinds: list):
    known_list: dict = {}
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

    snipy = None

    while True:
        raw_data, address = sniffer.recvfrom(65535)

        if address[0] in blinds:
            continue
        
        if not address[0] in known_list:
            known_list[address[0]] = 1
        else:
            known_list[address[0]] += 1

        array = []
        array.append(f"Known: [{len(known_list)}] | Last: {address[0]} ({known_list[address[0]]})")
        for key, value in known_list.items():
            array.append(f"{key} ({value})")
        
        if not snipy:
            snipy = Snipy(array)

        snipy.log(array)

blind = input("[*] Enter the IP address to hide: ")

main(blind.split(' '))