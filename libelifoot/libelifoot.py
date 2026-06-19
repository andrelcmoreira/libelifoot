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

from libelifoot.use_case import (
    bulk_update as _bulk_update,
    update_equipa as _update_equipa,
    get_available_providers as _get_available_providers,
    get_equipa_data as _get_equipa_data
)
from libelifoot.use_case.dto.equipa import Equipa
from libelifoot.domain.interface.update_equipa_listener import IUpdateEquipaListener
from libelifoot.provider import factory


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
    cmd = _update_equipa.Cmd(
        equipa_file,
        factory.create_roster_provider(provider),
        factory.create_coach_provider(),
        season,
        listener
    )

    cmd.run()


def bulk_update(
    equipa_dir: str,
    provider: str,
    season: int,
    listener: IUpdateEquipaListener
) -> None:
    """
    Update all equipas placed at 'equipa_dir'.

    :equipa_dir: The equipas directory.
    :provider: The data provider (espn or transfermarkt).
    :season: Year's season to use as reference in update operation.
    :listener: Event listener to handle the events.
    """
    cmd = _bulk_update.Cmd(
        equipa_dir,
        factory.create_roster_provider(provider),
        factory.create_coach_provider(),
        season,
        listener
    )

    cmd.run()


def get_equipa_data(equipa_file: str) -> Equipa:
    """
    Get the equipa data according to the supplied file 'equipa_file'.

    :equipa_file: The equipa file.

    :returns: The equipa data.
    """
    cmd = _get_equipa_data.Cmd(equipa_file)

    return cmd.run()


def get_available_providers() -> list[str]:
    """
    Get a list of the providers supported by the library.

    :returns: A list containing all available data providers.
    """
    cmd = _get_available_providers.Cmd()

    return cmd.run()
