from abc import ABC, abstractmethod
from typing import Optional

from libelifoot.entity.equipa import Equipa


class UpdateEquipaListener(ABC): # pragma: no cover

    @abstractmethod
    def on_update_equipa(
        self,
        equipa_name: str,
        equipa_data: Optional[Equipa]
    ) -> None:
        """
        Invoked when an equipa is successfully updated.

        :equipa_name: The name of the equipa.
        :equipa_data: The updated equipa data.
        """

    @abstractmethod
    def on_update_equipa_error(self, error: str) -> None:
        """
        Invoked when there is an error updating an equipa.

        :error: The error message.
        """
