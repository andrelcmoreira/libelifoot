from abc import abstractmethod, ABC
from json import load
from requests import exceptions, get
from unidecode import unidecode

from libelifoot.entity.player import Player
from libelifoot.error.data_not_available import EquipaDataNotAvailable
from libelifoot.error.not_provided import EquipaNotProvided


class BaseProvider(ABC):

    _REQUEST_TIMEOUT = 30
    _MAX_GK_PLAYERS = 3
    _MAX_DEF_PLAYERS = 6
    _MAX_MD_PLAYERS = 6
    _MAX_FW_PLAYERS = 6
    _MAX_NAME_SIZE = 18

    def __init__(self, provider_name: str, base_url: str, country_map: dict):
        self._name = provider_name
        self._base_url = base_url
        self._country_map = country_map

    @abstractmethod
    def assemble_uri(self, team_id: str, season: int) -> str:
        pass

    @abstractmethod
    def parse_reply(self, reply: str) -> list[Player]:
        pass

    @abstractmethod
    def select_players(self, player_list: list) -> list[Player]:
        pass

    @abstractmethod
    def get_coach(self, equipa_file: str, season: int) -> str:
        pass

    @property
    def name(self) -> str:
        return self._name

    def get_country(self, country: str) -> str:
        return self._country_map[country] \
            if country in self._country_map \
            else unidecode(country[0:3]).upper()

    def _fetch_team_data(self, team_id: str, season: int) -> list[Player]:
        headers = { 'User-Agent': 'elf98' }
        uri = self.assemble_uri(team_id, season)

        try:
            reply = get(uri, headers=headers, timeout=self._REQUEST_TIMEOUT)

            return self.parse_reply(reply.text)
        except (exceptions.ConnectionError, exceptions.ReadTimeout):
            return []

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
        if team_id == '':
            raise EquipaNotProvided(equipa_file)

        players = self._fetch_team_data(team_id, season)
        if not players:
            raise EquipaDataNotAvailable(equipa_file)

        return self.select_players(players)
