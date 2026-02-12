from libelifoot.entity.equipa import Equipa
from libelifoot.parser.equipa import EquipaParser
from libelifoot.serializer.equipa import EquipaSerializer


class EquipaFileHandler:

    @staticmethod
    def write(file_name: str, equipa: Equipa) -> None:
        """
        Write an equipa to an EFT file.

        :file_name: The file name to write the equipa to.
        :equipa: The equipa to write.
        """
        with open(file_name, 'wb') as f:
            data = EquipaSerializer.serialize(equipa)

            if data:
                f.write(data)

    @staticmethod
    def read(file_name: str) -> Equipa:
        """
        Read an equipa from an EFT file.

        :file_name: The file name to read the equipa from.
        :return: The equipa read from the file.
        """
        ep = EquipaParser(file_name)

        return ep.parse()
