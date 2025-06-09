from os import mkdir
from os.path import sep, exists

from command.command import Command
from equipa.builder import EquipaBuilder
from error.data_not_available import EquipaDataNotAvailable
from error.not_found import EquipaNotFound
from error.not_provided import EquipaNotProvided
from event.update_equipa_listener import UpdateEquipaListener

import provider.factory


class UpdateEquipa(Command):

    def __init__(self, equipa_file: str, prov: str, season: str,
                 output_dir: str, listener: UpdateEquipaListener):
        self._equipa = equipa_file
        self._prov = provider.factory.create(prov)
        self._season = season
        self._out_dir = output_dir
        self._listener = listener

    def run(self) -> None:
        equipa_file = self._equipa.split(sep)[-1]
        builder = EquipaBuilder()

        if not exists(self._out_dir):
            mkdir(self._out_dir)

        try:
            players = self._prov.get_players(equipa_file, self._season)
            coach = self._prov.get_coach(equipa_file, self._season)

            with open(self._out_dir + '/' + equipa_file, 'wb') as f:
                data = builder.create_base_equipa(self._equipa) \
                    .add_player_number(len(players)) \
                    .add_players(players) \
                    .add_coach(coach) \
                    .build()

                f.write(data)
                self._listener.on_update_equipa(self._equipa)
        except (EquipaNotProvided, EquipaDataNotAvailable, EquipaNotFound) as e:
            self._listener.on_update_equipa_error(e)
        except PermissionError as e:
            self._listener.on_update_equipa_error(e)
