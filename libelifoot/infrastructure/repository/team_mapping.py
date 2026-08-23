import json
import os
import pathlib

from typing import Optional

from libelifoot.domain.entity.equipa import Equipa
from libelifoot.domain.entity.provider import Provider
from libelifoot.domain.repository.team_mapping import ITeamMappingRepository


def get_team_mapping_repository() -> ITeamMappingRepository:
    return JsonTeamMappingRepository()


class JsonTeamMappingRepository(ITeamMappingRepository):

    _DATA_PATH = pathlib.Path(__file__).parent.parent / 'data'

    def get_team(self, equipa_file: str, provider: str) -> Optional[Equipa]:
        with open(f'{self._DATA_PATH}/{provider}.json', encoding='utf-8') as f:
            data = json.load(f)

            for entry in data:
                if entry['file'] == equipa_file:
                    return Equipa(**entry)

            return None

    def get_teams(self, provider: str) -> list[Equipa]:
        with open(f'{self._DATA_PATH}/{provider}.json', encoding='utf-8') as f:
            data = json.load(f)

            return [Equipa(**entry) for entry in data]

    def get_providers(self) -> list[Provider]:
        return [
            Provider(
                name=i.split('.')[0],
                url=''
            ) for i in os.listdir(self._DATA_PATH)]
