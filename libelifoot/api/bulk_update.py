from libelifoot.api.command import Command
from libelifoot.api.update import UpdateEquipa
from libelifoot.event.update_equipa_listener import UpdateEquipaListener

import libelifoot.provider.factory


class BulkUpdate(Command):

    def __init__(self, equipa_dir: str, prov: str, season: int,
                 listener: UpdateEquipaListener):
        self._dir = equipa_dir
        self._prov = libelifoot.provider.factory.create(prov)
        self._season = season
        self._listener = listener

    def run(self) -> None:
        teams = self._prov.get_teams()

        for team in teams:
            cmd = UpdateEquipa(self._dir + '/' + team['file'], self._prov.name,
                               self._season, self._listener)

            cmd.run()
