from ..system import SYSTEM

"""
- Support LINUX
! need testing on:
!- Windows
!- MacOS
"""

class Refresher():
    def __init__(self, array: list) -> None:
        """Initialize Refresher using array's content."""
        self.ESC = "\x1B"
        self.last = array

        print('\n'*len(array))

    def __to_latest_up(self) -> str:
        """Return ESC sequence to move cursor to the first line."""
        return f"{self.ESC}[{len(self.last)+1}A"

    def cleanup(self) -> None:
        """Clean previous console content."""
        text = self.__to_latest_up()

        for item in self.last:
            text += f"{' '*len(item)}\n"

        print(text)

    def log(self, array: list) -> None:
        """Update console with array's content."""
        self.cleanup()
        text = self.__to_latest_up()

        for item in array:
            text += f"{item}\n"

        print(text)
        self.last = array