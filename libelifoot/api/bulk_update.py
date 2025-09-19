from libelifoot.api.async_command import AsyncCommand
from libelifoot.api.update import UpdateEquipa
from libelifoot.event.update_equipa_listener import UpdateEquipaListener
from libelifoot.provider import factory

from time import sleep


class BulkUpdate(AsyncCommand):

    _UPDATE_INTERVAL = 10  # seconds

    def __init__(self, equipa_dir: str, prov: str, season: int,
                 listener: UpdateEquipaListener):
        self._dir = equipa_dir
        self._prov = factory.create(prov)
        self._season = season
        self._listener = listener

    def run(self) -> None:
        teams = self._prov.get_teams()

        for team in teams:
            cmd = UpdateEquipa(f"{self._dir}/{team['file']}", self._prov.name,
                               self._season, self._listener)

            cmd.run()

            sleep(self._UPDATE_INTERVAL)  # to avoid overwhelming the data source
