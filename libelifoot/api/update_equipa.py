import os.path

from libelifoot.api.async_command import AsyncCommand
from libelifoot.equipa import builder
from libelifoot.error.data_not_available import EquipaDataNotAvailable
from libelifoot.error.not_found import EquipaNotFound
from libelifoot.error.not_provided import EquipaNotProvided
from libelifoot.event.update_equipa_listener import UpdateEquipaListener
from libelifoot.provider.base_coach_provider import BaseCoachProvider
from libelifoot.provider.base_roster_provider import BaseRosterProvider


class Cmd(AsyncCommand):

    def __init__(self, equipa_file: str, roster_prov: BaseRosterProvider,
                 coach_prov: BaseCoachProvider, season: int,
                 listener: UpdateEquipaListener):
        self._equipa = equipa_file
        self._roster = roster_prov
        self._coach = coach_prov
        self._season = season
        self._ev = listener

    def run(self) -> None:
        equipa_builder = builder.EquipaBuilder()
        equipa_file = self._equipa.split(os.path.sep)[-1]

        try:
            players = self._roster.get_players(equipa_file, self._season)
            coach = self._coach.get_coach(equipa_file, self._season)
            equipa = equipa_builder.create_base_equipa(self._equipa) \
                .add_players(players) \
                .add_coach(coach) \
                .build()

            self._ev.on_update_equipa(equipa_file, equipa)
        except (EquipaNotProvided,
                EquipaDataNotAvailable,
                EquipaNotFound,
                PermissionError) as e:
            self._ev.on_update_equipa_error(str(e))
