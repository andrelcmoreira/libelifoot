from libelifoot.api import (
    bulk_update as _bulk_update,
    update_equipa as _update_equipa,
    get_equipa_data as _get_equipa_data
)
from libelifoot.entity.equipa import Equipa
from libelifoot.event.update_equipa_listener import UpdateEquipaListener
from libelifoot.provider import factory


def update_equipa(
    equipa_file: str,
    provider: str,
    season: int,
    listener: UpdateEquipaListener
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
    listener: UpdateEquipaListener
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
