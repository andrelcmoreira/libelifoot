from libelifoot.entity.equipa import Equipa
from libelifoot.parser.equipa import EquipaParser
from libelifoot.serializer.equipa import EquipaSerializer


class EquipaFileHandler:

    @staticmethod
    def write(file_name: str, equipa: Equipa) -> None:
        with open(file_name, 'wb') as f:
            data = EquipaSerializer.serialize(equipa)

            f.write(data)

    @staticmethod
    def read(file_name: str) -> Equipa:
        ep = EquipaParser(file_name)

        return ep.parse()
