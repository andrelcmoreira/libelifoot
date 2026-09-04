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

from libelifoot.domain.repository.equipa import IEquipaRepository
from libelifoot.infrastructure.eft.serializer.equipa import EquipaSerializer
from libelifoot.use_case.dto.equipa import Equipa
from libelifoot.use_case.cmd import ICmd


class SaveEquipa(ICmd):

    def __init__(
        self,
        file_name: str,
        equipa: Equipa,
        repository: IEquipaRepository
    ):
        self._file_name = file_name
        self._equipa = equipa
        self._repo = repository

    def run(self) -> Any:
        data = EquipaSerializer.serialize(self._equipa)

        if data:
            self._repo.save(self._file_name, bytes(data))
