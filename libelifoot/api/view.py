from command.command import Command
from error.header_not_found import EquipaHeaderNotFound
from error.not_found import EquipaNotFound
from event.view_equipa_listener import ViewEquipaListener
from parser.equipa import EquipaParser


class ViewEquipa(Command):

    def __init__(self, equipa_file: str, listener: ViewEquipaListener):
        self._equipa = equipa_file
        self._listener = listener

    def run(self) -> None:
        try:
            ep = EquipaParser(self._equipa)

            self._listener.on_view_equipa(ep.parse())
        except (EquipaHeaderNotFound, EquipaNotFound) as e:
            self._listener.on_view_equipa_error(e)
