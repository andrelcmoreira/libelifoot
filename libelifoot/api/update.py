from os.path import sep

from libelifoot.api.command import Command
from libelifoot.equipa.builder import EquipaBuilder
from libelifoot.error.data_not_available import EquipaDataNotAvailable
from libelifoot.error.not_found import EquipaNotFound
from libelifoot.error.not_provided import EquipaNotProvided
from libelifoot.event.update_equipa_listener import UpdateEquipaListener

import libelifoot.provider.factory


class UpdateEquipa(Command):

    def __init__(self, equipa_file: str, prov: str, season: int,
                 listener: UpdateEquipaListener):
        self._equipa = equipa_file
        self._prov = libelifoot.provider.factory.create(prov)
        self._season = season
        self._listener = listener

    def run(self) -> None:
        equipa_file = self._equipa.split(sep)[-1]
        builder = EquipaBuilder()

        try:
            players = self._prov.get_players(equipa_file, self._season)
            coach = self._prov.get_coach(equipa_file, self._season)

            equipa = builder.create_base_equipa(self._equipa) \
                .add_players(players) \
                .add_coach(coach) \
                .build()

            self._listener.on_update_equipa(equipa_file, equipa)
        except (EquipaNotProvided, EquipaDataNotAvailable, EquipaNotFound) as e:
            self._listener.on_update_equipa_error(e)
        except PermissionError as e:
            self._listener.on_update_equipa_error(e)
