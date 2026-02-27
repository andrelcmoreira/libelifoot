## libelifoot

[![CI](https://github.com/andrelcmoreira/libelifoot/actions/workflows/ci.yaml/badge.svg)](https://github.com/andrelcmoreira/libelifoot/actions/workflows/ci.yaml)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL_v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![pypi](https://img.shields.io/pypi/v/libelifoot)](https://pypi.org/project/libelifoot/)

### Overview

Library to handle Elifoot 98 equipas. The main functionalities of the library are:

- View data from an equipa file;
- Generate patch files with upstream data from an equipa file;
- Generate patches in batch from a directory of equipa files.

### Usage

View the content of an equipa file:

```python
from sys import argv

from libelifoot import view_equipa


def main(equipa: str) -> None:
    print(view_equipa(equipa))


if __name__ == "__main__":
    main(argv[1])
```

Generate a patch file with upstream data from an equipa file:

```python
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
```

Generate patches in batch based on a directory of equipa files:

```python
from sys import argv
from typing import Optional

from libelifoot import (
    bulk_update,
    Equipa,
    EquipaFileHandler,
    UpdateEquipaListener,
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


def main(equipa_dir: str, provider: str, season: int) -> None:
    ev = EventHandler()

    bulk_update(equipa_dir, provider, season, ev)


if __name__ == "__main__":
    main(argv[1], argv[2], int(argv[3]))
```

### Supported providers

To generate patches, the library fetches data from public football data providers. Currently, the library supports the following providers:

- ESPN;
- Transfermarkt.

### Documentation

See [docs](https://github.com/andrelcmoreira/libelifoot/tree/develop/docs).
