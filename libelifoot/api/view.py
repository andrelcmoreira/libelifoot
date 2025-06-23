from libelifoot.entity.equipa import Equipa
from libelifoot.parser.equipa import EquipaParser


def view(equipa: str) -> Equipa:
    ep = EquipaParser(equipa)

    return ep.parse()
