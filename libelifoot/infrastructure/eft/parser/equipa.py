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

from libelifoot.domain.entity.equipa import Equipa
from libelifoot.domain.entity.player import Player
from libelifoot.domain.entity.color import Color
from libelifoot.domain.util import crypto
from libelifoot.domain.util.offset import Offsets, OffsetCalculator
from libelifoot.domain.util.sizes import Sizes
from libelifoot.infrastructure.eft.parser.base_parser import BaseParser
from libelifoot.infrastructure.eft.parser import player


class EquipaParser(BaseParser):

    def __init__(self, equipa_data: bytes):
        if not equipa_data:
            raise ValueError("equipa data cannot be empty.")

        self._data = equipa_data

    def has_equipa_header(self, data: bytes) -> bool:
        start_offs = Offsets.HEADER_START.value
        end_offs = Offsets.HEADER_END.value + 1

        return data[start_offs:end_offs] == b'EFa' + b'\x00' * 47

    def parse_ext_name(self, data: bytes) -> str:
        offs = OffsetCalculator.get_extended_name()
        size = data[Sizes.HEADER.value]

        return crypto.decrypt(data, offs, size)

    def parse_short_name(self, data: bytes, ext_len: int) -> str:
        offs = OffsetCalculator.get_short_name(ext_len)

        return crypto.decrypt(data, offs + 1, data[offs])

    def parse_colors(self, data: bytes, ext_len: int, short_len: int) -> Color:
        offs = OffsetCalculator.get_colors(ext_len, short_len)
        bg = self.get_field(data, offs, Sizes.COLOR.value)
        txt = self.get_field(data, offs + Sizes.COLOR.value + 1,
                             Sizes.COLOR.value)

        return Color(background=bg, text=txt)

    def parse_level(self, data: bytes, ext_len: int, short_len: int) -> int:
        offs = OffsetCalculator.get_level(ext_len, short_len)
        level = self.get_field(data, offs, Sizes.LEVEL.value)

        return int(level.hex(), 16)

    def parse_country(self, data: bytes, ext_len: int, short_len: int) -> str:
        offs = OffsetCalculator.get_country(ext_len, short_len)

        return crypto.decrypt(data, offs, Sizes.COUNTRY.value - 1) # to skip the size byte

    def parse_players(
        self,
        data: bytes,
        ext_len: int,
        short_len: int
    ) -> list[Player]:
        players_offs = OffsetCalculator.get_players(ext_len, short_len)
        count_offs = OffsetCalculator.get_players_number(ext_len, short_len)
        pp = player.PlayersParser(data, players_offs, count_offs)

        return pp.parse()

    def parse_coach(self, data: bytes, ext_len: int, short_len: int) -> str:
        offs = OffsetCalculator.get_coach(data, ext_len, short_len)
        if offs > len(data): # no coach information available
            return ''

        return crypto.decrypt(data, offs + 1, data[offs])

    def parse(self) -> Equipa:
        ext_name = self.parse_ext_name(self._data)
        short_name = self.parse_short_name(self._data, len(ext_name))
        colors = self.parse_colors(self._data, len(ext_name), len(short_name))
        level = self.parse_level(self._data, len(ext_name), len(short_name))
        coach = self.parse_coach(self._data, len(ext_name), len(short_name))
        players = self.parse_players(self._data, len(ext_name), len(short_name))
        country = self.parse_country(self._data, len(ext_name), len(short_name))

        return Equipa(ext_name=ext_name, short_name=short_name, country=country,
                      level=level, colors=colors, coach=coach, players=players)
