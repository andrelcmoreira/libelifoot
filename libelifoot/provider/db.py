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
