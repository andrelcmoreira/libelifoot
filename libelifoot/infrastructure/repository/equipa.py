from typing import Optional

from libelifoot.domain.repository.equipa import IEquipaRepository


def get_equipa_repository() -> IEquipaRepository:
    return FileEquipaRepository()


class FileEquipaRepository(IEquipaRepository):

    def get_equipa(self, equipa_file: str) -> Optional[bytes]:
        """
        Retrieve an equipa by its file name.

        :equipa_file: The equipa file name.
        :return: The Equipa object if found, otherwise None.
        """
        try:
            with open(equipa_file, 'rb') as f:
                return f.read()
        except FileNotFoundError:
            return None

    def save_equipa(self, equipa_file: str, data: bytes) -> None:
        """
        Save an equipa to the repository.

        :equipa_file: The equipa file name.
        :equipa: The Equipa object to save.
        """
        with open(equipa_file, 'wb') as f:
            if data:
                f.write(data)
