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

from libelifoot.api.base_cmd import BaseCmd
from libelifoot.api import update_equipa
from libelifoot.event.update_equipa_listener import UpdateEquipaListener
from libelifoot.provider.base_coach_provider import BaseCoachProvider
from libelifoot.provider.base_roster_provider import BaseRosterProvider
from libelifoot.provider import db


class Cmd(BaseCmd):

    def __init__(
        self,
        equipa_dir: str,
        roster_prov: BaseRosterProvider,
        coach_prov: BaseCoachProvider,
        season: int,
        listener: UpdateEquipaListener
    ):
        self._dir = equipa_dir
        self._roster_prov = roster_prov
        self._coach_prov = coach_prov
        self._season = season
        self._ev = listener

    def run(self) -> Any:
        teams = db.get_teams(self._roster_prov.name)

        for team in teams:
            cmd = update_equipa.Cmd(f"{self._dir}/{team['file']}",
                                    self._roster_prov, self._coach_prov,
                                    self._season, self._ev)

            cmd.run()

            time.sleep(self._roster_prov.interval)  # to avoid overwhelming the data source
