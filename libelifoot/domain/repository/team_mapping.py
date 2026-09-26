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

from libelifoot.domain.entity.equipa_db_entry import Equipa
from libelifoot.domain.entity.provider import Provider


class ITeamMappingRepository(ABC): # pragma: no cover

    @abstractmethod
    def get_team(
        self,
        equipa_file: str,
        provider: str
    ) -> Optional[Equipa]:
        """
        Retrieve the team entry related to a given equipa file path.

        :equipa_file: The path to the equipa file.
        :provider: The name of the provider.
        :return: The team entry if found, otherwise None.
        """

    @abstractmethod
    def get_teams(self, provider: str) -> list[Equipa]:
        """
        Retrieve a list of teams bound to a given provider.

        :provider: The name of the provider.
        :return: A list of teams.
        """

    @abstractmethod
    def get_providers(self) -> list[Provider]:
        """
        Retrieve a list of available providers.

        :return: A list of providers.
        """
