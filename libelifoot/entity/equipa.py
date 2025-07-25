from dataclasses import dataclass

from libelifoot.entity.color import Color
from libelifoot.entity.player import Player


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
        return (
            f'extended name:\t{self.ext_name}\n'
            f'short name:\t{self.short_name}\n'
            f'country:\t{self.country}\n'
            f'colors:\t\t{self.colors} (text, background)\n'
            f'level:\t\t{self.level}\n'
            f'coach:\t\t{self.coach}\n'
            f'players:\t{self.players}'
        )
