from abc import ABC, abstractmethod
from typing import Optional

from libelifoot.use_case.dto.equipa import Equipa


class IEquipaRepository(ABC): # pragma: no cover

    @abstractmethod
    def get_equipa(self, equipa_file: str) -> Optional[Equipa]:
        """
        Retrieve an equipa by its file name.

        :equipa_file: The equipa file name.
        :return: The Equipa object if found, otherwise None.
        """

    @abstractmethod
    def save_equipa(self, equipa_file: str, equipa: Equipa) -> None:
        """
        Save an equipa to the repository.

        :equipa_file: The equipa file name.
        :equipa: The Equipa object to save.
        """
