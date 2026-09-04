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

from libelifoot.domain.error.unknown_provider import UnknownProvider
from libelifoot.infrastructure.provider.impl import espn, transfermarkt
from libelifoot.domain.repository.team_mapping import ITeamMappingRepository


def create_coach_provider(
    team_mapping_repo: ITeamMappingRepository
) -> transfermarkt.CoachProvider:
    return transfermarkt.CoachProvider(team_mapping_repo)


def create_roster_provider(
    prov_name: str,
    team_mapping_repo: ITeamMappingRepository
) -> espn.RosterProvider | transfermarkt.RosterProvider:
    if prov_name == 'espn':
        return espn.RosterProvider(team_mapping_repo)
    if prov_name == 'transfermarkt':
        return transfermarkt.RosterProvider(team_mapping_repo)

    raise UnknownProvider(prov_name)
