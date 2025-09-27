from abc import abstractmethod, ABC

from requests import exceptions, get

from libelifoot.error.not_provided import EquipaNotProvided
from libelifoot.provider.base_provider import BaseProvider


class CoachProvider(ABC, BaseProvider):

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

    def get_coach(self, equipa_file: str, season: int) -> str:
        team_id = self._get_team_id(equipa_file)
        if not team_id:
            raise EquipaNotProvided(equipa_file)

        return self._fetch_coach_data(team_id, season)
