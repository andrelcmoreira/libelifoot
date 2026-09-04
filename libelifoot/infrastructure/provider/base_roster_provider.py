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
from typing import Callable

from requests import exceptions, get
from unidecode import unidecode

from libelifoot.domain.entity.player import Player
from libelifoot.domain.error.equipa_data_not_available import EquipaDataNotAvailable
from libelifoot.domain.error.equipa_not_provided import EquipaNotProvided
from libelifoot.domain.util.player_position import PlayerPosition
from libelifoot.domain.repository.team_mapping import ITeamMappingRepository
from libelifoot.infrastructure.provider.base_provider import BaseProvider


class BaseRosterProvider(BaseProvider):

    _MAX_GK_PLAYERS = 2
    _MAX_DEF_PLAYERS = 6
    _MAX_MD_PLAYERS = 6
    _MAX_FW_PLAYERS = 6
    _MAX_NAME_SIZE = 18

    def __init__(
        self,
        provider_name: str,
        base_url: str,
        country_map: dict,
        interval: int,
        sorting_fn: Callable[[Player], int],
        repo: ITeamMappingRepository
    ):
        self._country_map = country_map
        self._sorting_fn = sorting_fn
        self._repo = repo

        super().__init__(provider_name, base_url, interval)

    @abstractmethod
    def parse_data(self, reply: str) -> list[Player]:
        pass # pragma: no cover

    def select_players(self, player_list: list[Player]) -> list[Player]:
        players = []
        gk = []
        df = []
        mf = []
        fw = []

        for player in player_list:
            match player.position:
                case PlayerPosition.G.name: gk.append(player)
                case PlayerPosition.D.name: df.append(player)
                case PlayerPosition.M.name: mf.append(player)
                case PlayerPosition.A.name: fw.append(player)

        gk.sort(key=self._sorting_fn, reverse=True)
        df.sort(key=self._sorting_fn, reverse=True)
        mf.sort(key=self._sorting_fn, reverse=True)
        fw.sort(key=self._sorting_fn, reverse=True)

        players.extend(gk[0:self._MAX_GK_PLAYERS])
        players.extend(df[0:self._MAX_DEF_PLAYERS])
        players.extend(mf[0:self._MAX_MD_PLAYERS])
        players.extend(fw[0:self._MAX_FW_PLAYERS])

        return players

    def get_country(self, country: str) -> str:
        return self._country_map[country] \
            if country in self._country_map \
            else unidecode(country[0:3]).upper()

    def _fetch_data(self, team_id: str, season: int) -> list[Player]:
        headers = { 'User-Agent': self._USER_AGENT }
        uri = self.assemble_uri(team_id, season)

        try:
            reply = get(uri, headers=headers, timeout=self._REQUEST_TIMEOUT)

            return self.parse_data(reply.text)
        except (
            exceptions.ConnectionError,
            exceptions.ReadTimeout
        ):
            return []

    def get_players(self, equipa_file: str, season: int) -> list[Player]:
        team = self._repo.get_team(equipa_file, self._name)
        if not team:
            raise EquipaNotProvided(equipa_file)

        players = self._fetch_data(team.id, season)
        if not players:
            raise EquipaDataNotAvailable(equipa_file)

        return self.select_players(players)
