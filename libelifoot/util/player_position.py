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

from enum import Enum


class PlayerPosition(Enum):
    U = -1 # unknown
    G = 0  # goalkeeper
    D = 1  # defender
    M = 2  # midfielder
    A = 3  # forward ('atacante' in portuguese)

    @staticmethod
    def to_pos_code(pos: str) -> int:
        match pos:
            case PlayerPosition.G.name: return PlayerPosition.G.value
            case PlayerPosition.D.name: return PlayerPosition.D.value
            case PlayerPosition.M.name: return PlayerPosition.M.value
            case PlayerPosition.A.name: return PlayerPosition.A.value

        return PlayerPosition.U.value

    @staticmethod
    def to_pos_name(pos_code: int) -> str:
        match pos_code:
            case PlayerPosition.G.value: return PlayerPosition.G.name
            case PlayerPosition.D.value: return PlayerPosition.D.name
            case PlayerPosition.M.value: return PlayerPosition.M.name
            case PlayerPosition.A.value: return PlayerPosition.A.name

        return PlayerPosition.U.name
