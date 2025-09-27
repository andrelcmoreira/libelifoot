from json import load


def get_team_id(equipa_file: str, provider: str) -> str:
    with open(f'data/{provider}.json', encoding='utf-8') as f:
        mapping = load(f)

        for entry in mapping:
            if entry['file'] == equipa_file:
                return entry['id']

        return ''


def get_teams(provider: str) -> list[dict]:
    with open(f'data/{provider}.json', encoding='utf-8') as f:
        mapping = load(f)

        return mapping
