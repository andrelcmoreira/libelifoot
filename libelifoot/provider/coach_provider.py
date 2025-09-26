from abc import abstractmethod, ABC
from json import load

from requests import exceptions, get

from libelifoot.error.not_provided import EquipaNotProvided


class CoachProvider(ABC):

    _USER_AGENT = 'libelifoot'
    _REQUEST_TIMEOUT = 30

    def __init__(self, provider_name: str, base_url: str, interval: int):
        self._name = provider_name
        self._base_url = base_url
        self._interval = interval

    @abstractmethod
    def assemble_coach_uri(self, team_id: str) -> str:
        pass

    @abstractmethod
    def parse_coach_data(self, reply: str, season: int) -> str:
        pass

    @property
    def name(self) -> str:
        return self._name

    @property
    def interval(self) -> int:
        return self._interval

    def _fetch_coach_data(self, team_id: str, season: int) -> str:
        headers = { 'User-Agent': self._USER_AGENT }
        uri = self.assemble_coach_uri(team_id)

        if not uri:
            return '' # operation not implemented by the specific provider

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

    def get_coach(self, equipa_file: str, season: int) -> str:
        team_id = self._get_team_id(equipa_file)
        if not team_id:
            raise EquipaNotProvided(equipa_file)

        return self._fetch_coach_data(team_id, season)
