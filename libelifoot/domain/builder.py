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

from typing import Self, Optional

from libelifoot.use_case.dto import (
    Equipa,
    Player
)
from libelifoot.file.equipa import EquipaFileHandler


class EquipaBuilder:

    def __init__(self):
        self._equipa = None

    def create_base_equipa(self, equipa_file: str) -> Self:
        self._equipa = EquipaFileHandler.read(equipa_file)
        # we are not interested on the players to create the base equipa
        self._equipa.players.clear()

        return self

    def add_players(self, players: list[Player]) -> Self:
        if self._equipa:
            self._equipa.players = players

        return self

    def add_coach(self, coach: str) -> Self:
        if self._equipa and coach:
            self._equipa.coach = coach

        return self

    def build(self) -> Optional[Equipa]:
        return self._equipa
