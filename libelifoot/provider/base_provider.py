from json import load


class BaseProvider:

    _USER_AGENT = 'libelifoot'
    _REQUEST_TIMEOUT = 30

    def __init__(self, provider_name: str, base_url: str, interval: int):
        self._name = provider_name
        self._base_url = base_url
        self._interval = interval

    @property
    def name(self) -> str:
        return self._name

    @property
    def interval(self) -> int:
        return self._interval

    def _get_team_id(self, equipa_file: str) -> str:
        with open(f'data/{self._name}.json', encoding='utf-8') as f:
            mapping = load(f)

            for entry in mapping:
                if entry['file'] == equipa_file:
                    return entry['id']

            return ''
