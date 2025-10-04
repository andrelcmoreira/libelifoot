from dataclasses import dataclass

from libelifoot.dto.color import Color
from libelifoot.dto.player import Player


@dataclass
class Equipa:

    ext_name: str
    short_name: str
    country: str
    level: int
    colors: Color
    coach: str
    players: list[Player]

    def __str__(self) -> str:
        players = ', '.join([str(p) for p in self.players])

        return (
            f'extended name:\t{self.ext_name}\n'
            f'short name:\t{self.short_name}\n'
            f'country:\t{self.country}\n'
            f'colors:\t\t{self.colors} (background, text)\n'
            f'level:\t\t{self.level}\n'
            f'coach:\t\t{self.coach}\n'
            f'players:\t{players}'
        )
