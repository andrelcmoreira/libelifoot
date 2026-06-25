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
from typing import Any, Optional

from libelifoot.domain.entity import Equipa


class ICmd(ABC): # pragma: no cover

    @abstractmethod
    def run(self) -> Any:
        pass


class ISerializer(ABC): # pragma: no cover

    @staticmethod
    @abstractmethod
    def serialize(obj: Any) -> Optional[bytearray]:
        pass


class IEquipaRepository(ABC): # pragma: no cover

    @abstractmethod
    def get_equipa(self, equipa_file: str) -> Optional[Equipa]:
        """
        Retrieve an equipa by its file name.

        :equipa_file: The equipa file name.
        :return: The Equipa object if found, otherwise None.
        """

    @abstractmethod
    def save_equipa(self, equipa_file: str, equipa: Equipa) -> None:
        """
        Save an equipa to the repository.

        :equipa_file: The equipa file name.
        :equipa: The Equipa object to save.
        """


class ITeamMappingRepository(ABC): # pragma: no cover

    @abstractmethod
    def get_team(self, equipa_file: str, provider: str) -> Optional[Equipa]:
        """
        Retrieve the mapped team related to a given equipa file path.

        :equipa_file: The path to the equipa file.
        :provider: The name of the provider.
        :return: The mapped team ID if found, otherwise None.
        """

    @abstractmethod
    def get_teams(self, provider: str) -> list[Equipa]:
        """
        Retrieve a list of team names for a given provider.

        :provider: The name of the provider.
        :return: A list of equipas.
        """
