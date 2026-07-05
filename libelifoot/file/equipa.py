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

from libelifoot.use_case.dto import Equipa
from libelifoot.domain.error import (
    EquipaHeaderNotFound,
    EquipaNotFound
)
from libelifoot.domain.parser.equipa import EquipaParser
from libelifoot.serializer.equipa import EquipaSerializer


class EquipaFileHandler:

    @staticmethod
    def write(file_name: str, equipa: Equipa) -> None:
        """
        Write an equipa to an EFT file.

        :file_name: The file name to write the equipa to.
        :equipa: The equipa to write.
        """
        with open(file_name, 'wb') as f:
            data = EquipaSerializer.serialize(equipa)

            if data:
                f.write(data)

    @staticmethod
    def read(file_name: str) -> Equipa:
        """
        Read an equipa from an EFT file.

        :file_name: The file name to read the equipa from.
        :return: The equipa read from the file.
        """
        try:
            with open(file_name, 'rb') as f:
                data = f.read()
                ep = EquipaParser(data)

                if not ep.has_equipa_header(data):
                    raise EquipaHeaderNotFound(file_name)

                return ep.parse()
        except FileNotFoundError as exc:
            raise EquipaNotFound(file_name) from exc
