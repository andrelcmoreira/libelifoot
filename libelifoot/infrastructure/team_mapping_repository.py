import json
import pathlib

from typing import Optional

from libelifoot.domain import entity
from libelifoot.domain.repository import ITeamMappingRepository


def get_team_mapping_repository() -> ITeamMappingRepository:
    return JsonTeamMappingRepository()


class JsonTeamMappingRepository(ITeamMappingRepository):

    _DATA_PATH = pathlib.Path(__file__).parent / 'data'

    def get_team(
        self,
        equipa_file: str,
        provider: str
    ) -> Optional[entity.Equipa]:
        with open(f'{self._DATA_PATH}/{provider}.json', encoding='utf-8') as f:
            data = json.load(f)

            for entry in data:
                if entry['file'] == equipa_file:
                    return entry['id']

            return None

    def get_teams(self, provider: str) -> list[entity.Equipa]:
        with open(f'{self._DATA_PATH}/{provider}.json', encoding='utf-8') as f:
            data = json.load(f)

            return data
