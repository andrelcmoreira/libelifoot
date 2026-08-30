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

from libelifoot.domain.entity.color import Color as ColorEntity


@dataclass
class Color:
    background: bytes
    text: bytes

    def __str__(self) -> str:
        return '#' + self.background.hex().upper() + ', #' \
            + self.text.hex().upper()

    @classmethod
    def from_entity(cls, entity: ColorEntity):
        return cls(
            background=entity.background,
            text=entity.text
        )
