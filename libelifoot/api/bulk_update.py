from time import sleep

from libelifoot.api.async_command import AsyncCommand
from libelifoot.api import update_equipa
from libelifoot.equipa import mapping
from libelifoot.event.update_equipa_listener import UpdateEquipaListener
from libelifoot.provider.base_roster_provider import BaseRosterProvider
from libelifoot.provider.base_coach_provider import BaseCoachProvider


class Cmd(AsyncCommand):

    def __init__(self, equipa_dir: str, roster_prov: BaseRosterProvider,
                 coach_prov: BaseCoachProvider, season: int,
                 listener: UpdateEquipaListener):
        self._dir = equipa_dir
        self._roster_prov = roster_prov
        self._coach_prov = coach_prov
        self._season = season
        self._ev = listener

    def run(self) -> None:
        teams = mapping.get_teams(self._roster_prov.name)

        for team in teams:
            cmd = update_equipa.Cmd(f"{self._dir}/{team['file']}",
                                    self._roster_prov, self._coach_prov,
                                    self._season, self._ev)

            cmd.run()

            sleep(self._roster_prov.interval)  # to avoid overwhelming the data source
