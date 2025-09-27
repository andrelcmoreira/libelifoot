from dataclasses import dataclass


@dataclass
class Color:

    text: bytes
    background: bytes

    def __str__(self) -> str:
        return '#' + self.background.hex().upper() + ', #' \
            + self.text.hex().upper()
