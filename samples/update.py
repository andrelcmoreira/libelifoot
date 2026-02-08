from sys import argv
from typing import Optional

from libelifoot import (
    update_equipa,
    Equipa,
    EquipaFileHandler,
    UpdateEquipaListener
)


class EventHandler(UpdateEquipaListener):

    def on_update_equipa(
        self,
        equipa_name: str,
        equipa_data: Optional[Equipa]
    ) -> None:
        print(f'{equipa_name}\n{equipa_data}')

        if equipa_data:
            EquipaFileHandler.write(f'{equipa_name}.patch', equipa_data)

    def on_update_equipa_error(self, error: str) -> None:
        print(f'ERROR: {error}')


def main(equipa: str, provider: str, season: int) -> None:
    ev = EventHandler()

    update_equipa(equipa, provider, season, ev)


if __name__ == "__main__":
    main(argv[1], argv[2], int(argv[3]))
