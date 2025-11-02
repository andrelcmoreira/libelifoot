from libelifoot.api.bulk_update import BulkUpdate
from libelifoot.api.update_equipa import UpdateEquipa
from libelifoot.api.view_equipa import view
from libelifoot.entity.equipa import Equipa
from libelifoot.event.update_equipa_listener import UpdateEquipaListener
from libelifoot.provider import factory


def update_equipa(equipa_file: str, provider: str, season: int,
                  listener: UpdateEquipaListener) -> None:
    """
    Update an equipa specified by 'equipa_file'.

    :equipa_file: The equipa file.
    :provider: The data provider (espn or transfermarkt).
    :season: Year's season to use as reference in update operation.
    :listener: Event listener to handle the events.
    """
    cmd = UpdateEquipa(equipa_file, factory.create_roster_provider(provider),
                       factory.create_coach_provider(), season, listener)

    cmd.run()


def bulk_update(equipa_dir: str, provider: str, season: int,
                listener: UpdateEquipaListener) -> None:
    """
    Update all equipas placed at 'equipa_dir'.

    :equipa_dir: The equipas directory.
    :provider: The data provider (espn or transfermarkt).
    :season: Year's season to use as reference in update operation.
    :listener: Event listener to handle the events.
    """
    cmd = BulkUpdate(equipa_dir, factory.create_roster_provider(provider),
                     factory.create_coach_provider(), season, listener)

    cmd.run()


def view_equipa(equipa_file: str) -> Equipa:
    """
    View an equipa specified by 'equipa_file'.

    :equipa_file: The equipa file.

    :returns: The equipa data.
    """
    return view(equipa_file)
