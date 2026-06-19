from abc import ABC, abstractmethod
from typing import Optional


class ITeamMappingRepository(ABC): # pragma: no cover

    @abstractmethod
    def get_team_id(self, equipa_file: str) -> Optional[str]:
        """
        Retrieve the mapped team ID for a given equipa file path.

        :equipa_file: The path to the equipa file.
        :return: The mapped team ID if found, otherwise None.
        """

    @abstractmethod
    def get_teams(self, provider: str) -> list[str]:
        """
        Retrieve a list of team names for a given provider.

        :provider: The name of the provider.
        :return: A list of team names.
        """
