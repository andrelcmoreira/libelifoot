from os.path import sep

from libelifoot.api.async_command import AsyncCommand
from libelifoot.equipa.builder import EquipaBuilder
from libelifoot.error.data_not_available import EquipaDataNotAvailable
from libelifoot.error.not_found import EquipaNotFound
from libelifoot.error.not_provided import EquipaNotProvided
from libelifoot.event.update_equipa_listener import UpdateEquipaListener
from libelifoot.provider.roster import factory as roster_factory
from libelifoot.provider.coach import factory as coach_factory


class UpdateEquipa(AsyncCommand):

    def __init__(self, equipa_file: str, prov: str, season: int,
                 listener: UpdateEquipaListener):
        self._equipa = equipa_file
        self._roster_prov = roster_factory.create(prov)
        self._coach_prov = coach_factory.create()
        self._season = season
        self._ev = listener

    def run(self) -> None:
        equipa_file = self._equipa.split(sep)[-1]
        builder = EquipaBuilder()

        try:
            players = self._roster_prov.get_players(equipa_file, self._season)
            coach = self._coach_prov.get_coach(equipa_file, self._season)

            equipa = builder.create_base_equipa(self._equipa) \
                .add_players(players) \
                .add_coach(coach) \
                .build()

            self._ev.on_update_equipa(equipa_file, equipa)
        except (EquipaNotProvided, EquipaDataNotAvailable, EquipaNotFound) as e:
            self._ev.on_update_equipa_error(e)
        except PermissionError as e:
            self._ev.on_update_equipa_error(e)
