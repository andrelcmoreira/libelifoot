from libelifoot.entity.equipa import Equipa
from libelifoot.file.equipa import EquipaFileHandler


def view(equipa: str) -> Equipa:
    return EquipaFileHandler.read(equipa)
