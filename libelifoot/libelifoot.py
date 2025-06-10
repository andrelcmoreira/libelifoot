from libelifoot.api.bulk_update import BulkUpdate
from libelifoot.api.update import UpdateEquipa
from libelifoot.api.view import view

from libelifoot.event.update_equipa_listener import UpdateEquipaListener

from libelifoot.entity.equipa import Equipa


def update_equipa(equipa_file: str, provider: str, season: str, output_dir: str,
                  listener: UpdateEquipaListener):
    cmd = UpdateEquipa(equipa_file, provider, season,
                                     output_dir, listener)

    cmd.run()


def bulk_update(equipa_file: str, provider: str, season: str, output_dir: str,
                listener: UpdateEquipaListener):
    cmd = BulkUpdate(equipa_file, provider, season,
                                 output_dir, listener)

    cmd.run()


def view_equipa(equipa: str) -> Equipa:
    return view(equipa)
