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

from libelifoot.use_case.dto import Player
from libelifoot.core.parser.base_parser import BaseParser
from libelifoot.util.crypto import decrypt
from libelifoot.core.player_position import PlayerPosition
from libelifoot.util.sizes import Sizes


class PlayersParser(BaseParser):

    def __init__(self, data: bytes, players_offs: int, count_offs: int):
        self._data = data
        self._players_offs = players_offs
        self._count_offs = count_offs

    def parse(self) -> list[Player]:
        number_players = self._data[self._count_offs]
        players = []

        for _ in range(0, number_players):
            entry_len = self._data[self._players_offs + Sizes.COUNTRY.value]
            pos_offs = self._players_offs + Sizes.COUNTRY.value + entry_len + 1
            ret = decrypt(self._data, self._players_offs,
                          Sizes.COUNTRY.value + entry_len + 1)

            country = ret[1:4]
            name = ret[5:]
            pos = PlayerPosition.to_pos_name(self._data[pos_offs])

            players.append(Player(name=name, position=pos, country=country))
            # +1 to skip the 'name size' byte
            # +1 to skip the position byte
            # +1 to jump to the next entry
            self._players_offs += Sizes.COUNTRY.value + entry_len + 3

        return players
