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
from libelifoot.provider.impl import espn
from libelifoot.provider.impl import transfermarkt


def create_coach_provider() -> transfermarkt.CoachProvider:
    return transfermarkt.CoachProvider()


def create_roster_provider(
    prov_name: str
) -> espn.RosterProvider | transfermarkt.RosterProvider:
    if prov_name == 'espn':
        return espn.RosterProvider()
    if prov_name == 'transfermarkt':
        return transfermarkt.RosterProvider()

    raise UnknownProvider(prov_name)
