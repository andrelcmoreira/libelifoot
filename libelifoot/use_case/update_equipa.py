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
from typing import Any

from libelifoot.domain.interface.cmd import ICmd
from libelifoot.domain import builder
from libelifoot.domain.error.data_not_available import EquipaDataNotAvailable
from libelifoot.domain.error.not_found import EquipaNotFound
from libelifoot.domain.error.not_provided import EquipaNotProvided
from libelifoot.domain.interface.update_equipa_listener import IUpdateEquipaListener
from libelifoot.provider.base_coach_provider import BaseCoachProvider
from libelifoot.provider.base_roster_provider import BaseRosterProvider


class Cmd(ICmd):

    def __init__(
        self,
        equipa_file: str,
        roster_prov: BaseRosterProvider,
        coach_prov: BaseCoachProvider,
        season: int,
        listener: IUpdateEquipaListener
    ):
        self._equipa = equipa_file
        self._roster = roster_prov
        self._coach = coach_prov
        self._season = season
        self._ev = listener
        self._builder = builder.EquipaBuilder()

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
