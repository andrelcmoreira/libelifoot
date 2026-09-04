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

from abc import abstractmethod

from requests import exceptions, get

from libelifoot.domain.error.equipa_not_provided import EquipaNotProvided
from libelifoot.infrastructure.provider.base_provider import BaseProvider
from libelifoot.domain.repository.team_mapping import ITeamMappingRepository


class BaseCoachProvider(BaseProvider):

    def __init__(
        self,
        provider_name: str,
        base_url: str,
        interval: int,
        repo: ITeamMappingRepository
    ):
        self._repo = repo
        super().__init__(provider_name, base_url, interval)

    @abstractmethod
    def parse_data(self, reply: str, season: int) -> str:
        pass # pragma: no cover

    def _fetch_data(self, team_id: str, season: int) -> str:
        headers = { 'User-Agent': self._USER_AGENT }
        uri = self.assemble_uri(team_id, season)

        if not uri:
            return '' # operation not implemented by the specific provider

        try:
            reply = get(uri, headers=headers, timeout=self._REQUEST_TIMEOUT)

            return self.parse_data(reply.text, season)
        except (
            exceptions.ConnectionError,
            exceptions.ReadTimeout
        ):
            return ''

    def get_coach(self, equipa_file: str, season: int) -> str:
        team = self._repo.get_team(equipa_file, self._name)
        if not team:
            raise EquipaNotProvided(equipa_file)

        return self._fetch_data(team.id, season)
