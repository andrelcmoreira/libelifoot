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

import os.path

from typing import Any, Optional, Self

from libelifoot.domain.error.equipa_data_not_available import EquipaDataNotAvailable
from libelifoot.domain.error.equipa_not_found import EquipaNotFound
from libelifoot.domain.error.equipa_not_provided import EquipaNotProvided
from libelifoot.infrastructure.eft.parser.equipa import EquipaParser
from libelifoot.infrastructure.provider.base_coach_provider import BaseCoachProvider
from libelifoot.infrastructure.provider.base_roster_provider import BaseRosterProvider
from libelifoot.infrastructure.repository.equipa import IEquipaRepository
from libelifoot.use_case.cmd import ICmd
from libelifoot.use_case.dto.equipa import Equipa
from libelifoot.use_case.dto.player import Player
from libelifoot.use_case.event.update_equipa_listener import IUpdateEquipaListener


class UpdateEquipa(ICmd):

    class Builder:

        def __init__(self, equipa_repo: IEquipaRepository):
            self._repo = equipa_repo
            self._equipa = None

        def create_base_equipa(self, equipa_file: str) -> Self:
            equipa_raw = self._repo.get_equipa(equipa_file)

            if not equipa_raw:
                raise EquipaNotFound(equipa_file)

            ep = EquipaParser(equipa_raw)
            if not ep.has_equipa_header(equipa_raw):
                raise EquipaDataNotAvailable(equipa_file)

            self._equipa = Equipa.from_entity(ep.parse())
            # we are not interested on the players to create the base equipa
            self._equipa.players.clear()

            return self

        def add_players(self, players: list[Player]) -> Self:
            if self._equipa:
                self._equipa.players = players

            return self

        def add_coach(self, coach: str) -> Self:
            if self._equipa and coach:
                self._equipa.coach = coach

            return self

        def build(self) -> Optional[Equipa]:
            return self._equipa

    def __init__(
        self,
        equipa_file: str,
        roster_prov: BaseRosterProvider,
        coach_prov: BaseCoachProvider,
        season: int,
        equipa_repo: IEquipaRepository,
        listener: IUpdateEquipaListener
    ):
        self._equipa = equipa_file
        self._roster = roster_prov
        self._coach = coach_prov
        self._season = season
        self._ev = listener
        self._builder = self.Builder(equipa_repo)

    def run(self) -> Any:
        equipa_file = self._equipa.split(os.path.sep)[-1]

        try:
            players = self._roster.get_players(equipa_file, self._season)
            coach = self._coach.get_coach(equipa_file, self._season)
            equipa = self._builder.create_base_equipa(self._equipa) \
                .add_players(players) \
                .add_coach(coach) \
                .build()

            self._ev.on_update_equipa(equipa_file, equipa)
        except (
            EquipaNotProvided,
            EquipaDataNotAvailable,
            EquipaNotFound,
            PermissionError
        ) as err:
            self._ev.on_update_equipa_error(str(err))
