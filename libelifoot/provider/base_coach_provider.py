from abc import abstractmethod

from requests import exceptions, get

from libelifoot.equipa import mapping
from libelifoot.error.not_provided import EquipaNotProvided
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
        except (exceptions.ConnectionError, exceptions.ReadTimeout):
            return ''

    def get_coach(self, equipa_file: str, season: int) -> str:
        team_id = mapping.get_team_id(equipa_file, self._name)
        if not team_id:
            raise EquipaNotProvided(equipa_file)

        return self._fetch_coach_data(team_id, season)
