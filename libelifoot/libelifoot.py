from libelifoot.entity.equipa import Equipa
from libelifoot.event.update_equipa_listener import UpdateEquipaListener
from libelifoot.api.bulk_update import BulkUpdate
from libelifoot.api.update import UpdateEquipa
from libelifoot.api.view import view


def update_equipa(equipa_file: str, provider: str, season: int,
                  listener: UpdateEquipaListener) -> None:
    cmd = UpdateEquipa(equipa_file, provider, season, listener)

    cmd.run()


def bulk_update(equipa_dir: str, provider: str, season: int,
                listener: UpdateEquipaListener) -> None:
    cmd = BulkUpdate(equipa_dir, provider, season, listener)

    cmd.run()


def view_equipa(equipa_file: str) -> Equipa:
    return view(equipa_file)
