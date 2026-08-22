import json
import os
import pathlib

from typing import Optional

from libelifoot.core.entity import Equipa, Provider
from libelifoot.core.repository import (
    IEquipaRepository,
    ITeamMappingRepository
)


def get_team_mapping_repository() -> ITeamMappingRepository:
    return JsonTeamMappingRepository()


def get_equipa_repository() -> IEquipaRepository:
    return FileEquipaRepository()


class JsonTeamMappingRepository(ITeamMappingRepository):

    _DATA_PATH = pathlib.Path(__file__).parent / 'data'

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


class FileEquipaRepository(IEquipaRepository):

    def get_equipa(self, equipa_file: str) -> Optional[bytes]:
        """
        Retrieve an equipa by its file name.

        :equipa_file: The equipa file name.
        :return: The Equipa object if found, otherwise None.
        """
        try:
            with open(equipa_file, 'rb') as f:
                return f.read()
        except FileNotFoundError:
            return None

    def save_equipa(self, equipa_file: str, data: bytes) -> None:
        """
        Save an equipa to the repository.

        :equipa_file: The equipa file name.
        :equipa: The Equipa object to save.
        """
        with open(equipa_file, 'wb') as f:
            if data:
                f.write(data)
