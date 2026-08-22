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

from libelifoot.infra.provider import factory
from libelifoot.infra.repository import (
    get_equipa_repository,
    get_team_mapping_repository
)
from libelifoot.use_case.dto import Equipa
from libelifoot.use_case.event import IUpdateEquipaListener
from libelifoot.use_case.bulk_update import BulkUpdate
from libelifoot.use_case.get_equipa_data import GetEquipaData
from libelifoot.use_case.get_providers import GetProviders
from libelifoot.use_case.update_equipa import UpdateEquipa


_TEAM_MAPPING_REPO = get_team_mapping_repository()
_EQUIPA_REPO = get_equipa_repository()


def update_equipa(
    equipa_file: str,
    provider: str,
    season: int,
    listener: IUpdateEquipaListener
) -> None:
    """
    Update an equipa specified by 'equipa_file'.

    :equipa_file: The equipa file.
    :provider: The data provider (espn or transfermarkt).
    :season: Year's season to use as reference in update operation.
    :listener: Event listener to handle the events.
    """
    cmd = UpdateEquipa(
        equipa_file,
        factory.create_roster_provider(provider),
        factory.create_coach_provider(),
        season,
        listener
    )

    cmd.run()


#def bulk_update(
#    equipa_dir: str,
#    provider: str,
#    season: int,
#    listener: IUpdateEquipaListener
#) -> None:
#    """
#    Update all equipas placed at 'equipa_dir'.
#
#    :equipa_dir: The equipas directory.
#    :provider: The data provider (espn or transfermarkt).
#    :season: Year's season to use as reference in update operation.
#    :listener: Event listener to handle the events.
#    """
#    cmd = _bulk_update.Cmd(
#        equipa_dir,
#        factory.create_roster_provider(provider),
#        factory.create_coach_provider(),
#        season,
#        _TEAM_MAPPING_REPO,
#        listener
#    )
#
#    cmd.run()


def get_equipa_data(equipa_file: str) -> Equipa:
    """
    Get the equipa data according to the supplied file 'equipa_file'.

    :equipa_file: The equipa file.

    :returns: The equipa data.
    """
    cmd = GetEquipaData(equipa_file, _EQUIPA_REPO)

    return cmd.run()


def get_providers() -> list[str]:
    """
    Get a list of the providers supported by the library.

    :returns: A list containing all available data providers.
    """
    cmd = GetProviders(_TEAM_MAPPING_REPO)

    return cmd.run()
