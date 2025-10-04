from dataclasses import dataclass


@dataclass
class Color:

    background: bytes
    text: bytes

    def __str__(self) -> str:
        return '#' + self.background.hex().upper() + ', #' \
            + self.text.hex().upper()
