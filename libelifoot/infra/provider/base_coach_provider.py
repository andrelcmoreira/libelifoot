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

from libelifoot.core.error import EquipaNotProvided
from libelifoot.provider import db
from libelifoot.provider.base_provider import BaseProvider


class BaseCoachProvider(BaseProvider):

    @abstractmethod
    def parse_coach_data(self, reply: str, season: int) -> str:
        pass # pragma: no cover

    def _fetch_coach_data(self, team_id: str, season: int) -> str:
        headers = { 'User-Agent': self._USER_AGENT }
        uri = self.assemble_uri(team_id, season)

        if not uri:
            return '' # operation not implemented by the specific provider

        try:
            reply = get(uri, headers=headers, timeout=self._REQUEST_TIMEOUT)

            return self.parse_coach_data(reply.text, season)
        except (
            exceptions.ConnectionError,
            exceptions.ReadTimeout
        ):
            return ''

    def get_coach(self, equipa_file: str, season: int) -> str:
        team_id = db.get_team_id(equipa_file, self._name)
        if not team_id:
            raise EquipaNotProvided(equipa_file)

        return self._fetch_coach_data(team_id, season)
