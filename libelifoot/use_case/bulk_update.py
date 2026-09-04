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

import time
from typing import Any

from libelifoot.domain.repository.equipa import IEquipaRepository
from libelifoot.domain.repository.team_mapping import ITeamMappingRepository
from libelifoot.infrastructure.provider.base_coach_provider import BaseCoachProvider
from libelifoot.infrastructure.provider.base_roster_provider import BaseRosterProvider
from libelifoot.use_case.update_equipa import UpdateEquipa
from libelifoot.use_case.event.update_equipa_listener import IUpdateEquipaListener
from libelifoot.use_case.cmd import ICmd


class BulkUpdate(ICmd):

    def __init__(
        self,
        equipa_dir: str,
        roster_prov: BaseRosterProvider,
        coach_prov: BaseCoachProvider,
        season: int,
        team_repo: ITeamMappingRepository,
        equipa_repo: IEquipaRepository,
        listener: IUpdateEquipaListener
    ):
        self._dir = equipa_dir
        self._roster_prov = roster_prov
        self._coach_prov = coach_prov
        self._season = season
        self._team_repo = team_repo
        self._equipa_repo = equipa_repo
        self._ev = listener

    def run(self) -> Any:
        teams = self._team_repo.get_teams(self._roster_prov.name)

        for team in teams:
            cmd = UpdateEquipa(
                f"{self._dir}/{team.file}",
                self._roster_prov,
                self._coach_prov,
                self._season,
                self._equipa_repo,
                self._ev
            )

            cmd.run()

            time.sleep(self._roster_prov.interval)  # to avoid overwhelming the data source
