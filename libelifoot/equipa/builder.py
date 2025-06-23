from typing import Self

from libelifoot.entity.equipa import Equipa
from libelifoot.file.equipa import EquipaFileHandler


class EquipaBuilder:

    def __init__(self):
        self._equipa = None

    def create_base_equipa(self, equipa_file: str) -> Self:
        self._equipa = EquipaFileHandler.read(equipa_file)
        # we are not interested on the players to create the base equipa
        self._equipa.players.clear()

        return self

    def add_players(self, players: list) -> Self:
        if self._equipa:
            self._equipa.players = players

        return self

    def add_coach(self, coach: str) -> Self:
        if self._equipa and coach:
            self._equipa.coach = coach

        return self

    def build(self) -> Equipa | None:
        return self._equipa
