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

from abc import ABC, abstractmethod
from typing import Optional


class IEquipaRepository(ABC): # pragma: no cover

    @abstractmethod
    def get(self, equipa_id: str) -> Optional[bytes]:
        """
        Retrieve an equipa.

        :equipa_id: The equipa ID.
        :return: The Equipa's raw data if it exists, otherwise None.
        """

    @abstractmethod
    def save(self, equipa_id: str, data: bytes) -> None:
        """
        Save an equipa.

        :equipa_id: The equipa ID.
        :data: The Equipa's raw data to be saved.
        """
