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

import json
import os
import pathlib

from typing import Optional

from libelifoot.domain.entity.equipa_db_entry import EquipaDbEntry
from libelifoot.domain.entity.provider import Provider
from libelifoot.domain.repository.team_mapping import ITeamMappingRepository


def get_team_mapping_repository() -> ITeamMappingRepository:
    return JsonTeamMappingRepository()


class JsonTeamMappingRepository(ITeamMappingRepository):

    _DATA_PATH = pathlib.Path(__file__).parent.parent / 'static'

    def get_team(
        self,
        equipa_file: str,
        provider: str
    ) -> Optional[EquipaDbEntry]:
        with open(f'{self._DATA_PATH}/{provider}.json', encoding='utf-8') as f:
            data = json.load(f)

            for entry in data:
                if entry['file'] == equipa_file:
                    return EquipaDbEntry(id=entry['id'], file=entry['file'])

            return None

    def get_teams(self, provider: str) -> list[EquipaDbEntry]:
        with open(f'{self._DATA_PATH}/{provider}.json', encoding='utf-8') as f:
            data = json.load(f)

            return [
                EquipaDbEntry(
                    id=entry['id'],
                    file=entry['file']
                ) for entry in data
            ]

    def get_providers(self) -> list[Provider]:
        return [
            Provider(
                name=i.split('.')[0],
                url=''
            ) for i in os.listdir(self._DATA_PATH)]
