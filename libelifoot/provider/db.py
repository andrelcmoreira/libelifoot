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


_DATA_PATH = pathlib.Path(__file__).parent / 'data'


def get_team_id(equipa_file: str, provider: str) -> str:
    with open(f'{_DATA_PATH}/{provider}.json', encoding='utf-8') as f:
        data = json.load(f)

        for entry in data:
            if entry['file'] == equipa_file:
                return entry['id']

        return ''


def get_teams(provider: str) -> list[dict]:
    with open(f'{_DATA_PATH}/{provider}.json', encoding='utf-8') as f:
        data = json.load(f)

        return data


def get_available_providers() -> list[str]:
    return [i.split('.')[0] for i in os.listdir(_DATA_PATH)]
