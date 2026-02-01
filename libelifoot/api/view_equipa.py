from typing import Any

from libelifoot.api.base_cmd import BaseCmd
from libelifoot.file.equipa import EquipaFileHandler


class Cmd(BaseCmd):

    def __init__(self, equipa: str):
        self._equipa = equipa

    def run(self) -> Any:
        return EquipaFileHandler.read(self._equipa)
