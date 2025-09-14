from abc import abstractmethod, ABC
from json import load
from typing import Callable

from requests import exceptions, get
from unidecode import unidecode

from libelifoot.entity.player import Player
from libelifoot.error.data_not_available import EquipaDataNotAvailable
from libelifoot.error.not_provided import EquipaNotProvided
from libelifoot.util.player_position import PlayerPosition


# TODO: strategy pattern?


class BaseProvider(ABC):

    _USER_AGENT = 'libelifoot'
    _REQUEST_TIMEOUT = 30
    _MAX_GK_PLAYERS = 3
    _MAX_DEF_PLAYERS = 6
    _MAX_MD_PLAYERS = 6
    _MAX_FW_PLAYERS = 6
    _MAX_NAME_SIZE = 18

    def __init__(self, provider_name: str, base_url: str, country_map: dict,
                 sorting_fn: Callable[[Player], int]):
        self._name = provider_name
        self._base_url = base_url
        self._country_map = country_map
        self._sorting_fn = sorting_fn

    @abstractmethod
    def assemble_team_data_uri(self, team_id: str, season: int) -> str:
        pass

    @abstractmethod
    def assemble_team_coach_uri(self, team_id: str) -> str:
        pass

    @abstractmethod
    def parse_team_data(self, reply: str) -> list[Player]:
        pass

    @abstractmethod
    def parse_coach_data(self, reply: str, season: int) -> str:
        pass

    @property
    def name(self) -> str:
        return self._name

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

        # TODO: check the maximum number of players allowed by the game
        players.extend(gk[0:self._MAX_GK_PLAYERS])
        players.extend(df[0:self._MAX_DEF_PLAYERS])
        players.extend(mf[0:self._MAX_MD_PLAYERS])
        players.extend(fw[0:self._MAX_FW_PLAYERS])

        return players

    def get_country(self, country: str) -> str:
        return self._country_map[country] \
            if country in self._country_map \
            else unidecode(country[0:3]).upper()

    def _fetch_team_data(self, team_id: str, season: int) -> list[Player]:
        headers = { 'User-Agent': self._USER_AGENT }
        uri = self.assemble_team_data_uri(team_id, season)

        try:
            reply = get(uri, headers=headers, timeout=self._REQUEST_TIMEOUT)

            return self.parse_team_data(reply.text)
        except (exceptions.ConnectionError, exceptions.ReadTimeout):
            return []

    def _fetch_coach_data(self, team_id: str, season: int) -> str:
        headers = { 'User-Agent': self._USER_AGENT }
        uri = self.assemble_team_coach_uri(team_id)

        if not uri:
            return ''

        try:
            reply = get(uri, headers=headers, timeout=self._REQUEST_TIMEOUT)

            return self.parse_coach_data(reply.text, season)
        except (exceptions.ConnectionError, exceptions.ReadTimeout):
            return ''

    def _get_team_id(self, equipa_file: str) -> str:
        with open(f'data/{self._name}.json', encoding='utf-8') as f:
            mapping = load(f)

            for entry in mapping:
                if entry['file'] == equipa_file:
                    return entry['id']

            return ''

    def get_teams(self) -> list[dict]:
        with open(f'data/{self._name}.json', encoding='utf-8') as f:
            mapping = load(f)

            return mapping

    def get_players(self, equipa_file: str, season: int) -> list[Player]:
        team_id = self._get_team_id(equipa_file)
        if not team_id:
            raise EquipaNotProvided(equipa_file)

        players = self._fetch_team_data(team_id, season)
        if not players:
            raise EquipaDataNotAvailable(equipa_file)

        return self.select_players(players)

    def get_coach(self, equipa_file: str, season: int) -> str:
        team_id = self._get_team_id(equipa_file)
        if not team_id:
            raise EquipaNotProvided(equipa_file)

        return self._fetch_coach_data(team_id, season)
