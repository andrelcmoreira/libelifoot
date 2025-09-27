from abc import ABC, abstractmethod


class BaseProvider(ABC):

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

    @abstractmethod
    def assemble_uri(self, team_id: str, season: int) -> str:
        pass
