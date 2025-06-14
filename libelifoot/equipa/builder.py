from typing import Self

from libelifoot.entity.equipa import Equipa
from libelifoot.parser.equipa import EquipaParser


class EquipaBuilder:

    def __init__(self):
        self._equipa = None

    def create_base_equipa_from_file(self, equipa_file: str) -> Self:
        ep = EquipaParser(equipa_file)

        with open(equipa_file, 'rb') as f:
            data = f.read()

            ext_name = ep.parse_ext_name(data)
            short_name = ep.parse_short_name(data, len(ext_name))
            country = ep.parse_country(data, len(ext_name), len(short_name))
            level = ep.parse_level(data, len(ext_name), len(short_name))
            coach = ep.parse_coach(data, len(ext_name), len(short_name))
            colors = ep.parse_colors(data, len(ext_name), len(short_name))

            self._equipa = Equipa(ext_name, short_name, country, level, colors,
                                  coach, [])

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
