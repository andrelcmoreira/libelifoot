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

from typing import Optional

from libelifoot.domain.repository.equipa import IEquipaRepository


def get_equipa_repository() -> IEquipaRepository:
    return FileEquipaRepository()


class FileEquipaRepository(IEquipaRepository):

    def get(self, equipa_file: str) -> Optional[bytes]:
        """
        Retrieve an equipa by its file name.

        :equipa_file: The equipa file name.
        :return: The Equipa object if found, otherwise None.
        """
        try:
            with open(equipa_file, 'rb') as f:
                return f.read()
        except FileNotFoundError:
            return None

    def save(self, equipa_file: str, data: bytes) -> None:
        """
        Save an equipa to the repository.

        :equipa_file: The equipa file name.
        :equipa: The Equipa object to save.
        """
        with open(equipa_file, 'wb') as f:
            if data:
                f.write(data)
