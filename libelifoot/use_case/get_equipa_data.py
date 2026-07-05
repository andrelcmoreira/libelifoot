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

from libelifoot.domain.interface import ICmd
from libelifoot.domain.repository import IEquipaRepository
from libelifoot.domain.parser.equipa import EquipaParser
from libelifoot.domain.error import (
    EquipaHeaderNotFound,
    EquipaNotFound
)


class Cmd(ICmd):

    def __init__(self, equipa: str, repository: IEquipaRepository):
        self._equipa = equipa
        self._repo = repository

    def run(self) -> Any:
        data = self._repo.get_equipa(self._equipa)
        if not data:
            raise EquipaNotFound(self._equipa)

        ep = EquipaParser(data)

        if not ep.has_equipa_header(data):
            raise EquipaHeaderNotFound(self._equipa)

        return ep.parse()
