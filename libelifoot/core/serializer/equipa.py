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

from typing import Any

from libelifoot.core.serializer.interface import ISerializer
from libelifoot.core.serializer.coach import CoachSerializer
from libelifoot.core.serializer.player import PlayerSerializer
from libelifoot.core.util.crypto import encrypt


class EquipaSerializer(ISerializer):

    @staticmethod
    def serialize(obj: Any) -> bytearray:
        equipa = bytearray(b'EFa' + b'\x00' * 47)
        equipa += encrypt(obj.ext_name)
        equipa += encrypt(obj.short_name)
        equipa += bytearray(obj.colors.background + b'\x00')
        equipa += bytearray(obj.colors.text + b'\x00')
        equipa += encrypt(obj.country)
        equipa += bytearray(obj.level.to_bytes())
        equipa += bytearray(len(obj.players).to_bytes())
        for p in obj.players:
            equipa += PlayerSerializer.serialize(p)

        equipa += CoachSerializer.serialize(obj.coach)

        return equipa
