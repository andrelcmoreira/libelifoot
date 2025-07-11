from abc import ABC, abstractmethod

from libelifoot.entity.equipa import Equipa


class UpdateEquipaListener(ABC):

    @abstractmethod
    def on_update_equipa(self, equipa_name: str, equipa_data: Equipa) -> None:
        pass

    @abstractmethod
    def on_update_equipa_error(self, error: str) -> None:
        pass
