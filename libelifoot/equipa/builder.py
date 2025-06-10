from typing import Self

from libelifoot.parser.equipa import EquipaParser
from libelifoot.serializer.coach import CoachSerializer
from libelifoot.serializer.player import PlayerSerializer
from libelifoot.util.offset import OffsetCalculator


class EquipaBuilder:

    def __init__(self):
        self._data = bytearray()
        self._default_coach = '' # to be used as default coach name when the
                                 # data is not available

    def create_base_equipa(self, in_file: str) -> Self:
        ep = EquipaParser(in_file)

        with open(in_file, 'rb') as f:
            data = f.read()

            ext_name = ep.parse_ext_name(data)
            short_name = ep.parse_short_name(data, len(ext_name))
            self._default_coach = ep.parse_coach(data, len(ext_name),
                                                 len(short_name))
            offs = OffsetCalculator.get_level(len(ext_name), len(short_name))

            self._data += data[:offs + 1]

        return self

    def add_players(self, players: list) -> Self:
        # TODO: check for the minimum number of players
        for player in players:
            self._data += PlayerSerializer.serialize(player)

        return self

    def add_coach(self, coach: str) -> Self:
        self._data += CoachSerializer.serialize(coach) if coach else \
            CoachSerializer.serialize(self._default_coach)

        return self

    def add_player_number(self, players_number: int) -> Self:
        self._data += players_number.to_bytes()

        return self

    def build(self) -> bytearray:
        return self._data
