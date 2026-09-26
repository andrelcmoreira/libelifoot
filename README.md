## libelifoot

[![CI](https://github.com/andrelcmoreira/libelifoot/actions/workflows/ci.yaml/badge.svg)](https://github.com/andrelcmoreira/libelifoot/actions/workflows/ci.yaml)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL_v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![pypi](https://img.shields.io/pypi/v/libelifoot)](https://pypi.org/project/libelifoot/)

### Overview

Library to handle Elifoot 98 equipas. The main functionalities of the library are:

- Get the equipa data from an equipa file;
- Generate patch files with upstream data from an equipa file;
- Generate patches in batch from a directory of equipa files.

### Usage

Get the content of an equipa file:

```python
from sys import argv

from libelifoot import get_equipa_data


def main(equipa: str) -> None:
    print(get_equipa_data(equipa))


if __name__ == "__main__":
    main(argv[1])
```

Generate a patch file with upstream data from an equipa file:

```python
from sys import argv
from typing import Optional

from libelifoot import (
    update_equipa,
    save_equipa,
    Equipa,
    IUpdateEquipaListener
)


class EventHandler(IUpdateEquipaListener):

    def on_update_equipa(
        self,
        equipa_name: str,
        equipa_data: Optional[Equipa]
    ) -> None:
        print(f'{equipa_name}\n{equipa_data}')

        if equipa_data:
            save_equipa(f'{equipa_name}.patch', equipa_data)

    def on_update_equipa_error(self, error: str) -> None:
        print(f'ERROR: {error}')


def main(equipa: str, provider: str, season: int) -> None:
    ev = EventHandler()

    update_equipa(equipa, provider, season, ev)


if __name__ == "__main__":
    main(argv[1], argv[2], int(argv[3]))
```

See [samples](https://github.com/andrelcmoreira/libelifoot/tree/develop/samples) folder for more examples.

### Supported providers

To generate patches, the library fetches data from public football data providers. Currently, the library supports the following providers:

- **ESPN**: Good for fresh data, but it may not have historical data for all seasons.
- **Transfermarkt**: Good for historical data, but it may not have the latest data for all teams.

### Documentation

See [docs](https://github.com/andrelcmoreira/libelifoot/tree/develop/docs).
