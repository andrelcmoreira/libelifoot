# Copyright (C) 2025 André L. C. Moreira <andrelcmoreira@proton.me>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from dataclasses import dataclass


@dataclass
class Color:
    background: bytes
    text: bytes

    def __str__(self) -> str:
        return '#' + self.background.hex().upper() + ', #' \
            + self.text.hex().upper()


@dataclass
class Player:
    name: str
    position: str
    country: str
    appearances: int = 0
    value: float = 0.0

    def __str__(self) -> str:
        return f'{self.position}: {self.name} - {self.country}'


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
