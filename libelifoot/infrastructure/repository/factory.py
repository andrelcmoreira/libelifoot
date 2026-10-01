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

from libelifoot.domain.repository.equipa import IEquipaRepository
from libelifoot.domain.repository.team_mapping import ITeamMappingRepository
from libelifoot.infrastructure.repository.file_equipa import \
    FileEquipaRepository
from libelifoot.infrastructure.repository.json_team_mapping import \
    JsonTeamMappingRepository


def get_equipa_repository() -> IEquipaRepository:
    return FileEquipaRepository()


def get_team_mapping_repository() -> ITeamMappingRepository:
    return JsonTeamMappingRepository()
